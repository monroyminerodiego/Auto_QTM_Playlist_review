import pyperclip as pc, os, datetime as dt, sys
os.system('cls')

def generate_schedule(days_to_substract:int=0):
    '''
    Function that generates a string with the data from './Notes/bitacora.txt'

    Inputs:
    - days_to_substract type['int']: Default value is set to '0', but it expects the number of days to substract to actual date.

    Outputs:
    - cliboard type['str']: String that has the data from './Notes/bitacora.txt' in the correct form to be paste in 'MX Schedule' spreadsheets
    '''
    keywords_dic = {
        'playlist' :'Digital Support\tAll\t\tFirst webcam and playlist monitoring',
        'playlist2':'Digital Support\tAll\t\tSecond webcam and playlist monitoring',
        'qplayer versions':'Digital Support\tAll\t\tUpdate of Qplayer versions',
        'playcounts':'Digital Support\tAll\t\tManual count of displaying creatives',
        'IT Meeting':'Digital Support\tAll\t\tIT Weekly Meeting'
        }
    keywords_list = [keyword for keyword in keywords_dic.keys()]
    
    # Headers of MX Schedule
    # Year -- Month -- Day -- Person -- (Project -- Category -- Is Sev1 -- Task) -- Hrs -- Billable Hrs -- WeekNum
    
    def get_elapsed_time(activity:list):
        '''
        Function that calculate the time elapsed between 2 time strings

        Inputs:
        - activity type['list']: Only 3 strings are expected to be included on the list in this especific order [Initial hour,Description of Activity,Final hour].
            - Initial hour: String with the information of the initial hour to be consider. Must have the following format: '%H:%M'
            - Description of Activity: String describing the activity developed during the time to calculate 
            - Final hour: String with the information of the final hour to be consider. Must have the following format: '%H:%M'

        Outputs:
        - time_elapsed type['string']: String that represents the time elapsed between Initial hour and Final hour
        '''
        initial_hour = dt.datetime.strptime((f'{activity[0]}'),'%H:%M')    
        final_hour = dt.datetime.strptime((f'{activity[2]}'),'%H:%M')
        time_elapsed = "{:.1f}".format((int((final_hour-initial_hour).total_seconds()))/3600)
        return time_elapsed

    def get_prj_ctg(task:str):
        '''
        This function takes by arguments only one parameter, which will be the activity description
        '''
        task_lower = task.lower()
        if task_lower in keywords_list:
            return keywords_dic[task_lower]
        elif 'couching' in task_lower:
            return f'BBP Projects\tTraining\t\t{task}'
        elif 'ticket' in task_lower:
            return f'Digital Support\tAll\t\t{task}'
        elif 'meeting' in task_lower:
            return f'Digital Support\tMeeting\t\t{task}'
        else:
            return f'\t\t\t{task}'
        
    def sum_breaks_elapsed_time(activity:str):
        '''
        '''



        return activity


    file = open('../Notes/bitacora.txt')
    clipboard = ''
    row_number = 2
    for activity in file:
        activity = ((activity).replace('\n','')).split('|')

        if '~' in activity: activity = sum_breaks_elapsed_time(activity)
        
        date = dt.datetime.now() - dt.timedelta(days=days_to_substract)

        row_info = f'{date.year}\t{date.month}\t{date.day}\tDiego\t{get_prj_ctg(activity[1])}\t{get_elapsed_time(activity)}\t\t=NUM.DE.SEMANA(FECHA(A{row_number},B{row_number},C{row_number}),1)'
        
        clipboard = f'{clipboard}{row_info}\n'
        row_number += 1
    return clipboard

if __name__ == '__main__':
    try:
        days = int(sys.argv[1])
        schedule = generate_schedule(days)
    except:
        schedule = generate_schedule()
    pc.copy(schedule)
    counts = schedule.count("\n")
    print(f'\n({counts}) Schedule copied to clipboard:\n{schedule}')