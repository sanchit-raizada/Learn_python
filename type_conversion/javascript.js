let user ='Helo world'
let input = 342424;
console.log(input+user) //342424Helo world

let input2 = true;
console.log(input2 + user) //trueHelo world

let input3 = null;
console.log(input3 + user) //nullHelo world

let input4 = undefined;
console.log(input4 + user) //undefinedHelo world

let input5 = Symbol("sanchit");
console.log(input5 + user) //TypeError: can't convert symbol to string  

let input6 = BigInt(123456789012345678901234567890);
console.log(input6 + user) //TypeError: can't convert BigInt to string

