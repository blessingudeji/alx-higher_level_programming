#!/usr/bin/node

const [, , argument] = process.argv;

if (!argument) {
  console.log('No argument');
} else {
  console.log(argument);
}
