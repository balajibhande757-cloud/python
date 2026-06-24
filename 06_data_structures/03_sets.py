# UNORDRED MUTABLE(CHANGABLE)
s=set()          #  an empty set
print(type(s))

my_set = {1, 2, 3, 4}
print(my_set)

my_set.add(45)
print(my_set)

# my_set.clear()
# print(my_set)

# my_set.copy()
# print(my_set)

my_set.pop()
print(my_set)

my_set.remove(3)
# my_set.remove(5454)   IT THROWS AN ERROR INSTEAD OF THIS
my_set.discard(5454)
print(my_set)

setb={45,25,37,47,}
l=my_set.union(setb)
print(my_set.intersection(setb))
print(my_set.difference(setb))
print(l)