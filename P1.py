#tuple

thistuple = ("Apple","Banana","Peaches")
print(thistuple)

print(thistuple[0])



for x in thistuple:
    print(x)

if "Pineapple" in thistuple:
    print("Yes it is present")
else: 
    print("No")

print(len(thistuple))

thistuple.append("Guava")

print(thistuple)

thistuple.insert(1,"Grappes")

print(thistuple)

del thistuple[0]

print(thistuple)

thistuple.remove("Grappes")
print(thistuple)

thistuple.pop()
print(thistuple)

thistuple.clear()
print(thistuple)

thistuple = tuple(("Apple","Banana"))
print(thistuple)