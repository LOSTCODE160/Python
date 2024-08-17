# i=30
# if(i>=52):
#     print("You have reached the end of the deck")
# else:
#     print("systum")

# i=30
# if(i==30):
#     if (i<35):
#         print("i is smaller")
#     if(i<40):
#         print("i is smaller too")
        

import sys

# sample Tuples
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

# print the sizes of sample Tuples
print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")


