# Mutable objects where value changed
# python has build in mutable Objects list, dict, set, bytearry
# we can change value of Object without object being destroyed & recreated.


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list)) # output: 4332194176 here they refr to same value

shopping_list+=["cookies"]
print(shopping_list) #output: 4332194176 here the refr value is allways same even thow value got update on list

# Here we are able to add new values in list with out creating new list
# An immutable obj can't be chagned. you create new obj and use same variable name for it, but you can not change the value of an immutable object.
# Mutable object, suchas lists, can be changed. 

a = b = c = d = e = f = another_list

print(a)
print("Adding cream")

b.append("cream")
print(c)
print(f)
print(d) # cream is updated on all c,f,d on same list 
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
# Adding cream
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']
# ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']

# Sequence Operators


# Iterating over list
for parts in shopping_list:
    print(parts)
    
valid_choice =[str(i) for i in range(1, len(shopping_list) +1)]
print(valid_choice)