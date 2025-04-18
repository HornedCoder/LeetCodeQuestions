'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle.
By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
'''

from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskFrequency = Counter(tasks)
        time = 0
        maxHeap = []
        for i in taskFrequency.values():
            maxHeap.append(-1*i)

        heapq.heapify(maxHeap)
        cooling = [] # Stores ([taskFrequency count, cooling Time])

        # Process until all tasks are done.
        while maxHeap or cooling:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1 # +1 because we are using -ves.
                # If there are instances of this task left , put it in cooling
                if count < 0:
                    cooling.append([count, time+n]) # Will be available after cooling time
            
            # Check if any tasks has finished cooling.
            if cooling and cooling[0][1] <= time:
                heapq.heappush(maxHeap, cooling.pop(0)[0])
        
        return time

