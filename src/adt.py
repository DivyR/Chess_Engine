class Queue:

   def __init__(self):
      self.store = []
   
   def put(self, data):
      self.store += [data]
      return True
   
   def get(self):
      data = self.store[0]
      self.store = self.store[1:]
      return data

class Stack:

   def __init__(self):
      self.store = []
   
   def push(self, data):
      self.store += [data]
      return True
   
   def pop(self):
      data = self.store[-1]
      self.store = self.store[:-1]
      return data
   
   def is_empty(self):
      return len(self.store) == 0