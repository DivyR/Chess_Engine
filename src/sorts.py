def InsertSort(array, data):  # sort moves to allow for BinarySearching
   if type(data) != list:
      array += [data]
   elif data != []:
      array += [data[0]]
      InsertSort(array, data[1::])
   for i in range(len(array) - 1, 0, -1):
      swap_flag = False
      for j in range(i, len(array) - i - 1, -1):
         if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def InsertSortNodes(array, nodes):  # sorting evalTree nodes by score
   if type(nodes) != list:
      array += [nodes]
   elif nodes != []:
      array += [nodes[0]]
      InsertSortNodes(array, nodes[1::])
   for i in range(len(array) - 1, 0, -1):
      swap_flag = False
      for j in range(i, len(array) - i - 1, -1):
         if array[j].score < array[j - 1].score:
            array[j], array[j - 1]= array[j - 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSortNodes(array):  # sorting evalTree nodes by score
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j].bcm[1] > array[j + 1].bcm[1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSort(array):  # created incase
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swap_flag = True
      if not swap_flag:
         break
   return True

def BubbleSortPDPos(array):  # Sort pd list depending on position
   for i in range(0, len(array), 1):
      swap_flag = False
      for j in range(0, len(array) - 1 - i, 1):
         if array[j][1] > array[j + 1][1]:
            swap = list(array[j])
            swap[2] = list(array[j][2])
            array[j] = list(array[j + 1])
            array[j][2] = list(array[j + 1][2])
            array[j + 1] = list(swap)
            swap_flag = True
      if not swap_flag:
         break
   return True

def BinarySearch(array, data):  # Search for specific moves of pieces
   start, end = 0, len(array) - 1
   while start <= end:
      middle = (end + start)//2
      mid_val = array[middle]
      if mid_val == data:
         return middle
      elif mid_val < data:
         start = middle + 1
      else:
         end = middle - 1
   return -1

def BinarySearchPDPos(array, data):  # search by piece locations
   start, end = 0, len(array) - 1
   while start <= end:
      middle = (end + start)//2
      mid_val = array[middle][1]
      if mid_val == data:
         return middle
      elif mid_val < data:
         start = middle + 1
      else:
         end = middle - 1
   return -1