#!/usr/bin/node

const [, , ...args] = process.argv.map(Number);
const list = [...new Set(args)];

if (list.length <= 1) {
  console.log(0);
} else {
  const sortedIntegers = list.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
