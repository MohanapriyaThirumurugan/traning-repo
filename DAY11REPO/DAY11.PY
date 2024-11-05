# this is class and object using manipulation
import pandas as pd

class totalclass():
    def get_data_from_csvfile(self):
        self.df=pd.read_csv('orders.csv')  
        # print(df)
    def data_manipulate(self):
        data=self.df.groupby('Product')['Price'].sum()
        print(data)

class class2(totalclass):
    def data_manipulate2(self):
        data2 = self.df.groupby(['Product','Quantity'])['Price'].sum()
        print(data2)

a1=totalclass()
a1.get_data_from_csvfile()
a1.data_manipulate()
a2=class2()
a2.get_data_from_csvfile()
a2.data_manipulate2()
a2.data_manipulate()

# here what i am going to do import file from manipulation and save the file 
from MANIPULATION import class2,totalclass
a2 = class2()
a3=totalclass()

a3.get_data_from_csvfile()
a2.get_data_from_csvfile()
a2.data_manipulate()
                                                                                          
manipulated_data = a2.df
manipulated_data.to_excel('oops1.xlsx', index=False)

print("Data has been saved to output_file.xlsx")