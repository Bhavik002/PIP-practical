#20CS002 Bhavik Ambasana
#creating a tuple
bhavik = (7, 1, 0, 55, 33, 17)
print(bhavik)
#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
bhavik =bhavik + (94,)
print(bhavik)
#adding items in a specific index
bhavik= bhavik[:5] + (25, 2, 56) + bhavik[:5]
print(bhavik)
#converting the tuple to list
listx = list(bhavik)
#use different ways to add items in list
listx.append(30)
bhavik = tuple(listx)
print(bhavik)