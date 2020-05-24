
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        #Creates an empty Queue with a specified capacity
        self.capacity = capacity
        self.items = [None]*capacity
        self.head=0               #First item in, first item ready to go out
        self.num_items=0          #Count of the total values in the Queue
        self.tail=self.capacity-1 #Last item in, last item ready to go out


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full(): 
          raise IndexError("queue is full")#Raises IndexError when Queue is full
        if self.tail+1 == self.capacity:#rotates the tail index of the array circularly and starts over at index of 0 when the capacity is reached
          self.tail = 0
        else:
          self.tail = self.tail+1
        self.items[self.tail] = item
        self.num_items = self.num_items+1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
          raise IndexError("queue is empty")#Raises IndexError when Queue is empty
        temp = self.items[self.head]
        if self.head+1 == self.capacity:#rotates the head index of the array circularly and starts over at index of 0 when the capacity is reached
          self.head = 0
        else:
          self.head = self.head+1
        self.num_items = self.num_items-1
        return temp

        


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items

    def get_head(self):
        return self.items[self.head]

    def get_tail(self):
        return self.items[self.tail]



