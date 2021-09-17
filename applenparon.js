const readline = require('readline'),


  compare = (a, p) => {
    [a, p] = [a * 7, p * 13];
    const diff = a - p;

    if (a > p) console.log('Axel')
    else if (a < p) console.log('Petra')
    else console.log('Lika')
  },

  rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

rl.on('line', (line) => {
  var nums = line.split(' ');
  var a = parseInt(nums[0]);
  var b = parseInt(nums[1]);

  compare(a, b)
});