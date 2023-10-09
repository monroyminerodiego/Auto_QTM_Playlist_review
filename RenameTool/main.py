import os, sys, pandas as pd
os.system('cls')

# Get the info from csv file
parameters_file = pd.read_csv('Data/parameters.csv',sep='\t')

# Changes the directory from 
images_path = 'C:/Users/Diego Monroy/OneDrive/BBP/Images IBO/'
os.chdir(images_path)
directories = [directory for directory in os.listdir(images_path)]

unique_dirs=[]
unexisting_directories=[]

print(f'{"*" * 15} Head of File {"*" * 15}\n{parameters_file.head()}\n\n')

for row in parameters_file['SellerID']:
    if not(row in unique_dirs):unique_dirs.append(row)
    # if not(row): unexisting_directories.append(row)