#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const args = process.argv.slice(2);

if (args.length !== 2 || isNaN(parseInt(args[0])) || isNaN(parseInt(args[1]))) {
  console.log('NaN');
} else {
  const result = add(args[0], args[1]);
  console.log(result);
}
