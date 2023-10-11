import os, pandas as pd
os.system('cls')

# Path of folder with images from IBO
# path = 'C:/Users/Diego Monroy/OneDrive/BBP/Images IBO/' # Path para lap trabajo
path = 'C:/Users/diego/OneDrive/BBP/Imagenes IBO Test/' # Path para lap diego

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


# Enters in every subdirectory 
for ParentDir in CSV_ParentDirs:
    os.system('cls')
    print(f'{"*" * 15} List of files in {ParentDir} from CSV_ParentDirs {"*" * 15}\n')
    
    # Get the info of the segmented file
    df = parameters_file.query(f"SellerID == {ParentDir}")
    print(f'{"*" * 15} Head of df {"*" * 15}\n{df.head()}\n\n')

    # Enters the folder
    path = f'{path}{ParentDir}/'
    os.chdir(f'{path}')

    directory_files = os.listdir()
    missing_images = []
    
    # Obtener solo los valores de directory_files que concuerden con el nombre del file
    for row in df.itertuples():
        old_name = row.FaceID
        new_name = row.ClientFaceID
        files = [match for match in directory_files if old_name in match]
        if len(files) == 0:
            missing_images.append(old_name)
            continue
        
        print(f'Match {old_name}\n{files}')
    
    # for file in directory_files:
    #     file = os.path.splitext(file)
    #     file_name, file_extension = file[0], file[1]
    #     if not(file_name in list(df['FaceID'])):
    #         missing_images.append(file_name)

    print(f'{"*" * 15} Missing files {"*" * 15}\n{missing_images} - Len: {len(missing_images)}\n\n')
    break