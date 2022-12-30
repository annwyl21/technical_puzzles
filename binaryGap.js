function solution(n) {
    let binS = n.toString(2);
    let count = 0;
    let largestCount = 0;
    for (let x = 0; x < binS.length; x++) {
        if (binS[x] === "0") {
            count ++;
        } else if (binS[x] === "1") {
            if (count > largestCount) {
            largestCount = count;
            count = 0
            }
        }
    }
    return "n " + n + ", binary " + binS + ", binary gap " + largestCount
}

console.log(solution(5243));