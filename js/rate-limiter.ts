class RateLimiter {
    private limit: number;
    private windowSize: number;
    private requests: Map<string, number[]>;

    constructor(limit: number, windowSize: number) {
        this.limit = limit;
        this.windowSize = windowSize;
        this.requests = new Map()
    }

    allowRequest(userId: string): boolean {
        const now = Date.now();

        if(!this.requests.has(userId)) {
            this.requests.set(userId, [now]);
        }

        const timestamps: number[] = this.requests.get(userId) || [];

        while(timestamps.length > 0 && timestamps[0] < now - this.windowSize) {
            timestamps.shift();

        }

        if(timestamps.length >= this.limit) { 
            return false;
        }

        timestamps?.push(now)
        return true;
    }   
}

function testRateLimiter() {
    const rateLimiter = new RateLimiter(3, 1000); // allow 3 requests per 1000ms (1 second)
    const userId = 'testUser';
    let passCount = 0, blockCount = 0;

    // Send 3 immediate requests - should all be allowed
    for (let i = 0; i < 3; i++) {
        if (rateLimiter.allowRequest(userId)) {
            passCount++;
            console.log(`Request ${i + 1}: allowed`);
        } else {
            blockCount++;
            console.log(`Request ${i + 1}: blocked`);
        }
    }

    // 4th request within the window should be blocked
    if (!rateLimiter.allowRequest(userId)) {
        blockCount++;
        console.log("Request 4: correctly blocked due to rate limit.");
    } else {
        passCount++;
        console.log("Request 4: incorrectly allowed.");
    }

    // Wait for 1 second to reset window
    setTimeout(() => {
        if (rateLimiter.allowRequest(userId)) {
            passCount++;
            console.log("Request after window: allowed as expected.");
        } else {
            blockCount++;
            console.log("Request after window: unexpectedly blocked.");
        }
        console.log(`Test Results: Allowed=${passCount}, Blocked=${blockCount}`);
    }, 1100);
}

testRateLimiter();