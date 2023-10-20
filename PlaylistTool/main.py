import pandas as pd, os, pyperclip as pc, json
os.system('cls')

# input('main.py...\nPresiona enter para pegar la información...\n')
# content = (pc.paste().replace('\r','').split('\n'))
content = open('Data/playlist.txt')

x = 0
data = []
for row in content:
    row = row.replace('\r','').replace('\n','')
    row = row.split('\t')
    if x == 0:
        headers = row
    else:
        data.append(row)
    x += 1

Playlist = pd.DataFrame(data=data,columns=headers)

CompanyNames  = list(set(Playlist['CompanyName']))
CompanyNames.sort()
for CompanyName in CompanyNames:
    Playlist_filtered = Playlist.query(f"CompanyName == '{CompanyName}'")
    print(f"{'*'*10} Playlist head of {CompanyName} {'*'*10}\n{Playlist_filtered.head()}\n\n")

    break