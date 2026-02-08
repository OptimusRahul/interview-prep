/*
LeetCode 1675 - Minimize Deviation in Array (Hard)
https://leetcode.com/problems/minimize-deviation-in-array/

Problem: Given an array of positive integers, minimize the "deviation" 
(difference between max and min) using these operations any number of times:
- If a number is odd, multiply it by 2
- If a number is even, divide it by 2

Input : [1, 2, 3, 4]
Output : 1

Approach:
1. Odd numbers can only increase (×2 once), even numbers can only decrease (÷2)
2. Normalize all odds by ×2 (their max possible value)
3. Greedily reduce the max until it becomes odd

Time: O(n * log(max) * log(n))  |  Space: O(n)
*/

// function minimumDeviation(nums) {
//     console.log("Input:", nums);
    
//     // Step 1: Normalize - multiply odd numbers by 2
//     let arr = nums.map(n => n % 2 ? n * 2 : n);
//     arr.sort((a, b) => b - a); // descending order
    
//     let minVal = Math.min(...arr);
//     let minDev = arr[0] - minVal;
    
//     console.log("After normalizing odds:", arr);
//     console.log(`Initial: max=${arr[0]}, min=${minVal}, deviation=${minDev}`);
    
//     // Step 2: Keep reducing max while it's even
//     while (arr[0] % 2 === 0) {
//         arr[0] = arr[0] / 2;
//         minVal = Math.min(minVal, arr[0]);
//         arr.sort((a, b) => b - a); // re-sort
//         minDev = Math.min(minDev, arr[0] - minVal);
//         console.log(`Divided: arr=${arr}, max=${arr[0]}, min=${minVal}, deviation=${minDev}`);
//     }
    
//     console.log("Result:", minDev, "\n");
//     return minDev;
// }

function minimumDeviation(input) {
    const length = input.length;
    smallest = input[0], largest = input[length - 1];

    while (largest > smallest) {
        if (largest % 2 === 0) {
    }

}

// Test cases
console.log(minimumDeviation([1, 2, 3, 4])); // Output: 1
// console.log(minimumDeviation([4, 1, 5, 20, 3])); // Output: 3
// console.log(minimumDeviation([2, 10, 8])); // Output: 3