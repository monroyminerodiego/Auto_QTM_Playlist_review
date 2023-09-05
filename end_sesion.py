import pyperclip as pc, os, datetime as dt
os.system('cls')

def generate_schedule():
    keywords_list = ['playlist','playlist2','qplayer versions']
    keywords_dic = {
        'playlist' :'Digital Support\tAll\t\tFirst webcam and playlist monitoring',
        'playlist2':'Digital Support\tAll\t\tSecond webcam and playlist monitoring',
        'qplayer versions':'Digital Support\tAll\t\tUpdate of Qplayer versions'
        }
    
    # Headers of MX Schedule
    # Year -- Month -- Day -- Person -- (Project -- Category -- Is Sev1 -- Task) -- Hrs -- Billable Hrs -- WeekNum
    # [CHECK]
    def get_elapsed_time(activity):
        hora_inicial = dt.datetime.strptime((f'{activity[0]}'),'%H:%M')    
        hora_final = dt.datetime.strptime((f'{activity[2]}'),'%H:%M')
        tiempo_transcurrido = "{:.1f}".format((int((hora_final-hora_inicial).total_seconds()))/3600)
        return tiempo_transcurrido
    # [CHECK]
    def get_prj_ctg(task):
        task_lower = task.lower()
        if task_lower in keywords_list:
            return keywords_dic[task_lower]
        elif 'couching' in task_lower:
            return f'BBP Projects\tTraining\t\t{task}'
        elif 'ticket' in task_lower:
            return f'BBP Projects\tTraining\t\t{task}'
        else:
            return f'\t\t\t{task}'
        

    
    activities = open('../Notes/bitacora.txt')
    clipboard = ''
    row_number = 2
    for activity in activities:
        activity = ((activity).replace('\n','')).split('|')
        
        row_info = f'{dt.datetime.now().year}\t{dt.datetime.now().month}\t{dt.datetime.now().day}\tDiego\t{get_prj_ctg(activity[1])}\t{get_elapsed_time(activity)}\t\t=NUM.DE.SEMANA(FECHA(A{row_number},B{row_number},C{row_number}),1)'
        
        clipboard = f'{clipboard}{row_info}\n'
        row_number += 1
    return clipboard

if __name__ == '__main__':
    schedule = generate_schedule()
    pc.copy(schedule)
    print(f'\nSchelude copied to clipboard:\n{schedule}')