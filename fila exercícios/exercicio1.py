#https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

from collections import deque
import threading
import time

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
    
food_order_queue = Queue()

def place_orders(orders):
    for o in orders:
        food_order_queue.enqueue(o)
        print(f"Placing order {o}")
        time.sleep(0.5)
        
def serve_orders():
    time.sleep(1)
    while food_order_queue.size() > 0:
        order = food_order_queue.dequeue()
        print(f"Serving {order}")
        time.sleep(0.5)
        
if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()