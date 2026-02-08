// Given a function 'fn' and a time 't' in milliseconds. You need to return a throttled version of that function.

const throttle = (mainFunction, delay) => {
    let timerID = null;
    return (...args) => {
        if(timerID === null) {
            mainFunction(...args);

            timerID = setTimeout(() => {
                timerID = null;
            }, delay)
        }
    }
}

let startTime = Date.now();

const handleMouseMove = (e) => {
    console.log(`mousemove throttled @ ${Date.now() - startTime}ms | x=${e.clientX}, y=${e.clientY}`);
}

const throttledFn = throttle(handleMouseMove, 50);

const moveTarget = document.getElementById('moveBox') ?? document;
moveTarget.addEventListener('mousemove', throttledFn);