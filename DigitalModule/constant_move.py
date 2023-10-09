import pyautogui as py, os; os.system('cls')

size = py.size()

for i in [3,2,1]:
    print(f'Empezando en {i}...',end='\r')
    py.sleep(1)


while True:
    for side in ['C','L','U','R','D']:
        if side == 'L':
            x -= 150
        elif side == 'U':
            y += 150
        elif side == 'R':
            x += 150
        elif side == 'D':
            y -= 150
        else:
            x = (size.width)/2
            y = (size.height)/2

        os.system('cls')
        print(f'Moviendo a ({x},{y})...',end='\r')
        py.moveTo(x,y,duration=2)
        py.sleep(2.5)
            
