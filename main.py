# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

item1 = "11:06 PM"
print(item1[0:2])
print(item1[3:5])

k1 = int(item1[0:2])
k2 = int(item1[3:5])
print(type(k1),type(k2))
print(k1+k2)

item2 = "2:02"
print(item2[0:1])
print(item2[2:4])


#def add_time(start, duration, day=""):
  #time1 = int(start)
  #time2 = int(duration)
  #new_time = time1 + time2


  #return new_time



print(add_time("11:06 PM", "2:02"))
print(add_time("12:15 AM", "446:06"))
print(add_time("19:15 AM", "6:06"))


# Run unit tests automatically
main(module='test_module', exit=False)