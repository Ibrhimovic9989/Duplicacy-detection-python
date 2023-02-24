#Importing the required libraries
import pandas as pd

#Taking input from user for file path, sheet name and aadhaar number

file_path = input("Enter the file path:")
sheet_name = input("Enter the file name:")
A = input("Enter the aadhaar number:")

#Reading the excel file into pandas dataframe

df = pd.read_excel(file_path, engine='openpyxl')
df1 = df

#Checking if the aadhaar number is already present in the dataframe

if A in df1.values:
  print("Already registered")
else:
# If aadhaar number is not present, taking input for name, gender and phone number
  a = input("Enter your name:")
  b = input("Enter your Gender:")
  c = input("Enter your Phone Number:")


# Creating a dictionary of the new data to be added and converting it to pandas dataframe
data = {'Aadhaar Number': [A],
        'Name': [a],
        'Gender': [b],
        'PHONE NUMBER': [c]}
df2 = pd.DataFrame(data)

# Appending the new data to the original dataframe and writing it to the same excel file
df3 = df1.append(df2)
writer = pd.ExcelWriter(file_path, engine='openpyxl')
df3.to_excel(writer, sheet_name=sheet_name, index=False)
writer.save() 


