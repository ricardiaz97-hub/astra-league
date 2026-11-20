// receptor local para tools/fbx2anim.html: guarda el JSON que manda el navegador. Uso: node tools/anim-recv.js anims
const http=require('http'),fs=require('fs'),path=require('path');const OUT=process.argv[2];
http.createServer((q,r)=>{r.setHeader('Access-Control-Allow-Origin','*');if(q.method!=='POST'){r.end();return;}let b='';q.on('data',c=>b+=c);q.on('end',()=>{fs.writeFileSync(path.join(OUT,path.basename(q.url)),b);console.log('saved',q.url,b.length);r.end('ok');process.exit(0);});}).listen(8765,'127.0.0.1',()=>console.log('listening'));
