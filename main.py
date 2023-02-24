import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

file_path = input("Enter the file path:")
sheet_name = input("Enter the file name:")
A= input("Enter the aadhaar number:")
df=pd.read_excel(file_path,engine='openpyxl')
df1=df
print(df1)


if A in df1.values:
   print("ALready Registered")

else:
    a = input("Enter your name:")
    b = input("Enter your Gender:")
    c = input("Enter your Phone Number:")
    data = {'Aadhaar Number': [A],
            'Name': [a],
            'Gender': [b],
            'PHONE NUMBER': [c]}
    df2 = pd.DataFrame(data)
    df3 = df1.append(df2)
    writer = pd.ExcelWriter(file_path, engine='openpyxl')
    df3.to_excel(writer, sheet_name, index=False)
    writer.save()






