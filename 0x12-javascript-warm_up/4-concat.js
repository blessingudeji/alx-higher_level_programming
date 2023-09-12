#!/usr/bin/node

const [, , args1, args2] = process.argv;

const firstArg = args1 === undefined ? 'undefined' : args1;
const secondArg = args2 === undefined ? 'undefined' : args2;

console.log(`${firstArg} is ${secondArg}`);
