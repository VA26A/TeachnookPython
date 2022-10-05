#list

thislist = ["Apple","Banana","Peaches"]
print(thislist)

print(thislist[0])

thislist[0] = "Pineapple"

print(thislist)

for x in thislist:
    print(x)

if "Pineapple" in thislist:
    print("Yes it is present")
else: 
    print("No")

print(len(thislist))

thislist.append("Guava")

print(thislist)

thislist.insert(1,"Grappes")

print(thislist)

del thislist[0]

print(thislist)

thislist.remove("Grappes")
print(thislist)

thislist.pop()
print(thislist)

thislist.clear()
print(thislist)

thislist = list(("Apple","Banana"))
print(thislist)