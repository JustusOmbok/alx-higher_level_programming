#!/usr/bin/node

const n = process.argv;
const size = n.length;

function secondBiggest (n) {
  n.sort((n, m) => m - n);
  return n[1];
}

if (size < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(n.slice(2, size)));
}
