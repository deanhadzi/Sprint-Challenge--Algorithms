#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) In this first case the runtime complexity is polynomial. The running time is proportional to n squared.
If the n doubled, the same would happen with runtime. Caluclated as a + n^2, then drop all the constants.
Answer is O(n^c)


b) The second case gives the logarithmic runtime complexity. The running time is proportional to the number of times
the n can be divided by 2 (as this is the rate at which j is being incremented). Answer is O(log n)


c) This algorithm is an example of the linear time as we saw with most of the recursion problems that only have one recursion call.
This is very inefficient solution with larger inputs and will require memoization to make it more useful. Answer is O(n)

## Exercise II

This would be an ideal candidate for a binary search. Floor are ordered set where each next floor is one higher from the previous. First egg would be
thrown from the middle floor (n/2). If the egg breaks, we would move to the lower section of the building, but now move to n/4 - floor and throw it again. If the eggs doesn't break, we would find the next middle point between n/4 and n/2 and repeat again. Each next throw would cut the floor range in half until we can pricessly find the floor from which the egg would be broken. 

Binary search has a best case scenario of runtime complexity of O(1) - if we hit the correct floor on the first go. The average runtime complexity of binary search is O(log n).
