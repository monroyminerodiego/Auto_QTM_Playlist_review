import pyperclip as pc, os, datetime as dt, sys
os.system('cls')

def generate_schedule(days_to_substract=0):
    '''
    The function only takes one optional parameter, called 'days', which will have a default value of 0, refering to the days that we need to substract of the actual date in the data.

    The output of this function will be a string containing all the data from 'bitacora.txt' file, transformed to match the format of 'MX Schedule' spreadsheet file.
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
    
    def get_elapsed_time(activity):
        '''
        Function created to calculate the duration of the activity.

        Takes by input a required argument called 'activity', which expects to be a list with  3 elements following the next order: Initial Hour, Activity Description, Final Hour.

        The output of this function will be the time elapsed during the development of the activity.
        
        Notes:
        - Hours must have the following format "%H:%M"
        '''
        initial_hour = dt.datetime.strptime((f'{activity[0]}'),'%H:%M')    
        final_hour = dt.datetime.strptime((f'{activity[2]}'),'%H:%M')
        time_elapsed = "{:.1f}".format((int((final_hour-initial_hour).total_seconds()))/3600)
        return time_elapsed

    def get_prj_ctg(task):
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
        
    
    activities = open('Notes/bitacora.txt')
    clipboard = ''
    row_number = 2
    for activity in activities:
        activity = ((activity).replace('\n','')).split('|')
        
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