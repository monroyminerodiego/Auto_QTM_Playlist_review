import os, pandas as pd, numpy as np
from getpass import getuser
from tqdm import tqdm
os.system('cls'); input(f"renaming.py\n\n")

path = f'C:/Users/{getuser()}/OneDrive/BBP/Images IBO Test/'
ParametersCSV = pd.read_csv(open('Data/parameters.csv'))

ParentDirs = list(set(ParametersCSV['SellerID']))
ParentDirs.sort()

for ParentDir in ParentDirs:
    os.chdir(f'{path}{ParentDir}')

    # Lista de directorios
    DirList = pd.DataFrame(columns=['FileName','Extension','FileNameCleaned'])
    for file in os.listdir(): 
        file = os.path.splitext(file)
        file = [file[0],file[1],(file[0])[:-3] if (file[0])[-3:] == '-AS' else file[0]]
        DirList.loc[len(DirList.index)] = file

    print(f'{"*"*10} Head of DirList "{ParentDir}" {"*"*10}\n{DirList.head()}\n{len(DirList)}\n\n')

    delete_row_df = []
    save_files = []

    # bucle que evalua si el archivo se tiene que guardar o eliminar dependiendo de -AS / -BS
    for row in DirList.itertuples():
        if row.FileName[-3:] == '-AS':
            save_files.append(f'{row.FileName}{row.Extension}')
        else:
            # os.remove(f'{row.FileName}{row.Extension}')
            delete_row_df.append(row.Index)


    # Creacion de DirList limpia
    DirList_cleaned = DirList.drop(delete_row_df,axis=0)
    print(f'{"*"*10} Head of DirList_cleaned "{ParentDir}" {"*"*10}\n{DirList_cleaned.head()}\n{len(DirList_cleaned)}\n\n')

    
    delete_files =[]
    
    for row in DirList_cleaned.itertuples():
        if not(row.FileNameCleaned in list(ParametersCSV['FaceID'])):
            delete_files.append(f'{row.FileName}{row.Extension}')
            print(f'{row.FileName}{row.Extension}', end='\r')

    break
