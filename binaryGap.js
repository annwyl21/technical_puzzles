// Codility Puzzle
// Find the binary gap

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

// Solution turns the given number into a binary string
// Sets up 2 zero'd counters to count the 0's and to store the largest count of 0's
// Loops over the string
// Adds 1 to the count of zeros 
// or stores replaces the largest count of 0's if the new count is bigger than the stored value
// returns the initial number, that umber in binary and the binary gap

// Challenges overcome - Type Issues
// when comparing the value in the string to the value in the if statement
// once the number is converted to a string the value is no longer a 'number' and must be compared to
// 'a thing in a string' using "" 