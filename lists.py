friends = ["Lisa", "Sheena", "Misha", "Zora","Veera", "Misha"]
lucky_numbers=[6, 7, 8, 13, 11, 18, 29]

#List Functions
print(friends)
print(friends[2])
print(friends[-1])
print(friends[1:4])


# friends.extend(lucky_numbers)
# print(friends)

friends.append("Bika")
print(friends)

friends.insert(1, "Pasa")
print(friends)

friends.remove("Bika")
print(friends)


# friends.clear()
# print(friends)

# friends.append("Bika")
# friends.pop()
# print(friends)


print(friends.index("Pasa"))

print(friends.count("Misha"))

friends.sort()
print(friends)


lucky_numbers.sort()
print(lucky_numbers)


lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
