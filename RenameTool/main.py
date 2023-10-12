import os, pandas as pd, numpy as np
from getpass import getuser
from tqdm import tqdm
os.system('cls'); input("main.py...")

# Path of folder with images from IBO
path = f'C:/Users/{getuser()}/OneDrive/BBP/Images IBO/'


# Get the info from csv file
parameters_file = pd.read_csv('Data/parameters.csv',sep=',')
# print(f'{"*" * 15} Head of CSV_File {"*" * 15}\n{parameters_file.head()}\n\n')


#Get unique SellerID column values
CSV_ParentDirs = list(set(parameters_file['SellerID']))
CSV_ParentDirs.sort()
# print(f'{"*" * 15} CSV ParentDirs {"*" * 15}\n{CSV_ParentDirs}\n\n')


# Get in a list all the directories from downloaded images
os.chdir(path)
IBO_ParentDirs = os.listdir()
for index in range(len(IBO_ParentDirs)):
    IBO_ParentDirs[index] = int(IBO_ParentDirs[index])
IBO_ParentDirs.sort()
# print(f'{"*" * 15} IBO ParentDirs {"*" * 15}\n{IBO_ParentDirs}\n\n')
    

# Compares the IBO directories with csv file
MissingDirs = list(set(CSV_ParentDirs).difference(IBO_ParentDirs))
# print(f'{"*" * 15} Missing Dirs - IBO {"*" * 15}\n{MissingDirs}\n\n')

# Titles for report
missing_files_csv = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/missing_files.csv','a')
np.savetxt(missing_files_csv,['SellerID,CompanyName,FaceID,ClientFaceID'],fmt='%s',delimiter=',')
missing_files_csv.close()

unchanged_files = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/unchanged_files.csv','a')
np.savetxt(unchanged_files,['Folder,File'],fmt='%s',delimiter=',')
unchanged_files.close()

duplicated_files = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/duplicated_files.csv','a')
np.savetxt(duplicated_files,['SellerID,CompanyName,FaceID,ClientFaceID'],fmt='%s',delimiter=',')
duplicated_files.close()

# Enters in every subdirectory 
for ParentDir in CSV_ParentDirs:
    os.system('cls')
    
    # Get the info of the segmented file
    df = parameters_file.query(f"SellerID == {ParentDir}")

    # Enters the folder
    os.chdir(f'{path}{ParentDir}/')

    directory_files = os.listdir()
    missing_files = []
    
    
    print(f'{"*" * 15} List of files in folder "{ParentDir}" from CSV_ParentDirs {"*" * 15}\n{df.head()}\nExpected matchs: {len(df)}\n\n')
    # Iterates the df to rename the files in folder
    for row in tqdm(df.itertuples()):
        old_name_csv = row.FaceID
        new_name_csv = row.ClientFaceID
        files = [match for match in directory_files if old_name_csv in match]

        #If there's no files 
        if len(files) == 0:
            missing_files.append(f'{row.SellerID},{row.CompanyName},{row.FaceID},{row.ClientFaceID}')
            continue
        
        for file in files:
            directory_files.remove(file)
            file = os.path.splitext(file)
            old_name_file, file_extension = file[0], file[1]
            new_name_file = old_name_file.replace(str(old_name_csv),str(new_name_csv).replace('/','-'))
            try:
                os.rename(old_name_file+file_extension,new_name_file+file_extension)
            except FileExistsError:
                duplicated_files = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/duplicated_files.csv','a')
                np.savetxt(duplicated_files,[f'{row.SellerID},{row.CompanyName},{row.FaceID},{row.ClientFaceID}'],fmt='%s',delimiter=',')
                duplicated_files.close()

        
    missing_files_csv = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/missing_files.csv','a')
    np.savetxt(missing_files_csv,missing_files,fmt='%s',delimiter=',')
    missing_files_csv.close()

    if len(directory_files) != 0:
        unchanged_files = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/unchanged_files.csv','a')
        for file in directory_files:
            np.savetxt(unchanged_files,[f'{ParentDir},{file}'],fmt='%s',delimiter=',')
        unchanged_files.close()

    print(f'{len(missing_files)} Missing files\n\n')

    # input('Presiona enter para continuar...')

    