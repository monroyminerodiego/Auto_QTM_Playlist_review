import os, pandas as pd
os.system('cls')

# Path of folder with images from IBO
path = 'C:/Users/Diego Monroy/OneDrive/BBP/Images IBO/'

# Get the info from csv file
parameters_file = pd.read_csv('Data/parameters.csv',sep=',')
print(f'{"*" * 15} Head of CSV_File {"*" * 15}\n{parameters_file.head()}\n\n')

#Get unique SellerID column values
CSV_ParentDirs = list(set(parameters_file['SellerID']))
CSV_ParentDirs.sort()
print(f'{"*" * 15} CSV ParentDirs {"*" * 15}\n{CSV_ParentDirs}\n\n')

# Get in a list all the directories from downloaded images
os.chdir(path)
IBO_ParentDirs = os.listdir()
for index in range(len(IBO_ParentDirs)):
    IBO_ParentDirs[index] = int(IBO_ParentDirs[index])
IBO_ParentDirs.sort()
print(f'{"*" * 15} IBO ParentDirs {"*" * 15}\n{IBO_ParentDirs}\n\n')
    

# Compares the IBO directories with csv file
MissingDirs = list(set(CSV_ParentDirs).difference(IBO_ParentDirs))
print(f'{"*" * 15} Missing Dirs - IBO {"*" * 15}\n{MissingDirs}\n\n')


print(f'{"*" * 15} List of files in ParentDir from CSV_ParentDirs {"*" * 15}\n')
# Enters in every subdirectory 
for ParentDir in CSV_ParentDirs:
    # Get the info of the segmented file
    df = parameters_file.query(f"SellerID == {ParentDir}")
    
    os.chdir(f'{path}{ParentDir}')
    directory_files = os.listdir()
    
    missing_files = []
    for 

    print(missing_files)

    break