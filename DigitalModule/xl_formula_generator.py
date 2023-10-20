import pyperclip as pc, os, sys
import fill_schedule as fs
os.system('cls')

input("Presiona 'enter' para comenzar...")
def condicional():
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

try:
    formula = sys.argv[1]
except:
    formula = 'c'

if formula == 'p':
    pc.copy('=SUMAR.SI.CONJUNTO(O:O,G:G,SI(Y(G2=G3,H2=H3),"",G2),D:D,SI(Y(G2=G3,H2=H3),"",D2),F:F,1,H:H,SI(Y(G2=G3,H2=H3),"",H2))')
    formula = 'conteo de Playcounts'
else:
    condicional()
    formula = 'formato condicional'
print(f'Formula para {formula} copiada con éxito...!!!')