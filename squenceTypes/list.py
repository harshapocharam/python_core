# A sequence is a ordered collection of items.
# that can be refered using Indexing
# string are immutable and List are mutable ( we can change content)

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

print("*****")

# interate using for loop in computer_parts list
# [] used in indexing sequence and list
for part in computer_parts:
  print(part)
  
print("*****")
# identifying using indexing item 
print(computer_parts[2])

# slice alist
print(computer_parts[0:3])
print(computer_parts[:2])
print(computer_parts[3:])
print(computer_parts[-1])



