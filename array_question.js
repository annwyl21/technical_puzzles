// Codility Puzzle - Cyclic Rotation
// rotate an array right by a specified number of places

function solution (A, K) {
    for (let x = 0; x < K; x++) {
        lastItem = A.pop()
        A.unshift(lastItem)
    }
    
    return A
}

console.log(solution([1,2,3,4,5], (3)))

// Solution creates a loop that
// saves the final item in the array as a variable
// then adds that item back onto the start of the array
// looping through this action for the specified number of times

// Challenges...
// This does not score 100% on coditlity, failing on the 'extreme_empty' test ???