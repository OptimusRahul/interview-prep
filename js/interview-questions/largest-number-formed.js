/*
<div class="dark:text-brand-card-title dark:text-opacity-80 text-brand-light-heading font-maven tracking-wider leading-6 text-sm"><div class="markdown-container"><p>Write a function that arranges a list of <strong>non-negative integers</strong> to form the <strong>largest possible number</strong>.
Given an array of integers, rearrange them such that when concatenated, they produce the <strong>maximum possible numeric value</strong>.</p>
<h3>Input</h3>
<ul>
<li>An array <code>arr</code> of non-negative integers.</li>
</ul>
<h3>Output</h3>
<ul>
<li>A <strong>string</strong> representing the <strong>largest number</strong> that can be formed by arranging the given integers.</li>
</ul>
<h3>Constraints &amp; Edge Cases</h3>
<ul>
<li>
<p>All integers in the array are <strong>non-negative</strong>.</p>
</li>
<li>
<p>The resulting number may be <strong>very large</strong>, so return it as a <strong>string</strong>.</p>
</li>
<li>
<p>If <strong>all numbers are 0</strong>, return <code>"0"</code> (not <code>"000"</code>).</p>
</li>
<li>
<p>The array may contain <strong>duplicate numbers</strong>.</p>
</li>
<li>
<p>When comparing numbers for arrangement, treat them as strings:</p>
<ul>
<li>
<p>For example, <code>"30"</code> should come <strong>after</strong> <code>"3"</code> because:</p>
<ul>
<li><code>"330"</code> &gt; <code>"303"</code> → so <code>"3"</code> should come before <code>"30"</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><div style="color: rgb(212, 212, 212); font-size: 13px; text-shadow: none; font-family: Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.5; tab-size: 4; hyphens: none; padding: 1em; margin: 0.5em 0px; overflow: auto; background: rgb(30, 30, 30);"><code class="language-js" style="white-space: pre; color: rgb(212, 212, 212); font-size: 13px; text-shadow: none; font-family: Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace; direction: ltr; text-align: left; word-spacing: normal; word-break: normal; line-height: 1.5; tab-size: 4; hyphens: none;"><span class="token" style="color: rgb(106, 153, 85);">//Example 1:</span><span>
</span>
<span></span><span class="token literal-property" style="color: rgb(156, 220, 254);">Input</span><span class="token" style="color: rgb(212, 212, 212);">:</span><span>
</span><span></span><span class="token" style="color: rgb(86, 156, 214);">const</span><span> arr </span><span class="token" style="color: rgb(212, 212, 212);">=</span><span> </span><span class="token" style="color: rgb(212, 212, 212);">[</span><span class="token" style="color: rgb(181, 206, 168);">3</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">30</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">34</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">5</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">9</span><span class="token" style="color: rgb(212, 212, 212);">]</span><span> 
</span>
<span></span><span class="token literal-property" style="color: rgb(156, 220, 254);">output</span><span class="token" style="color: rgb(212, 212, 212);">:</span><span> </span><span class="token" style="color: rgb(206, 145, 120);">"9534330"</span><span>
</span>
<span></span><span class="token" style="color: rgb(106, 153, 85);">//Example 2:</span><span>
</span>
<span></span><span class="token literal-property" style="color: rgb(156, 220, 254);">Input</span><span class="token" style="color: rgb(212, 212, 212);">:</span><span>
</span><span></span><span class="token" style="color: rgb(86, 156, 214);">const</span><span> arr3 </span><span class="token" style="color: rgb(212, 212, 212);">=</span><span> </span><span class="token" style="color: rgb(212, 212, 212);">[</span><span class="token" style="color: rgb(181, 206, 168);">54</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">546</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">548</span><span class="token" style="color: rgb(212, 212, 212);">,</span><span> </span><span class="token" style="color: rgb(181, 206, 168);">60</span><span class="token" style="color: rgb(212, 212, 212);">]</span><span> 
</span>
<span></span><span class="token literal-property" style="color: rgb(156, 220, 254);">output</span><span class="token" style="color: rgb(212, 212, 212);">:</span><span> </span><span class="token" style="color: rgb(206, 145, 120);">"6054854654"</span></code></div></pre></div></div>
*/

function formLargestNumber(arr) {
    const nums = arr.map(num => num.toString());
    
    console.log('Before Sorting : ', nums)
    
    nums.sort((a,b) => {
        console.log(`${a} - ${b} - ${b+a} - ${a+b} - ${(b+a).localeCompare(a+b)}`);
        // return (b+a).localeCompare(a+b)
        return a + b > b + a ? -1 : 1;
    })
    
    console.log('After Sorting : ', nums)
    
    if(nums[0] === '0') {
        return '0';
    }
    
    return nums.join('')
}

const input = [3, 30, 34, 5, 9];
console.log(formLargestNumber(input));