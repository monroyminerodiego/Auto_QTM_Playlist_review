import pyperclip as pc, os
os.system('cls')

input("Presiona 'enter' para comenzar...")
df = pc.paste()
df = df.replace('\n',',')
df = df.replace('\r','')
df = df.split(',')

all_campaigns = []
for row in df:
    row = row.split('\t')
    row.pop(0); row.pop(0); row.pop(1); row.pop(1)
    all_campaigns.append(row)

last_face = ''
last_campaign = ''
unique_campaigns = []
for row_list in all_campaigns:
    if (last_face != row_list[0]) or (last_campaign != row_list[1]):
        unique_campaigns.append(row_list)
    last_face = row_list[0]
    last_campaign=row_list[1]

x = 0
formula = '=Y($F:$F=1,O('
for campaign in unique_campaigns:
    if x%2 == 0:
        formula += f',Y($D:$D="{campaign[0]}",$G:$G="{campaign[1]}")'
    x += 1
    
    
formula += '))'


pc.copy(formula)
print('Formula generada con éxito...!!!')