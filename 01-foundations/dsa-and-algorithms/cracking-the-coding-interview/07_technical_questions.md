# VII. Technical Questions

## How to prepare

* Try to solve the problem on your own
* Write the code on paper
* Test the code - on paper
* Type the paper code as-is into a computer

## What you need to know

* Core Data Structures, Algorithms, and Concepts

| Data Structures | Algorithms | Concepts | 
| --------------- | ---------  | -------- |
| Linked Lists | Breadth-First Search | Bit Manipulation |
| Trees, Tries, &Graphs | Depth-First Search | Memory (Stack vs. Heap) | 
| Stacks & Queues | Binary Search | Recursion |
| Heaps | Merge Sort | Dynamica Programming |
| Vectors/ArrayLists | Quick Sort | Big O Time & Space |
| Hash Tables | | | 

## Walking Through a problem

### Listen

* Listen carefully to the problem, and be sure that you've mentally recorded any unique information in the problem.

### Draw an Example

* An example can dramatically improve someone's ability to solve an interview question, and yet so many candi­dates just try to solve the question in their heads.

### State a Brute Force

* Some candidates don't state the brute force because they think it's both obvious and terrible. But here's the thing: Even if it's obvious for someone, it's not necessarily obvious for the others candidates. We don't want someone's nterviewer to think that they are struggling to see even the easy solution.

### Optimize

* Look for any unused information. Did the interviewer tell that the array was sorted? How can someone leverage that information?
* Use a fresh example. Sometimes, just seeing a different example will unclog someone's mind or help to see a pattern in the problem
* Solve it incorrectly: Just like having an inefficient solution can help you find an efficient solution, having an incorrect solution might help you find a correct solution. For example, if you're asked to generate a random value from a set such that all values are equally likely, an incorrect solution might be one that returns a semi-random value: Any value could be returned, but some are more likely than others. You can then think about why that solution isn't perfectly random. Can you rebalance the probabilities?
* Make time vs. space tradeoff. Sometimes storing extra state about the problem can help you optimize the runtime
* Precompute information. Is there a way that you can reorganize the data (sorting, etc.) or compute some values upfront that will help save time in the long run?
* Use a hash table. Hash tables are widely used in interview questions and should be at the top of your mind
* Think about the best conceivable runtime

### Walk Through

* After you've nailed down an optimal algorithm, don't just dive into coding. Take a moment to solidify your understanding of the algorithm.
* Whiteboard coding is slow-very slow. So is testing your code and fixing it. As a result, you need to make sure that you get it as close to "perfect" in the beginning as possible.

### Implement

* Start coding in the far top left corner of the whiteboard (you'll need the space). Avoid "line creep" (where each line of code is written an awkward slant). It makes your code look messy and can be very confusing when working in a whitespace-sensitive language, like Python.

### Test

* Start with a "conceptual" test. A conceptual test means just reading and analyzing what each line of code does. Think about it like you're explaining the lines of code for a code reviewer. Does the code do what you think it should do?
* Weird looking code. Double check that line of code that says x = length - 2. Investigate that for loop that starts at i = 1. While you undoubtedly did this for a reason, it's really easy to get it just slightly wrong.
* Hot spots. You've coded long enough to know what things are likely to cause problems. Base cases in recursive code. Integer division. Null nodes in binary trees. The start and end of iteration through a linked list. Double check that stuff.
* Small test cases. This is the first time we use an actual, specific test case to test the code. Don't use that nice, big 8-element array from the algorithm part. Instead, use a 3 or 4 element array. It'll likely discover the same bugs, but it will be much faster to do so.
* Special cases. Test your code against null or single element values, the extreme cases, and other special cases.

## Optimize and Solve Tecnique: Look for BUD

* Bottlenecks
* Unnecessary working
* Duplicated work
