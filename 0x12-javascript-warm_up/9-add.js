#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const [, , args1, args2] = process.argv;
const num1 = parseInt(args1);
const num2 = parseInt(args2);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
