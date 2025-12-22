Counting sort starts by creating an array that stores the number of times each value appears (i.e. its frequency) between 0 and the largest observed value in the input array.

For example, given the following input array : $\textrm{A}=[5, 3, 5, 3, 1]$.

A size $k=\textrm{max}(A) + 1 = 5 + 1 = 6$ zero-filled array is created : $\textrm{C}=[0, 0, 0, 0, 0, 0]$.

Then, we traverse the array with $i=0..6$ and insert the number of times $i$ appears in $C[i]$. For example, $0$ appears $0$ times, so $C[0] = 0$.Then, $1$ appears once, so $C[1] = 1 → [0, 1, 0, 0, 0, 0]$. Continuing, we have $3$ and $5$ that appear twice each, giving $[0, 1, 0, 2, 0, 2]$.

With the frequency array $\textrm{A}$ complete, we create a new array in which we append $A[i]$ copies of $i$ by traversing it from left to right. Therefore, we store $1$ once, $3$ twice and $5$ twice also : $[1, 3, 3, 5, 5]$. This gives a size $n$ array.

The time and space complexities of counting sort are both $O(max(n+k))$.

It is possible to reduce these complexities to $O(n+k)$ where $k=\textrm{max} - \textrm{min} + 1$ by traversing the input array and adjusting the indices dynamically as $j = A[i] - \textrm{min}$.
