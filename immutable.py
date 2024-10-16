# Immutable Objects - can't be changed
# python built in types are int, float, bool, str, tuple, frozenset, bytes

result = True
another_result = result
print(id(result))
print(id(another_result)) #output: 4403187096 ( refr to same location )

result = "Correct"
another_result = result
print(id(result))
print(id(another_result)) #output: 4340209664 ( refr to same location )
