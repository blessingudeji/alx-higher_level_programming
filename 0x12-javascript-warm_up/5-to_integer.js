#!/usr/bin/node

const [, , arg] = process.argv;

const checkInt = parseInt(arg);
if (!isNaN(checkInt)) {
  console.log(`My number: ${checkInt}`);
} else {
  console.log('Not a number');
}
