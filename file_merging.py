#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import subprocess

def run_python_scripts(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            print(f"Running {filename}...")
            subprocess.call(["C:\\Users\\aogunbanwo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe", os.path.join(directory, filename)])

# Replace 'your_directory' with the path to the directory containing your Python scripts
run_python_scripts(r'C:\Users\ogunb\OneDrive\Desktop\Portfolio\Script')
print("All Script Updated")


print(f"Combining the differnet volume files for Snowflake.....")

import os
import pandas as pd


files = os.listdir("C:\Users\ogunb\OneDrive\Desktop\Portfolio\files")


rows = 0
main = pd.DataFrame()

for file in files:
    df = pd.read_csv(f"C:\Users\ogunb\OneDrive\Desktop\Portfolio\files/{file}")
    rows = rows + len(df)
    main = pd.concat([main, df], ignore_index=True)


print(f"No of rows : {rows}",f"No of rows : {len(main)}" )


df = main.copy()


df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
df.dtypes


filename = r'C:\Users\ogunb\OneDrive\Desktop\Portfolio\Forecast_Volume.csv'
df.to_csv(filename, index=False)


print("Updated Successfuly")



print(f"Combining the differnet Handle files for Snowflake.....")

import os
import pandas as pd


files = os.listdir("C:\Users\ogunb\OneDrive\Desktop\Portfolio\handle Forecast")


rows = 0
main = pd.DataFrame()

for file in files:
    df = pd.read_csv(f"C:\Users\ogunb\OneDrive\Desktop\Portfolio\handle Forecast/{file}")
    rows = rows + len(df)
    main = pd.concat([main, df], ignore_index=True)

    
print(f"No of rows : {rows}",f"No of rows : {len(main)}" )


df = main.copy()


df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
df.dtypes


filename = r'C:\Users\ogunb\OneDrive\Desktop\Portfolio\\Handle_Forecast_AHT.csv'
df.to_csv(filename, index=False)


print("Updated Successfuly")
