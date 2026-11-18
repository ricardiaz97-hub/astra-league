const fs=require('fs'),zlib=require('zlib');const [src,out]=process.argv.slice(2);
const v=fs.readFileSync(src,'utf8').split(/\r?\n/).filter(l=>/^[\d.\-]+\s+[\d.\-]+\s+[\d.\-]+\s*$/.test(l.trim())).map(l=>l.trim().split(/\s+/).map(Number));
const N=32;if(v.length!==N*N*N)throw new Error('bad lut '+v.length);
const W=N*N,H=N,raw=Buffer.alloc((W*3+1)*H);
for(let b=0;b<N;b++)for(let g=0;g<N;g++)for(let r=0;r<N;r++){const c=v[r+g*N+b*N*N],o=g*(W*3+1)+1+(b*N+r)*3;for(let k=0;k<3;k++)raw[o+k]=Math.round(Math.min(1,Math.max(0,c[k]))*255);}
const crc=b=>{let c=~0;for(const x of b){c^=x;for(let k=0;k<8;k++)c=c&1?(c>>>1)^0xedb88320:c>>>1;}return ~c>>>0;};
const ch=(t,d)=>{const l=Buffer.alloc(4);l.writeUInt32BE(d.length);const td=Buffer.concat([Buffer.from(t),d]);const c=Buffer.alloc(4);c.writeUInt32BE(crc(td));return Buffer.concat([l,td,c]);};
const ih=Buffer.alloc(13);ih.writeUInt32BE(W,0);ih.writeUInt32BE(H,4);ih[8]=8;ih[9]=2;
fs.writeFileSync(out,Buffer.concat([Buffer.from([137,80,78,71,13,10,26,10]),ch('IHDR',ih),ch('IDAT',zlib.deflateSync(raw)),ch('IEND',Buffer.alloc(0))]));
const p=v[N-1+(N-1)*N+(N-1)*N*N],m=v[16+16*N+16*N*N];console.log('ok white',p,'mid',m);
