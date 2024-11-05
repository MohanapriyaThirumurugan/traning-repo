import pandas as pd
# read the excel file using pandas
df=pd.read_excel('sales_data.xlsx')
# print(df)
# Find the total sales for each region.
totalsales=df.groupby('Region')['Sales'].sum()
# print(totalsales)
 #Find the product that generated the highest sales in each region.
productsales=df.groupby(['Product','Region'])['Sales'].sum()
regiongroup=productsales.reset_index()
maximumsales=regiongroup.loc[regiongroup.groupby('Region')['Sales'].idxmax()]
# print(maximumsales)
# print(regiongroup)
# print(productsales)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
# print(df['Month'].to_string())
# monthly_sales = df.groupby('Month')['Sales'].sum()
# print(monthly_sales)


# ---------------------------------------------------------------------------------------------------

# Employee Data Filtering
# 1. Read the CSV file into a pandas DataFrame.

# df1=pd.read_csv('employee_data.csv')
# print(df1)
#  Filter out employees who are older than 40 and have a salary greater than 50,000

# sum=df1[(df1['Age']>=40)&(df1['Salary']>=50000)]
# print(sum)


# 3. Calculate the average salary by department.
# sum1=df1.groupby('Department')['Salary'].mean()
# print(sum1)

# Identify the department with the highest number of employees.
# identify =df1.groupby('Department')['Name'].count()
# print(identify)
# hightestemp=identify.idxmax()
# print(hightestemp)

# Save the filtered data to an Excel file
# sum.to_excel('pandassavedfile.xlsx', index=False)



# ----------------------------------------------------------------------------------------------------------------

# Student Grades Analysis
# Read the Excel file into a pandas DataFrame.
df3=pd.read_excel('grades.xlsx')
print(df3)
#  Calculate the average grade for each student across all subjects
df3['Avarage']=df3.set_index('Student')[['Math','Science','English']].mean(axis=1)

df3['Avarage']
print(df3['Avarage'])
# Find the student(s) with the highest average grade.
highestavg_by_std=df3['Avarage'].idxmax()
highest_score=df3['Avarage'].max()
print(f"Student with the highest average grade: {highestavg_by_std},Highest average grade: {highest_score}")

# 4. Add a new column `Pass/Fail` based on the condition that if a student has an average grade of 50 or above, they pass; otherwise, they fail.
df3['Pass/Fail']=df3['Avarage'].apply(lambda x:'pass' if x>50 else 'fail')

print(df3[['Avarage', 'Pass/Fail']].to_string())

# sorted_df = df3.sort_values(by='Average', ascending=False)



# -------------------------------------------------------------------------------------------------------


# Financial Data Processing
# Read the JSON file into a pandas DataFrame.

# df4=pd.read_json('financial_data.json', lines='True')
# # print(df4)

# #  Calculate the total deposits and total withdrawals.

# totalamount=df4.groupby('Transaction Type')['Amount'].sum()
# print(totalamount)

# #  Calculate the net balance (total deposits - total withdrawals).
# netbalance=df4[('Deposit',0)-totalamount.get('Withdrawal',0)]
# print(netbalance)
# df4['netdeposite']=netbalance
# print(df4['netdeposite'])

# print(df4[['Transaction Type', 'Amount', 'netdeposite']])

# #  Identify the month with the highest net deposits.

# df4['Date']=pd.to_datetime(df4['Date'])
# df4['Month'] = df4['Date'].dt.month

# monthly_deposite=df4.groupby('Month')['netdeposite'].max()
# print(monthly_deposite,"MONTHLY DEPOSITE")

# df4.to_csv('financial_data_processed.csv', index=False)


# ----------------------------------------------------------------------------------------------------
# . Read the CSV file into a pandas DataFrame.

# df5=pd.read_csv('orders.csv')
# print(df5)
# # 2. Calculate the total amount spent by each customer.

# totalamountspent=df5.groupby('Customer ID')['Price'].sum()
# print(totalamountspent,'to...................................')
# # 3. Find the product that generated the most revenue.

# mostrevenue=df5.groupby('Product')['Price'].idxmax()
# max_revenue_amount = df5.groupby('Product')['Price'].sum().max()  

# print(f"revcenue by product {mostrevenue}  max_revenue_amount{max_revenue_amount}")
# # 4. List the top 3 customers who have spent the most.
# top3=totalamountspent.head(3)
# print(top3)
# # 5. Save the summary of customer spending into a new file `customer_spending.xlsx`.
# df5.to_excel('customer_spending.xlsx',index='flase')