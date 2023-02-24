# Duplicacy-detection-python
#This is a Python code for adding new data to an existing Excel file. Here's how it works:

#The user is prompted to enter the file path, sheet name, and Aadhaar number.
#The Excel file is loaded into a pandas DataFrame.
#If the Aadhaar number already exists in the DataFrame, the code outputs "Already Registered" and does not add any new data.
#If the Aadhaar number does not exist in the DataFrame, the user is prompted to enter their name, gender, and phone number.
#The new data is stored in a dictionary and converted to a pandas DataFrame.
#The new DataFrame is appended to the original DataFrame.
#The combined DataFrame is written to the same Excel file using the openpyxl engine.
#Note that the code uses the openpyxl engine to read and write Excel files. The xlsxwriter library is also imported but not used in this code.
