// Give a function 'fn' and a time in milliseconds. You need to return a debounced version of that function.

const debounce = (mainFunction, delay) => {
    // Declare a variable to store the timer ID.
    let timerID;

    // Returns an anonymous function that takes in any number of arguments and returns a debounced version of the 'mainFunction'.
    return function(...args) {
        // Clear the previous timer to prevent the execution of 'mainFunction'
        clearTimeout(timerID);

        // Set a new timer that will execute the 'mainFunction' after the specified delay.
        timerID = setTimeout(() => {
            mainFunction(...args);
        }, delay)
    }
}

let startTime = Date.now();

const fetchData = () => {
    console.log(`fetchData called after ${Date.now() - startTime}ms`);
}

const debouncedFn = debounce(fetchData, 50);

// Input 1
setTimeout(debouncedFn, 30);
setTimeout(debouncedFn, 40);

// Input 1
setTimeout(debouncedFn, 30);
setTimeout(debouncedFn, 40);
setTimeout(debouncedFn, 100);
setTimeout(debouncedFn, 160);
setTimeout(debouncedFn, 170);