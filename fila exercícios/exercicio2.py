# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, val):
        return self.queue.appendleft(val)
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("The queue is empty")
            return
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def first(self):
        return self.queue[-1]

def binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")
    
    for item in range(n):
        first = numbers_queue.first()
        print(first)
        numbers_queue.enqueue(first + "0")
        numbers_queue.enqueue(first + "1")
        numbers_queue.dequeue()
        
if __name__ == '__main__':
    binary_numbers(14)       