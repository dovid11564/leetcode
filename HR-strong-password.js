//https://www.hackerrank.com/challenges/strong-password/problem
//my submisssion: https://www.hackerrank.com/challenges/strong-password/submissions/code/337577093
'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */

function minimumNumber(n, password) {
    const numbers = "0123456789"
    const lower_case = "abcdefghijklmnopqrstuvwxyz"
    const upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const special_characters = "!@#$%^&*()-+"
    //not going to do this now, worth revisiting later, could the following checkers be better stored as an array or obj?
    let numChecker = 0;
    let lowChecker = 0;
    let uppChecker = 0;
    let speChecker = 0;
    for (let i = 0; i < password.length; i++) {
        if (numbers.includes(password[i])) {
            numChecker++
        } else if (lower_case.includes(password[i])) {
            lowChecker++
        } else if (upper_case.includes(password[i])) {
            uppChecker++
        } else if (special_characters.includes(password[i])) {
            speChecker++
        }
    }
    if (n > 6 && numChecker === 0 && lowChecker === 0 && uppChecker === 0 && speChecker === 0) {
        return 0;
    } else if (n > 6) {
        const zeroes = [numChecker, lowChecker, uppChecker, speChecker].filter(checker => checker === 0);
        return zeroes.length;
    } else if (n < 6 && numChecker === 0 && lowChecker === 0 && uppChecker === 0 && speChecker === 0) {
        return 6 - n;
    } else if (n < 6) {
        const zeroes = [numChecker, lowChecker, uppChecker, speChecker].filter(checker => checker === 0);
        return Math.max(zeroes.length, 6 - n);
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const password = readLine();

    const answer = minimumNumber(n, password);

    ws.write(answer + '\n');

    ws.end();
}
