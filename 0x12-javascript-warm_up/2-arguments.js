#!/usr/bin/node
const process = require('process');
let args = process.argv;
const length = args.length;
if (length === 2) {
    console.log("No argument");
}
if (length === 3){
    console.log("Argument found");
}
if (length > 3){
    console.log("Arguments found")
}