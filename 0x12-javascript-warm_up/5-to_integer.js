#!/usr/bin/node

const one = 'Not a number';

const args = process.argv[2];

if (isNaN(parseInt(+args))) {
  console.log(one);
} else {
  console.log('My number: ' + parseInt(+args));
}
