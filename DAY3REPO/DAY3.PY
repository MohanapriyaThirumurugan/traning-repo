



# odd or even
# a =int(input())
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")


# multiplication table
# a= int(input("enter a value"))

# for i in range(1, 11):
#     result = a* i
#     print(result)

# factorial number

# num = int(input("Enter a number: "))


# factorial = 1


# for i in range(1, num + 1):
#     factorial *= i

# print(f"The factorial of {num} is {factorial}")

# print vowels 

# string=input()

# vowels="auios"
# count=0
# for i in string:
#     if i in vowels:
#         count+=1
#         print(count)



# Get the number from user input
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")  
# else:

#     is_prime = True
    

#     for i in range(2, num):      
#         if num % i == 0:  
#             is_prime = False  
#             break 
    
#     # Print the result
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")

# Get three numbers from user input
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# # Find the largest number
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3

# # Print the largest number
# print("The largest number is:", largest)

# Get a positive integer from user input

# number = input("Enter a positive integer: ")


# digit_sum = 0


# for digit in number:
#     digit_sum += int(digit)  


# print("The sum of the digits is:", digit_sum)

# Get the upper limit from user input
# number = int(input("Enter the upper limit (a positive integer): "))


# for i in range(1, number + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")  
#     elif i % 3 == 0:
#         print("Fizz")     
#     elif i % 5 == 0:
#         print("Buzz")      
#     else:
#         print(i)   

# Get a positive integer from user input
# number = input("Enter a positive integer: ")


# reversed_number = ""
# print(reversed_number)
# for digit in number:
#     print(digit)
#     reversed_number = digit + reversed_number
#     print(reversed_number)


# print("The reverse of the number is:", reversed_number)

# a=int(input("enter the value"))
# b=int(input("enter the value"))
# c=int(input("enter the value"))

# if a==b==c:
#    print("all values are equal")
# else:
#    if a>=b and a>=c :
#      largest=a
#    elif b>=a and b>=c :
#      largest=b
#    else:
#      largest=c
# print(largest)

# find factorial
# num=int(input("enter a value :"))

# fact=1 # just intialize the value to store current value
# # this if condition if someone give 1 and 0,but 1 and 0 has no factorial or 
# if num<=0 and num<=1:
#     print("1 and 0 has no fact")
# else:
#     for it in range(1,num+1): #o find range
#         print(it)
#         fact*=it #multiple fact value and it value
#     print(fact)
        
# find the vowels

# string=input("enter a value str ") 
# # i am declar the variable    
# v1="aeiousAEIOUS"
# # how much it has increase
# count=0

# for i in string: 
#     # in also check the v1
#     if i in v1:
#        count+=1

# print(count)

# su =input("enter the value :")
# # inilize the count
# count=0
# for i in su: #
#     count+=int(i) # convert to the int to count
#     print(count)

# multiplication 
# mul=int(input("enter the value"))

# #
# for i in range(1,10+1):
#     sum=i*mul
#     print(i,"*2=",sum)

# fizz question
# num =int(input("enter the value :"))
# for i in range(1, num + 1):
#     if i%5==0 and i%3==0:
#       print("FizzBuzz")
#     elif i%3==0:
#      print("Fizz")
#     elif i%5==0:
#      print("bizz")
#     else:
#      print(i)

# n = int(input("Enter a positive integer: "))

# # Using the formula
# sum_natural_numbers = n * (n + 1) // 2  # Use // for integer division

# print(n, "natural numbers is:", sum_natural_numbers)


# Get a positive integer from user input
number = input("Enter a positive integer: ")


reversed_number = ""
print(reversed_number)
for digit in number:
    print(digit)
    reversed_number = digit + reversed_number
    print(reversed_number)


print("The reverse of the number is:", reversed_number)