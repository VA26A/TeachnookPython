#sets

thisset = {"Apple","Banana","Peaches"}
print(thisset)

for x in thisset:
    print(x)

thisset.add("orange")
print(thisset)

thisset.update(["well","reality"])
print(thisset)

print(len(thisset))

thisset.remove("reality")
print(thisset)

thisset.discard("well")
thisset.pop()

print(thisset)