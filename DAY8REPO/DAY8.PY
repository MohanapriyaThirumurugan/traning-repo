def merge(nums1, m, nums2, n):
    # Start from the end of both arrays
    i, j, k = m - 1, n - 1, m + n - 1

    # While there are still elements in nums2
    while j >= 0:
        print(f"Before comparison: i = {i}, nums1[i] = {nums1[i] if i >= 0 else 'None'}, j = {j}, nums2[j] = {nums2[j]}, k = {k}")
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        print(f"After comparison: nums1 = {nums1}\n")

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]  # Has enough space to hold all elements from nums2
m = 3  # Number of elements to consider in nums1 (1, 2, 3)
nums2 = [2, 5, 6]  # The array we want to merge into nums1
n = 3  # Number of elements in nums2

# Call the merge function
merge(nums1, m, nums2, n)

# Output the merged array
print("Final nums1:", nums1)   



def generate_pascals_triangle(numRows):
    triangle = []
    
    for row in range(numRows):
        # Create a new row with '1's
        new_row = [1] * (row + 1)
        print(new_row,"....................new row")
        
        # Each element (except for the first and last) is the sum of the two above it
        for j in range(1, row):
            new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
            print(new_row[j],'................................jjjj')
        
        # Add the new row to the triangle
        triangle.append(new_row)
    
    return triangle

# Example usage
numRows1 = 2
print(generate_pascals_triangle(numRows1))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# numRows2 = 1
# print(generate_pascals_triangle(numRows2))  # Output: [[1]]


















class groupsoffunction:
    name="this class has the two function"

    def arraymerge(self,num1,num2,m,n):
        # define of loop
        i=m-1
        j=n-1
        k=m+n-1

        while j>=0:
            if(i>=0)and(num1[i]>num2[j]):
                num1[k]=num1[i]
                i-=1
            else:
                num1[k]=num2[j]  
                j-=1
            k-=1
        return num1
    def string(self):

        name="AUKBC"
        location="chrompet"
        campus="M.I.T"
# how to create a obeject
classobject= groupsoffunction()
classobjectagain= groupsoffunction()

#how to accesses the class element using object
# print(classobjectagain.arraymerge([1,2,3,0,0,0],[2,3,4],3,3))
# print(classobject.name)

# how to use constructor in class and obejct
class electronics:
    def __init__(self):
        self.name=""
        self.group='headphones'
        self.device="hp"
    def reversstring(self,val):
        temp=[]
        for i in val:
            temp=[i]+temp
        return temp 
    def __init__(self):
        self.name="hp"
        self.ram="4ram" 
        self.storage="12gb"

# object creation

gagets=electronics()
gagets.name="boat"
print(gagets.name)
print(gagets.reversstring("mohana"))

#instance varaible
class Phone:
    def __init__(self, brand, price):
        self.brand = brand  # Instance variable
        self.price = price  # Instance variable
samsung = Phone("Samsung", 5000)
print(samsung.brand)  # Accessing instance variable


#class variable
class Phone:
    charger_type = 'c-type'  # Class variable
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display(self):
       print( self.brand)
       print(self.price)
# we can change the class variable also
Phone.charger_type='b-type'
redmi=Phone("redmi","500")
redmi.display()
print(Phone.charger_type)  # Accessing class variable


# DIFFERENT TYPE OF CLASS METHOD IN PYTHON
#instance method
class school:
   def __init__(self):
       self.fees=""
       self.schlname="rajavignesh"
   def setschlname(self,schlname):
     self.schlname=schlname
   def getschlname(self):
     print(self.schlname)
# object creation
highschool=school()
highschool.setschlname("sowdambikka")
highschool.getschlname()

#class method
# cls is a keyword and it is used to acceses the class variable
class Laptop:
    # Class variable
    lapname = "Dell laptop"
    
    def __init__(self):
        self.brand = " "
        self.price = "2000"
    
    @classmethod
    def chargetype(cls):
        cls.lapname = "HP LAPTOP"

lap = Laptop()
Laptop.chargetype()
print(Laptop.lapname)  

#static method call
class college:
    universityname="anna university"
    def __init__(self):
        self.name="au kbc"
        self.fees="80000"
    @staticmethod
    def info():
        clgname="jec",
        print(f"College name: {clgname}")

clg=college()
clg.info()

      


    






