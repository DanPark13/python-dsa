from hashSet import HashSet

# Test Hash Set
myHashSet = HashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))
print(myHashSet)