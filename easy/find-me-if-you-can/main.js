const $ = q => document.querySelector(q);
const $a = q => document.querySelectorAll(q);

const boxes = [];
for (let i = 0; i < 384; i++) {
    const box = document.createElement('button');
    box.className = 'box';
    box.textContent = 'Flag';
    document.body.appendChild(box);
    boxes.push(box);
}

let flagbox = boxes[Math.floor(Math.random() * boxes.length)];
for (const box of boxes) {
    if (box === flagbox) {
        box.onclick = () => {
            let enc = "\u0021\u0036\u0024\u0019\u0005\u000f\u004c\u000c\u0007\u0017\u004f\u0001\u0016\u0004\u004c\u0001\u000e\u0017\u0000\u001f";
            
            let rw = []
            for (const e of enc) {
                rw.push(e['\x63har\x43ode\x41t'](0) ^ 0x62);
            }
            const x = rw['\x6dap'](x => String['from\x43har\x43ode'](x));
            alert(`${x['\x6aoin']('')}`);
        };
        flagbox = null;
    } else {
        box.onclick = () => alert('no flag here');
    }
}