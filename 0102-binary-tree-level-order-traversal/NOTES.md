Walk through:
​
1. initialize queue with root
2. while queue is not empty:
3. initalize level to empty
4. iterate through queue (which would have only the root node at the first time)
5. append root.val to level
6. append left and right children to next_queue
7. go back to step 4
8. append level to result
9. queue = next_queue (refresh queue to next_queue) and go back to step 2
​
big picture: update queue to only have the nodes on each level
​