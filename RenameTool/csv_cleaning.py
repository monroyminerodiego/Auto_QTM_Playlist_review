import pandas as pd, numpy as np, os
from tqdm import tqdm
os.system('cls'); input("csv_cleaning.py...")


ParametersCsv, UnchangedCsv, MissingCsv = pd.read_csv(open('Data/parameters.csv')), pd.read_csv(open('Data/unchanged_files.csv')), pd.read_csv(open('Data/missing_files.csv'))
path = 'C:/Users/Diego Monroy/OneDrive/BBP/Images IBO/'

# Validating Missing Data
MissingDirs_MissingCsv = list(set(MissingCsv['SellerID']))
MissingCsv_cleaned = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/MissingFiles_cleaned.csv','a')
np.savetxt(MissingCsv_cleaned,["SellerID,CompanyName,FaceID,ClientFaceID"],fmt='%s',delimiter=',')
MissingCsv_cleaned.close()


for ParentDir in tqdm(MissingDirs_MissingCsv):
    os.chdir(f'{path}{ParentDir}/')
    df = MissingCsv.query(f"SellerID == {ParentDir}")

    files = os.listdir()

    for row in df.itertuples():
        if (len([match for match in files if str(row.ClientFaceID) in match]) == 0) and (len([match for match in files if str(row.FaceID) in match]) == 0):
            MissingCsv_cleaned = open('C:/Users/Diego Monroy/Projects/BBP/RenameTool/Data/MissingFiles_cleaned.csv','a')
            np.savetxt(MissingCsv_cleaned,[f"{row.SellerID},{row.CompanyName},{row.FaceID},{row.ClientFaceID}"],fmt='%s',delimiter=',')
            MissingCsv_cleaned.close()



    

