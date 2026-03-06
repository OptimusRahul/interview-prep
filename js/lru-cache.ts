class Node {
    key: number;
    value: number;
    prev: Node | null = null;
    next: Node | null = null

    constructor(key: number, value: number) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    private capacity: number;
    private cache: Map<number, Node>;
    private head: Node
    private tail: Node

    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map();
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    get(key: number): number {
        if(this.cache.has(key)) {
            const node = this.cache.get(key)!;
            this.remove(node);
            this.insert(node);
            return node.value;
        }
        return -1;
    }
    
    put(key: number, value: number): void {
        if(this.cache.has(key)) {
            this.remove(this.cache.get(key));
        }
        const newNode = new Node(key, value);
        this.insert(newNode);
        this.cache.set(key, newNode);
    }
    
    private remove(node: Node): void {
        this.cache.delete(node.key);
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    private insert(node: Node): void {
        this.cache.set(node.key, node);
        node.next = this.head.next;
        node.next.prev = node;
        node.prev = this.head;
        this.head.next = node;
    }
}

const lruCache = new LRUCache(2);
lruCache.put(1, 1);
lruCache.put(2, 2);
console.log(lruCache.get(1));
lruCache.put(3, 3);
console.log(lruCache.get(2));
lruCache.put(4, 4);
console.log(lruCache.get(1));
console.log(lruCache.get(3));
console.log(lruCache.get(4));


const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
})

rl.on('line', (line) => {
    console.log(line);
})