import pandas as pd

# file=pd.read_excel('sales_data.xlsx', usecols=['Region','Sales','Product'])
# print(file.to_string())

# emptdic={}

# for i in range(len(file)):
#     region=file['Region'][i]
#     sales=file['Sales'][i]
#     # print(region,sales)

#     if region in emptdic:
#         emptdic[region]+=sales
#         pass


#     else:
#         emptdic[region]=sales
# print(emptdic)

# for k in emptdic:
#     v =(f'Reegion_Name: {k}, Total_Sales: {emptdic[region]}')
# print(v)


import pandas as pd

# Read the Excel file into a pandas DataFrame
file_path = 'sales_data.xlsx'
df = pd.read_excel(file_path)


highest_sales = df.groupby(['Region', 'Product'])['Sales'].sum().reset_index()
highest_sales= highest_sales.loc[highest_sales.groupby('Region')['Sales'].idxmax()]
# print(highest_sales)


import pandas as pd

# # Read the Excel file into a pandas 
# file_path = 'sales_data.xlsx'
# df = pd.read_excel(file_path)

# df['Date'] = pd.to_datetime(df['Date'])
# df['Month'] = df['Date'].dt.to_period('M')
# findsales = df.groupby('Month')['Sales'].sum()
# print(findsales)



df = pd.read_csv('employee_data.csv')
var = df[(df['Age']>50) & (df['Salary']>50000)]
print (var)

# df = pd.read_csv('employee_data.csv')
# var = df.groupby('Department')['Salary'].mean()
# print (var)

# v= df['Department'].value_counts().idxmax()
# print (v)


