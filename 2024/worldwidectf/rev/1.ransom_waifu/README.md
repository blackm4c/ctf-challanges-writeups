## [rev] Ransom Waifu

**Author:** yun

**Description:**
```
The hackers' ransomware has locked up my waifu!
Help me find the passwords those hackers used!
In fact, I've already recovered 2/3 of the password! but I need your help to find the last part!

Alternate Link: https://ransom-yun.pages.dev/

https://ransom.wwctf.com/
```

### Overview

Upon visiting the link provided in the challenge description, we are greeted by a login page prompting for a password. The password is validated through a function named ``check``, as seen in the code snippet below:

```js
if (check([password, [252, 174, 221, 116, 74, 140, 110, 29], [166, 74, 96, 96, 218, 220, 56, 111]])) {
    result.textContent = 'Correct password!';
    result.style.color = 'green';
    unlock(password);
} else {
    result.textContent = 'Incorrect password.';
    result.style.color = 'red';
}
```

The ``check`` function is defined within the ``ransomware.js`` file, but unfortunately, the file's contents are heavily obfuscated, making it difficult to understand.

### Simplifying the obfuscated code

Fortunately, we can use an online deobfuscation tool like <https://obf-io.deobfuscate.io/> to make the code more readable.

```js
function check(_0x25883e) {
  const _0x55b20f = [ ... ]; // Very big, removed for clarity
  const _0x5ab57e = ["1DwVRiEiGWjuyupm", "vYb2h2aIafJZwgFX", "6kbUutVIpZMxQYvc", "7QakoJNVWhG5ymIp", "poB7FQorqiVyhK5t", "7W2gzK0RBrwugCj1", "XIpQkMw4ISxevkCX", "LOEYrHUc1FSi3472", "3JkFWJMpwKlUqWqQ", "l5wN4Rh3eeS8DRsr", "6eMeF1wcAxpjHw10", "ZOVFVc4IYO42SqW4", "sBZO1SnyyWECqtfA", "HbHq2ZbQRVaAQn2s", "mLONgGjM6o1iN4TF"];
  const _0x11a6b6 = {
    "1DwVRiEiGWjuyupm": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgbGV0IGEgPSB5W3gucG9wKCldLCBiID0geVt4LnBvcCgpXQ0KICAgICAgICByZXR1cm4gYlthXQ0KICAgIH0=",
    vYb2h2aIafJZwgFX: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0uY2hhckNvZGVBdCgwKQ0KICAgIH0=",
    "6kbUutVIpZMxQYvc": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuICF5W3gucG9wKCldDQogICAgfQ==",
    "7QakoJNVWhG5ymIp": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgbGV0IGEgPSB5W3gucG9wKCldLCBiID0geVt4LnBvcCgpXQ0KICAgICAgICByZXR1cm4gYiAlIGENCiAgICB9",
    poB7FQorqiVyhK5t: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gKiB5W3gucG9wKCldDQogICAgfQ==",
    "7W2gzK0RBrwugCj1": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIDEgLyAoeVt4LnBvcCgpXSAvIHlbeC5wb3AoKV0pDQogICAgfQ==",
    XIpQkMw4ISxevkCX: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgbGV0IGEgPSB5W3gucG9wKCldLCBiID0geVt4LnBvcCgpXQ0KICAgICAgICBsZXQgY2FycnkgPSBhICYgYjsNCiAgICAgICAgbGV0IHJlc3VsdCA9IGEgXiBiOw0KICAgICAgICB3aGlsZSAoY2FycnkgIT0gMCkgew0KICAgICAgICAgICAgbGV0IHNoaWZ0ZWRjYXJyeSA9IGNhcnJ5IDw8IDE7DQogICAgICAgICAgICBjYXJyeSA9IHJlc3VsdCAmIHNoaWZ0ZWRjYXJyeTsNCiAgICAgICAgICAgIHJlc3VsdCBePSBzaGlmdGVkY2Fycnk7DQogICAgICAgIH0NCiAgICAgICAgcmV0dXJuIHJlc3VsdA0KICAgIH0=",
    LOEYrHUc1FSi3472: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgbGV0IGIgPSB5W3gucG9wKCldLCBhID0geVt4LnBvcCgpXQ0KICAgICAgICBsZXQgY2FycnkgPSBhICYgKH5iICsgMSk7DQogICAgICAgIGxldCByZXN1bHQgPSBhIF4gKH5iICsgMSk7DQogICAgICAgIHdoaWxlIChjYXJyeSAhPSAwKSB7DQogICAgICAgICAgICBsZXQgc2hpZnRlZGNhcnJ5ID0gY2FycnkgPDwgMTsNCiAgICAgICAgICAgIGNhcnJ5ID0gcmVzdWx0ICYgc2hpZnRlZGNhcnJ5Ow0KICAgICAgICAgICAgcmVzdWx0IF49IHNoaWZ0ZWRjYXJyeTsNCiAgICAgICAgfQ0KICAgICAgICByZXR1cm4gcmVzdWx0DQogICAgfQ==",
    "3JkFWJMpwKlUqWqQ": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gPT09IHlbeC5wb3AoKV0NCiAgICB9",
    l5wN4Rh3eeS8DRsr: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gIT09IHlbeC5wb3AoKV0NCiAgICB9",
    "6eMeF1wcAxpjHw10": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gJiB5W3gucG9wKCldDQogICAgfQ==",
    ZOVFVc4IYO42SqW4: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gXiB5W3gucG9wKCldDQogICAgfQ==",
    sBZO1SnyyWECqtfA: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gfCB5W3gucG9wKCldDQogICAgfQ==",
    HbHq2ZbQRVaAQn2s: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gJiYgeVt4LnBvcCgpXQ0KICAgIH0=",
    mLONgGjM6o1iN4TF: "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgcmV0dXJuIHlbeC5wb3AoKV0gfHwgeVt4LnBvcCgpXQ0KICAgIH0="
  };
  const _0x1c72ba = [ ... ]; // Very big, removed for clarity
  const _0x584466 = [];
  for (let _0x4426f4 = 0; _0x4426f4 < _0x25883e.length; _0x4426f4++) {
    _0x1c72ba[_0x4426f4] = _0x25883e[_0x4426f4];
  }
  function _0x37448b(_0x5f5c9d) {
    _0x1c72ba.push(_0x5f5c9d);
    return _0x1c72ba.length - 1;
  }
  _0x55b20f.forEach(_0x5e5b3d => {
    if (typeof _0x5e5b3d === "string") {
      const _0xc55560 = eval('(' + atob(_0x11a6b6[_0x5ab57e[parseInt(_0x5e5b3d)]]) + ')');
      _0x584466.push(_0x37448b(_0xc55560(_0x584466, _0x1c72ba)));
    } else {
      _0x584466.push(_0x5e5b3d);
    }
  });
  return _0x1c72ba[_0x584466.pop()];
}
```

We notice that the code contains Base64-encoded strings, which, when decoded, reveal additional JavaScript code.

```js
//  const _0x11a6b6 = {
//      "1DwVRiEiGWjuyupm": "ZnVuY3Rpb24gKHgsIHkpIHsNCiAgICAgICAgbGV0IGEgPSB5W3gucG9wKCldLCBiID0geVt4LnBvcCgpXQ0KICAgICAgICByZXR1cm4gYlthXQ0KICAgIH0=",
//      ...
//  };

function (x, y) {
    let a = y[x.pop()], b = y[x.pop()]
    return b[a]
}
```

From this, it becomes evident that the code implements a form of a VM written in JavaScript. With careful renaming of variables and restructuring the logic, we can derive a more comprehensible version of the program as seen below.

```js
function check(user_input) {
    const bytecode = [ ... ]; // Very big, removed for clarity
    var functions = [];

    functions[0] = (x, y) => {    
        let a = y[x.pop()], b = y[x.pop()];
        return b[a]
    }
    functions[1] = (x, y) => {        
        return y[x.pop()];
    }
    functions[2] = (x, y) => {
        return !y[x.pop()];
    }
    functions[3] = (x, y) => {
        let a = y[x.pop()], b = y[x.pop()];        
        return b%a;
    }
    functions[4] = (x, y) => {
        return y[x.pop()] * y[x.pop()];
    }
    functions[5] = (x, y) => {        
        return 1 / (y[x.pop()] / y[x.pop()]);
    }
    functions[6] = (x, y) => {
        let a = y[x.pop()], b = y[x.pop()]
        let carry = a & b;
        let result = a ^ b;
        while (carry != 0) {
            let shiftedcarry = carry << 1;
            carry = result & shiftedcarry;
            result ^= shiftedcarry;
        }
                
        return result;
    }
    functions[7] = (x, y) => {
        let b = y[x.pop()], a = y[x.pop()]
        let carry = a & (~b + 1);
        let result = a ^ (~b + 1);
        while (carry != 0) {
            let shiftedcarry = carry << 1;
            carry = result & shiftedcarry;
            result ^= shiftedcarry;
        }
        
        return result;
    }
    functions[8] = (x, y) => {
        return y[x.pop()] === y[x.pop()];
    }
    functions[9] = (x, y) => {
        return y[x.pop()] !== y[x.pop()];
    }
    functions[10] = (x, y) => {
        return y[x.pop()] & y[x.pop()];
    }
    functions[11] = (x, y) => {
        return y[x.pop()] ^ y[x.pop()];
    }
    functions[12] = (x, y) => {
        return y[x.pop()] | y[x.pop()];
    }
    functions[13] = (x, y) => {
        return y[x.pop()] && y[x.pop()];
    }
    functions[14] = (x, y) => {
        return y[x.pop()] || tempy[x.pop()];
    }


    const program = [ ... ]; // Very big, removed for clarity
    const stack = [];
    for (let i = 0; i < user_input.length; i++) {
        program[i] = user_input[i];
    }

    bytecode.forEach(instruction => {
        if (typeof instruction === 'string') {
            const opcode_function = functions[parseInt(instruction)];
            func_count[parseInt(instruction)] += 1;

            var op_res = opcode_function(stack, program);

            program.push(op_res);

            stack.push(program.length - 1)
        } else {
            stack.push(instruction);
        }
    });

    return program[stack.pop()];
}
```

Now, this is a lot more readable!

### Analyzing the VM

To begin our analysis, we can log how frequently each function is executed. This provides insight into the flow of the program and helps us identify key operations or patterns in the VM's logic.

```
function0: 608
function1: 152
function2: 0
function3: 304
function4: 114
function5: 0
function6: 114
function7: 0
function8: 38
function9: 0
function10: 0
function11: 152
function12: 0
function13: 37
function14: 0
```

We observe that the function execution count remains unchanged regardless of the input, indicating that the virtual machine performs a consistent number of operations for every input. Among these functions, ``function8`` performs a straightforward comparison ``(a === b)``, leading us to infer that the flag is 38 characters long, with each character being individually checked.

By adding additional logging, a pattern becomes apparent. For instance, here's an excerpt of the observed operations:

```
password[1] = 11
password[2] = 22
22 ^ 11 = 29
array_1[1] = 174
174 * 29 = 5046
array_2[1] = 74
74 + 5046 = 5120
5120 ^ 188 = 5308
password[1] = 11
password[0] = 0
0 + 11 = 11
array_1[1] = 174
174 ^ 11 = 165
array_2[1] = 74
74 * 165 = 12210
57 + 12210 = 12267
12267 ^ 5308 = 15191
213 * 15191 = 3235683
1410273 === 3235683 = false
```

Which can be rewritte as:

``1410273 == (213 * ((57 + (array_2[1] * (array_1[1] ^ ((password[0]) + (password[1]))))) ^ ((array_2[1] + (array_1[1] * (password[2] ^ password[1]))) ^ 188)))``

This pattern repeats itself 38 times, with variations in the specific values used in each iteration. Given the repetitive nature of the logic, it becomes clear that the program validates each character of the password sequentially against a set of constraints.

Since my JavaScript skills are limited, I wrote a Python script that parses the output and formats it into a form that the Z3 solver can understand:

```py
import re

def parse_and_transform(input_text):
    output = ""
    
    blocks = input_text.strip().split("\n\n")
    for block in blocks:
        block = block[1:].replace("\n", " ")
    
        lines = block.split(" ")
    
        i = 0

        for line in lines:
            print(f"{i}: {line}")
            i += 1
        

        output += f"\ns.add({lines[74]} == ({lines[69]} * (({lines[59]} + ({lines[51]} * ({lines[43]} ^ (({lines[35]}) + ({lines[32]}))))) ^ (({lines[51]} + ({lines[43]} * ({lines[3]} ^ {lines[0]}))) ^ {lines[29]}))))"
    
    return output

input_text = """password[1] = 11
password[2] = 22
22 ^ 11 = 29
array_1[1] = 174
174 * 29 = 5046
array_2[1] = 74
74 + 5046 = 5120
5120 ^ 188 = 5308
password[1] = 11
password[0] = 0
0 + 11 = 11
array_1[1] = 174
174 ^ 11 = 165
array_2[1] = 74
74 * 165 = 12210
57 + 12210 = 12267
12267 ^ 5308 = 15191
213 * 15191 = 3235683
1410273 === 3235683 = false


password[19] = 99
password[20] = 0
0 ^ 99 = 99
...
"""

output = parse_and_transform(input_text)
print(output)
```

With this we can construct the final solve script.

```py
from z3 import *

array_1 = [252, 174, 221, 116, 74, 140, 110, 29]
array_2 = [166, 74, 96, 96, 218, 220, 56, 111]

password = [BitVec("c_{}".format(i), 32) for i in range(38)]

s = Solver()

for i in range(38):
    s.add(password[i] >= 0, password[i] <= 255)

s.add(103569 == (69 * ((69 + (array_2[0] * (array_1[0] ^ ((password[37]) + (password[0]))))) ^ ((array_2[0] + (array_1[0] * (password[1] ^ password[0]))) ^ 14))))
s.add(1410273 == (213 * ((57 + (array_2[1] * (array_1[1] ^ ((password[0]) + (password[1]))))) ^ ((array_2[1] + (array_1[1] * (password[2] ^ password[1]))) ^ 188))))
s.add(1194466 == (182 * ((38 + (array_2[2] * (array_1[2] ^ ((password[1]) + (password[2]))))) ^ ((array_2[2] + (array_1[2] * (password[3] ^ password[2]))) ^ 236))))
s.add(3304794 == (254 * ((248 + (array_2[3] * (array_1[3] ^ ((password[2]) + (password[3]))))) ^ ((array_2[3] + (array_1[3] * (password[4] ^ password[3]))) ^ 83))))
s.add(4250975 == (115 * ((101 + (array_2[4] * (array_1[4] ^ ((password[3]) + (password[4]))))) ^ ((array_2[4] + (array_1[4] * (password[5] ^ password[4]))) ^ 168))))
s.add(1434672 == (144 * ((162 + (array_2[5] * (array_1[5] ^ ((password[4]) + (password[5]))))) ^ ((array_2[5] + (array_1[5] * (password[6] ^ password[5]))) ^ 205))))
s.add(1657074 == (151 * ((125 + (array_2[6] * (array_1[6] ^ ((password[5]) + (password[6]))))) ^ ((array_2[6] + (array_1[6] * (password[7] ^ password[6]))) ^ 245))))
s.add(792390 == (61 * ((139 + (array_2[7] * (array_1[7] ^ ((password[6]) + (password[7]))))) ^ ((array_2[7] + (array_1[7] * (password[8] ^ password[7]))) ^ 49))))
s.add(55890 == (243 * ((182 + (array_2[0] * (array_1[0] ^ ((password[7]) + (password[8]))))) ^ ((array_2[0] + (array_1[0] * (password[9] ^ password[8]))) ^ 72))))
s.add(468292 == (44 * ((152 + (array_2[1] * (array_1[1] ^ ((password[8]) + (password[9]))))) ^ ((array_2[1] + (array_1[1] * (password[10] ^ password[9]))) ^ 239))))
s.add(4570092 == (222 * ((128 + (array_2[2] * (array_1[2] ^ ((password[9]) + (password[10]))))) ^ ((array_2[2] + (array_1[2] * (password[11] ^ password[10]))) ^ 121))))
s.add(4415362 == (226 * ((209 + (array_2[3] * (array_1[3] ^ ((password[10]) + (password[11]))))) ^ ((array_2[3] + (array_1[3] * (password[12] ^ password[11]))) ^ 32))))
s.add(4538278 == (122 * ((209 + (array_2[4] * (array_1[4] ^ ((password[11]) + (password[12]))))) ^ ((array_2[4] + (array_1[4] * (password[13] ^ password[12]))) ^ 222))))
s.add(209304 == (24 * ((39 + (array_2[5] * (array_1[5] ^ ((password[12]) + (password[13]))))) ^ ((array_2[5] + (array_1[5] * (password[14] ^ password[13]))) ^ 34))))
s.add(1588748 == (161 * ((235 + (array_2[6] * (array_1[6] ^ ((password[13]) + (password[14]))))) ^ ((array_2[6] + (array_1[6] * (password[15] ^ password[14]))) ^ 69))))
s.add(3339440 == (208 * ((58 + (array_2[7] * (array_1[7] ^ ((password[14]) + (password[15]))))) ^ ((array_2[7] + (array_1[7] * (password[16] ^ password[15]))) ^ 49))))
s.add(952128 == (72 * ((214 + (array_2[0] * (array_1[0] ^ ((password[15]) + (password[16]))))) ^ ((array_2[0] + (array_1[0] * (password[17] ^ password[16]))) ^ 118))))
s.add(2922543 == (117 * ((19 + (array_2[1] * (array_1[1] ^ ((password[16]) + (password[17]))))) ^ ((array_2[1] + (array_1[1] * (password[18] ^ password[17]))) ^ 252))))
s.add(312864 == (16 * ((249 + (array_2[2] * (array_1[2] ^ ((password[17]) + (password[18]))))) ^ ((array_2[2] + (array_1[2] * (password[19] ^ password[18]))) ^ 134))))
s.add(929380 == (31 * ((191 + (array_2[3] * (array_1[3] ^ ((password[18]) + (password[19]))))) ^ ((array_2[3] + (array_1[3] * (password[20] ^ password[19]))) ^ 63))))
s.add(8851407 == (197 * ((156 + (array_2[4] * (array_1[4] ^ ((password[19]) + (password[20]))))) ^ ((array_2[4] + (array_1[4] * (password[21] ^ password[20]))) ^ 109))))
s.add(1846515 == (155 * ((125 + (array_2[5] * (array_1[5] ^ ((password[20]) + (password[21]))))) ^ ((array_2[5] + (array_1[5] * (password[22] ^ password[21]))) ^ 28))))
s.add(2953720 == (220 * ((33 + (array_2[6] * (array_1[6] ^ ((password[21]) + (password[22]))))) ^ ((array_2[6] + (array_1[6] * (password[23] ^ password[22]))) ^ 253))))
s.add(3463992 == (237 * ((205 + (array_2[7] * (array_1[7] ^ ((password[22]) + (password[23]))))) ^ ((array_2[7] + (array_1[7] * (password[24] ^ password[23]))) ^ 207))))
s.add(1280928 == (44 * ((101 + (array_2[0] * (array_1[0] ^ ((password[23]) + (password[24]))))) ^ ((array_2[0] + (array_1[0] * (password[25] ^ password[24]))) ^ 249))))
s.add(127560 == (30 * ((5 + (array_2[1] * (array_1[1] ^ ((password[24]) + (password[25]))))) ^ ((array_2[1] + (array_1[1] * (password[26] ^ password[25]))) ^ 159))))
s.add(197301 == (13 * ((208 + (array_2[2] * (array_1[2] ^ ((password[25]) + (password[26]))))) ^ ((array_2[2] + (array_1[2] * (password[27] ^ password[26]))) ^ 163))))
s.add(386910 == (18 * ((36 + (array_2[3] * (array_1[3] ^ ((password[26]) + (password[27]))))) ^ ((array_2[3] + (array_1[3] * (password[28] ^ password[27]))) ^ 227))))
s.add(114738 == (39 * ((226 + (array_2[4] * (array_1[4] ^ ((password[27]) + (password[28]))))) ^ ((array_2[4] + (array_1[4] * (password[29] ^ password[28]))) ^ 64))))
s.add(742775 == (55 * ((23 + (array_2[5] * (array_1[5] ^ ((password[28]) + (password[29]))))) ^ ((array_2[5] + (array_1[5] * (password[30] ^ password[29]))) ^ 158))))
s.add(501690 == (42 * ((17 + (array_2[6] * (array_1[6] ^ ((password[29]) + (password[30]))))) ^ ((array_2[6] + (array_1[6] * (password[31] ^ password[30]))) ^ 206))))
s.add(4778284 == (196 * ((78 + (array_2[7] * (array_1[7] ^ ((password[30]) + (password[31]))))) ^ ((array_2[7] + (array_1[7] * (password[32] ^ password[31]))) ^ 59))))
s.add(272085 == (55 * ((11 + (array_2[0] * (array_1[0] ^ ((password[31]) + (password[32]))))) ^ ((array_2[0] + (array_1[0] * (password[33] ^ password[32]))) ^ 96))))
s.add(1371072 == (192 * ((79 + (array_2[1] * (array_1[1] ^ ((password[32]) + (password[33]))))) ^ ((array_2[1] + (array_1[1] * (password[34] ^ password[33]))) ^ 122))))
s.add(2206236 == (148 * ((32 + (array_2[2] * (array_1[2] ^ ((password[33]) + (password[34]))))) ^ ((array_2[2] + (array_1[2] * (password[35] ^ password[34]))) ^ 236))))
s.add(4155088 == (161 * ((215 + (array_2[3] * (array_1[3] ^ ((password[34]) + (password[35]))))) ^ ((array_2[3] + (array_1[3] * (password[36] ^ password[35]))) ^ 123))))
s.add(11333348 == (247 * ((90 + (array_2[4] * (array_1[4] ^ ((password[35]) + (password[36]))))) ^ ((array_2[4] + (array_1[4] * (password[37] ^ password[36]))) ^ 182))))
s.add(2257580 == (130 * ((116 + (array_2[5] * (array_1[5] ^ ((password[36]) + (password[37]))))) ^ ((array_2[5] + (array_1[5] * (password[0] ^ password[37]))) ^ 182))))

if s.check() == sat:
    m = s.model()
    sol = ''.join([chr(m[password[i]].as_long()) for i in range(38)])
    print("Password:", sol) # wwf{m45h1r0_w41fu_>_<_50_cu73~~_4hw4_}
else:
    print("No solution found.")
```

### Conclusion
All in all, this was a fun challenge, a pretty standard VM rev. Initially, my solution didn't work because I had initialized the ``password`` variable with ``BitVec("c_{}".format(i), 8)``, which represents an 8-bit vector. However, changing it to ``BitVec("c_{}".format(i), 32)`` (a 32-bit vector) resolved the issue. This is a something I encounter frequently, but I always seem to forget about it.