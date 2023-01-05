// Codility Puzzle
// Locate the value in an array that does not have a match/ pair/ snap ?

function solution(A) {
    const frequency = {};
    for (let x = 0; x < A.length; x++) {
        let element = A[x]
        if (frequency.hasOwnProperty(element)){
            frequency[element]++;
        }else{
            frequency[element] = 1;
        }; 
    }
    for (let number in frequency) {
        //console.log(number); - the key
        //console.log(frequency[number]) - the value
        div = frequency[number] %2;
        if (div != 0) {
            return number
        }
    }
}

console.log(solution([9,3,9,3,9,7,9]))

// Solution creates an empty object called 'frequency',
// loops through the given array checking if the element already exists 
// and adds novel numbers to the object and counting the frequency
// The code then looks through the object to find 
// the key associated with the value that is not an even number (that appears only once)
// and returns that key
