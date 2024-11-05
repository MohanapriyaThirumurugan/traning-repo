




















# list

# how to add in List
#syntax -------> variblename =[]

Au=["AUKBC",True,45, 56]
kbc=[3,5,7,8]

# how to find length in list
print(len(Au))  # len is a keyword

# how add one element in length 
Au.append("hellomohana") 
print(Au)

# how to insert in list
Au.insert(2,"mohana")
print(Au)

# how to modify the value 
Au[0]=78
print(Au)
 
# how to remove elemrnt in a list

Au.pop(3)
print(Au) 

# merge to array

Au.extend(kbc)
print("non reverse order :",Au)

kbc.extend(Au)
print("reverse order :",kbc)

# how to get the input values from user
 
 # here i while loop is perfect exmaple 

def hellolist():
    Au1 = []  # Initialize an empty list
    
    # Loop to get user input
    while True:
        userinput = input("Enter the list value or 'stop': ")
        
        if userinput.lower() == 'stop':  # Stop the loop if the user types 'stop'
            break
        
        Au1.append(userinput)  # Add the user input to the list
    
    print("Your final list:", Au1)

# Call the function
# hellolist()



# tuples
# A tuple is a collection which is ordered and unchangeable.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Since tuples are indexed, they can have items with the same value:

tupleex=("apple","mango","orange")
print(tupleex)

# now i can  change tuple to list 
listex=list(tupleex)

print(listex)

# join tupless
tupleex2=(7,8)
c=tupleex+tupleex2
print(c)

# sets

# here we can modify ,add, pop

setex={1,2,3}

# add element
setex.add(4)
print(setex)

# it does not accept the duplicate values
setex.add(3)
print(setex)

# modify the values
setex.add("mohana")
print("remove methods :",setex)

#remove 
setex.remove(1)
print("remove methods :",setex)
# merge two set 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
  
thisset.update(mylist)

print(thisset)

# types of set 
# union
# The union() method returns a new set with all items from both sets.
# and also use | this for also union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print("union means combaines:",set3)

#ou can use the - operator instead of the difference() method, and you will get the same result.

#Example
#Use - to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)


# dictionaries
# Dictionaries cannot have two items with the same key:

dic={
    "name":"mohana",
    "age":22,
    "location":"karapakkam"
}

# how to accese
print(dic)
# how to accesses one key
print(dic["name"])
# how to print all keys
print(dic.keys())
# how to print all values
print(dic.values())




