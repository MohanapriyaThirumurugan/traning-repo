# with open("TVAQueries.txt","r",encoding="utf-8")as file1:

#     filereaded=file1.readlines()
#     lengthline =""
    
#     for j in filereaded:
#      if len(j) >len(lengthline):
#       lengthline=j
# count=0
# for k in lengthline:
#   count+=1
  
# print(lengthline)
# print(count)

# second question
# 1.Count the Number of Lines: Write a program that reads a text file line by line and counts how many lines contain a specific Tamil word (e.g., "அந்த").
# import sys

# def plusOne(digits):
#         strings = ""
#         for number in digits:
#             strings += str(number)

#         temp = str(int(strings) +1)
#         print(temp)
#         return [int(temp[i]) for i in range(len(temp))]
# print(plusOne(["1","2","12"]))

# def plusOne(digits):
#   s =''
#   for i in digits:
#     v = str(i)
#     s = s+v
#   temp = int(s)+1
#   q = str(temp)
#   l =[]
#   for j in q:
#     l.append(j)
#   return l
# print(plusOne([1,2,33,56]))

def plusone(digits):
  string=""
  for i in digits:
    val=str(i)
    string+=val
   #coverting str to int

  sum=int(string)+1
  val2=str(sum)
  temp=[]

  for j in val2:
    temp+=j
  return temp
print(plusone([1,2,13]))



