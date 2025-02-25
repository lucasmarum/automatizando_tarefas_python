import copy
spam = ['a','b','c','d']
cheese = copy.copy(spam)
cheese[1] = 42
print("esse é o spam: " + str(spam))
print("esse é o cheese: " + str(cheese))
