"""BVH (Motifect) -> anims/*.json del juego.
Formato de salida igual que anims/ual.json: por hueso humanoide, cuaternión [x,y,z,w] por cuadro =
rotación MUNDO del hueso respecto al reposo (T-pose del BVH), en ejes del modelo (Y arriba, de frente a +Z).
'drop' = altura de cadera relativa al reposo, normalizada a la altura de cadera.
Uso: python tools/bvh2anim.py <carpeta BVH> <salida.json> <prefijo> [config.json]
"""
import json, math, os, sys

MAP = {'Hips': 'hips', 'Spine1': 'spine', 'Spine2': 'chest', 'Chest': 'upperChest', 'Neck1': 'neck', 'Head': 'head',
       'LeftShoulder': 'leftShoulder', 'LeftArm': 'leftUpperArm', 'LeftForeArm': 'leftLowerArm', 'LeftHand': 'leftHand',
       'RightShoulder': 'rightShoulder', 'RightArm': 'rightUpperArm', 'RightForeArm': 'rightLowerArm', 'RightHand': 'rightHand',
       'LeftLeg': 'leftUpperLeg', 'LeftShin': 'leftLowerLeg', 'LeftFoot': 'leftFoot', 'LeftToeBase': 'leftToes',
       'RightLeg': 'rightUpperLeg', 'RightShin': 'rightLowerLeg', 'RightFoot': 'rightFoot', 'RightToeBase': 'rightToes'}


def qmul(a, b):
    ax, ay, az, aw = a; bx, by, bz, bw = b
    return (aw*bx + ax*bw + ay*bz - az*by, aw*by - ax*bz + ay*bw + az*bx, aw*bz + ax*by - ay*bx + az*bw, aw*bw - ax*bx - ay*by - az*bz)


def qaxis(ax, deg):
    h = math.radians(deg) / 2; s = math.sin(h)
    return {'X': (s, 0, 0, math.cos(h)), 'Y': (0, s, 0, math.cos(h)), 'Z': (0, 0, s, math.cos(h))}[ax]


def qrot(q, v):
    p = qmul(qmul(q, (v[0], v[1], v[2], 0)), (-q[0], -q[1], -q[2], q[3]))
    return p[:3]


def parse(path):
    tok = open(path).read().split()
    i = 0; joints = []; stack = []
    while tok[i] != 'MOTION':
        t = tok[i]
        if t in ('ROOT', 'JOINT'):
            joints.append({'name': tok[i+1], 'parent': stack[-1] if stack else -1, 'ch': [], 'off': (0, 0, 0)}); i += 2; continue
        if t == 'End':
            joints.append({'name': '_end', 'parent': stack[-1], 'ch': [], 'off': (0, 0, 0)}); i += 2; continue
        if t == '{': stack.append(len(joints)-1)
        elif t == '}': stack.pop()
        elif t == 'OFFSET': joints[stack[-1]]['off'] = tuple(float(x) for x in tok[i+1:i+4]); i += 4; continue
        elif t == 'CHANNELS':
            n = int(tok[i+1]); joints[stack[-1]]['ch'] = tok[i+2:i+2+n]; i += 2+n; continue
        i += 1
    nf = int(tok[i+2]); ft = float(tok[i+5]); vals = [float(x) for x in tok[i+6:]]
    stride = sum(len(j['ch']) for j in joints); frames = [vals[k*stride:(k+1)*stride] for k in range(nf)]
    return joints, frames, ft


CHILD = {'Hips': 'Spine1', 'Spine1': 'Spine2', 'Spine2': 'Chest', 'Chest': 'Neck1', 'Neck1': 'Head',
         'LeftShoulder': 'LeftArm', 'LeftArm': 'LeftForeArm', 'LeftForeArm': 'LeftHand', 'RightShoulder': 'RightArm', 'RightArm': 'RightForeArm', 'RightForeArm': 'RightHand',
         'LeftLeg': 'LeftShin', 'LeftShin': 'LeftFoot', 'LeftFoot': 'LeftToeBase', 'RightLeg': 'RightShin', 'RightShin': 'RightFoot', 'RightFoot': 'RightToeBase'}


def restdirs(joints, idx):
    pos = []
    for j in joints:
        pp = pos[j['parent']] if j['parent'] >= 0 else (0, 0, 0)
        pos.append(tuple(a+b for a, b in zip(pp, j['off'])))
    out = {}
    for a, b in CHILD.items():
        d = [y-x for x, y in zip(pos[idx[a]], pos[idx[b]])]; l = math.sqrt(sum(x*x for x in d)) or 1
        out[MAP[a]] = [round(x/l, 4) for x in d]
    return out


HPAR = {'spine': 'hips', 'chest': 'spine', 'upperChest': 'chest', 'neck': 'upperChest', 'head': 'neck', 'leftShoulder': 'upperChest', 'leftUpperArm': 'leftShoulder',
        'leftLowerArm': 'leftUpperArm', 'leftHand': 'leftLowerArm', 'rightShoulder': 'upperChest', 'rightUpperArm': 'rightShoulder', 'rightLowerArm': 'rightUpperArm',
        'rightHand': 'rightLowerArm', 'leftUpperLeg': 'hips', 'leftLowerLeg': 'leftUpperLeg', 'leftFoot': 'leftLowerLeg', 'leftToes': 'leftFoot',
        'rightUpperLeg': 'hips', 'rightLowerLeg': 'rightUpperLeg', 'rightFoot': 'rightLowerLeg', 'rightToes': 'rightFoot'}
# torsión máxima (grados) de cada hueso sobre su propio eje respecto al padre: el mocap de IA retuerce brazos y piernas y aplasta la malla
TWIST = {'leftUpperArm': 35, 'rightUpperArm': 35, 'leftLowerArm': 70, 'rightLowerArm': 70, 'leftHand': 30, 'rightHand': 30, 'leftShoulder': 10, 'rightShoulder': 10,
         'leftUpperLeg': 25, 'rightUpperLeg': 25, 'leftLowerLeg': 8, 'rightLowerLeg': 8, 'leftFoot': 15, 'rightFoot': 15, 'leftToes': 5, 'rightToes': 5,
         'spine': 25, 'chest': 20, 'upperChest': 20, 'neck': 30, 'head': 50}
TAX = {'leftHand': 'leftLowerArm', 'rightHand': 'rightLowerArm', 'leftToes': 'leftFoot', 'rightToes': 'rightFoot', 'head': 'neck'}
inv = lambda q: (-q[0], -q[1], -q[2], q[3])


def nrm(q):
    l = math.sqrt(sum(x*x for x in q)) or 1
    return tuple(x/l for x in q)


def clamp_twist(rel, axis, lim):
    d = sum(a*b for a, b in zip(rel[:3], axis))
    tw = nrm((axis[0]*d, axis[1]*d, axis[2]*d, rel[3]))
    if tw[3] < 0: tw = tuple(-x for x in tw)
    ang = 2*math.degrees(math.acos(min(1, tw[3])))
    if ang <= lim: return rel
    sw = qmul(rel, inv(tw)); h = math.radians(lim)/2*(1 if d*rel[3] >= 0 else -1)
    return qmul(sw, (axis[0]*math.sin(h), axis[1]*math.sin(h), axis[2]*math.sin(h), math.cos(h)))


def slerp(a, b, t):
    d = sum(x*y for x, y in zip(a, b))
    if d < 0: b = tuple(-x for x in b); d = -d
    if d > .9995: return nrm(tuple(x+(y-x)*t for x, y in zip(a, b)))
    th = math.acos(d); s = math.sin(th)
    return tuple((x*math.sin((1-t)*th)+y*math.sin(t*th))/s for x, y in zip(a, b))


def clean(frames_q, rd):
    """frames_q: lista de dict hueso->rotación mundo. Limita torsión (de padre a hijo, conservando lo local de los hijos) y suaviza el temblor."""
    order = ['hips'] + [b for b in HPAR]  # HPAR va de padres a hijos
    out = []
    for W in frames_q:
        W2 = {'hips': W['hips']}
        for b in order[1:]:
            p = HPAR[b]; rel = qmul(inv(W[p]), W[b])
            ax = rd.get(b) or rd.get(TAX.get(b, ''))
            if ax and b in TWIST: rel = clamp_twist(rel, tuple(ax), TWIST[b])
            W2[b] = nrm(qmul(W2[p], rel))
        out.append(W2)
    sm = []
    for i in range(len(out)):  # suavizado 1-2-1 (quita el temblor sin perder la pose)
        a, b, c = out[max(0, i-1)], out[i], out[min(len(out)-1, i+1)]
        sm.append({k: slerp(slerp(a[k], c[k], .5), b[k], .5) for k in b})
    return sm


def convert(path, cfg):
    joints, frames, ft = parse(path)
    idx = {j['name']: k for k, j in enumerate(joints)}
    leg = sum(-joints[idx[n]]['off'][1] for n in ('LeftShin', 'LeftFoot')) * 1.06
    out = {k: [] for k in MAP.values()}; hipy = []; energy = []; prev = None; raw = []
    yawfix = None
    for fr in frames:
        c = 0; world = []; pos0 = None
        for j in joints:
            q = (0, 0, 0, 1)
            for ch in j['ch']:
                v = fr[c]; c += 1
                if ch.endswith('rotation'): q = qmul(q, qaxis(ch[0], v))
                elif ch == 'Yposition': pos0 = v
            pw = world[j['parent']] if j['parent'] >= 0 else (0, 0, 0, 1)
            world.append(qmul(pw, q))
        if yawfix is None:
            f = qrot(world[idx['Hips']], (0, 0, 1)); yaw = math.atan2(f[0], f[2])
            yawfix = (0, math.sin(-yaw/2), 0, math.cos(-yaw/2))
        cur = {}
        for bn, hb in MAP.items():
            q = qmul(yawfix, world[idx[bn]])
            if hb == 'neck' and 'Neck2' in idx: q = slerp(q, qmul(yawfix, world[idx['Neck2']]), .55)  # el rig tiene un solo hueso de cuello
            cur[hb] = q
        raw.append(cur)
        hipy.append(pos0 or 0)
        if prev:
            e = sum(2*math.acos(min(1, abs(sum(a*b for a, b in zip(cur[k], prev[k]))))) for k in cur)
        else: e = 0
        energy.append(e); prev = cur
    rd = restdirs(joints, idx)
    for hb, ch in (('leftHand', 'LeftHandMiddle1'), ('rightHand', 'RightHandMiddle1')):
        if ch in idx:
            v = joints[idx[ch]]['off']; l = math.sqrt(sum(x*x for x in v)) or 1; rd[hb] = [x/l for x in v]
    for W in clean(raw, rd):
        for k, q in W.items():
            l = out[k]
            if l and sum(x*y for x, y in zip(l[-1], q)) < 0: q = tuple(-x for x in q)
            l.append(q)
    n = len(frames)
    a, b = 0, n
    if cfg.get('trim', True):
        sm = [sum(energy[max(0, i-2):i+3])/5 for i in range(n)]
        mx = max(sm) or 1; th = mx*cfg.get('th', .1)
        act = [i for i in range(n) if sm[i] > th]
        if act: a = max(0, act[0]-cfg.get('lead', 3)); b = min(n, act[-1]+cfg.get('tail', 6))
    if 'cut' in cfg: a, b = cfg['cut']
    rest = leg if leg > 1 else (hipy[0] or 1)
    bones = {k: [round(x, 3) for q in v[a:b] for x in q] for k, v in out.items()}
    drop = [round((h-hipy[a])/rest, 3) if cfg.get('dropRel') else round((h-rest)/rest, 3) for h in hipy[a:b]]
    res = {'src': 'Motifect ' + os.path.basename(path)[:-4], 'fps': round(1/ft), 'frames': b-a, 'mode': cfg.get('mode', 'once'), 'rate': cfg.get('rate', 1), 'speed': 0, 'bones': bones}
    if cfg.get('drop', True): res['drop'] = drop
    res['rdir'] = restdirs(joints, idx)  # dirección de reposo de cada hueso: el juego la alinea con el rig del personaje
    return res


if __name__ == '__main__':
    src, dst, pre = sys.argv[1:4]
    conf = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
    skip = set(conf.get('_skip', []))
    allc = {}
    for fn in sorted(os.listdir(src)):
        if not fn.endswith('.bvh'): continue
        name = fn[:-4]
        if name in skip: continue
        r = convert(os.path.join(src, fn), conf.get(name, {}))
        allc[pre + name] = r
        print(pre + name, r['frames'], 'drop', min(r['drop']) if r.get('drop') else '-', max(r['drop']) if r.get('drop') else '-')
    d0 = sorted(r['drop'][0] for r in allc.values() if r.get('drop') and abs(r['drop'][0]) < .2)
    off = d0[len(d0)//2] if d0 else 0  # de pie = 0: corrige la estimación de altura de cadera
    for r in allc.values():
        if r.get('drop'): r['drop'] = [round(x-off, 3) for x in r['drop']]
    print('drop offset', off)
    json.dump(allc, open(dst, 'w'), separators=(',', ':'))
    print(dst, os.path.getsize(dst))
