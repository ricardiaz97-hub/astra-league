// Checks SEWER_LAYOUT in index.html before playing: rooms that overlap, tunnels that cut through rooms or each other,
// tunnels whose ends are not inside a room, and rooms too small for the tunnels that open into them.
// Usage: node tools/sewer-check.js
const fs = require('fs');
const src = fs.readFileSync(__dirname + '/../index.html', 'utf8');
const a = src.indexOf('const SEWER_LAYOUT='), b = src.indexOf('function buildSewer(){');
if (a < 0 || b < 0) { console.error('SEWER_LAYOUT not found'); process.exit(1); }
const L = new Function(src.slice(a, b) + ';return SEWER_LAYOUT;')();
const P = (x, z) => [(x - 800) / 3.5 * L.K, (z - 460) / 3.5 * L.K];
const blob = (cx, cz, r, k, seed) => Array.from({ length: 36 }, (_, i) => { const t = i / 36 * 2 * Math.PI, rr = r * (1 + k * Math.sin(3 * t + seed) + k * .5 * Math.cos(5 * t + seed * 2)); return [cx + Math.cos(t) * rr, cz + Math.sin(t) * rr]; });
const inPoly = (x, z, pts) => { let c = false; for (let i = 0, j = pts.length - 1; i < pts.length; j = i++) { const [p, q] = pts[i], [e, d] = pts[j]; if ((q > z) !== (d > z) && x < (e - p) * (z - q) / (d - q) + p) c = !c; } return c; };
const rooms = L.rooms.map(r => ({ id: r.id, y: r.y, h: r.h, pts: (r.blob ? blob(...r.blob) : r.poly).map(p => P(p[0], p[1])) }));
const roomAt = (x, z, y) => rooms.find(r => y > r.y - 3 && y < r.y + r.h && inPoly(x, z, r.pts));
const errs = [];
// rooms overlapping in plan and height
for (let i = 0; i < rooms.length; i++) for (let j = i + 1; j < rooms.length; j++) {
  const A = rooms[i], B = rooms[j]; if (A.y + A.h < B.y - 2 || B.y + B.h < A.y - 2) continue;
  if (A.pts.some(p => inPoly(p[0], p[1], B.pts)) || B.pts.some(p => inPoly(p[0], p[1], A.pts))) errs.push(`rooms overlap: ${A.id} / ${B.id}`);
}
// tunnels: dense polyline samples (close enough to the Catmull-Rom curve for clearance checks)
const tuns = L.tunnels.map((t, ti) => {
  const w = t.w || 20, h = t.h || 16, s = [];
  for (let i = 1; i < t.pts.length; i++) { const [ax, az, ay] = t.pts[i - 1], [bx, bz, by] = t.pts[i], [x0, z0] = P(ax, az), [x1, z1] = P(bx, bz), n = Math.ceil(Math.hypot(x1 - x0, z1 - z0));
    for (let k = 0; k < n; k++) { const f = k / n; s.push({ x: x0 + (x1 - x0) * f, z: z0 + (z1 - z0) * f, y: ay + (by - ay) * f }); } }
  const last = t.pts[t.pts.length - 1], [lx, lz] = P(last[0], last[1]); s.push({ x: lx, z: lz, y: last[2] });
  return { ti, w, h, s, A: roomAt(s[0].x, s[0].z, s[0].y), B: roomAt(lx, lz, last[2]) };
});
for (const t of tuns) {
  if (!t.A) errs.push(`tunnel ${t.ti}: start is not inside a room`);
  if (!t.B) errs.push(`tunnel ${t.ti}: end is not inside a room`);
  const hit = new Set(); for (const p of t.s) { const r = roomAt(p.x, p.z, p.y); if (r && r !== t.A && r !== t.B) hit.add(r.id); }
  for (const id of hit) errs.push(`tunnel ${t.ti}: cuts through room ${id}`);
  for (const r of [t.A, t.B]) if (r) { let cx = 0, cz = 0; for (const [x, z] of r.pts) { cx += x; cz += z; } cx /= r.pts.length; cz /= r.pts.length;
    const rmin = Math.min(...r.pts.map(([x, z]) => Math.hypot(x - cx, z - cz))); if (rmin < t.w / 2 + 3) errs.push(`room ${r.id} too narrow (${rmin.toFixed(1)} m) for tunnel ${t.ti} (${t.w} m wide)`); }
}
for (let i = 0; i < tuns.length; i++) for (let j = i + 1; j < tuns.length; j++) {
  const A = tuns[i], B = tuns[j], need = (A.w + B.w) / 2 + 1.5; let worst = 1e9;
  for (const p of A.s) { if (roomAt(p.x, p.z, p.y)) continue; for (const q of B.s) { if (roomAt(q.x, q.z, q.y) || Math.abs(p.y - q.y) > Math.max(A.h, B.h) + 2) continue; worst = Math.min(worst, Math.hypot(p.x - q.x, p.z - q.z)); } }
  if (worst < need) errs.push(`tunnels ${i} and ${j} too close: ${worst.toFixed(1)} m (need ${need.toFixed(1)})`);
}
let len = 0; for (const t of tuns) for (let i = 1; i < t.s.length; i++) len += Math.hypot(t.s[i].x - t.s[i - 1].x, t.s[i].z - t.s[i - 1].z);
console.log(`${rooms.length} rooms, ${tuns.length} tunnels, ${Math.round(len)} m of tunnel`);
if (errs.length) { console.log(errs.join('\n')); process.exit(1); } else console.log('layout OK');
