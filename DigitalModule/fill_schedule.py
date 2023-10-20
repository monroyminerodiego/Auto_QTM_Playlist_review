class generate_schedule:
    '''
    Class that generates a string with the data from a '.txt' file.

    Mandatory Inputs:
    - file_path type['str']: Expects the path of one '.txt' file that follows the format of '../Notes/bitacora.txt' (See documentation for more information)

    Optional Inputs:
    - days_to_substract type['int']: Expects the number of days to substract to actual date. Default value is set to '0'.

    Outputs:
    - cliboard type['str']: String that has the data from 'file_path' in the correct format to be paste in 'MX Schedule' spreadsheets.
    '''
    
    def __get_elapsed_time(self,activity:list):
        '''
        Function that calculate the time elapsed between 2 time strings

        Inputs:
        - activity type['list']: Only 3 strings are expected to be included on the list in this especific order [Initial hour,Title of Activity,Ending hour].
            - Initial hour: String with the information of the initial hour to be consider. Must have the following format: '%H:%M'.
            - Title of Activity: String describing the activity developed during the time to calculate.
            - Ending hour: String with the information of the final hour to be consider. Must have the following format: '%H:%M'.

        Outputs:
        - time_elapsed type['string']: String that represents the time elapsed between Initial hour and Final hour
        '''
        initial_hour = dt.datetime.strptime(f'{activity[0]}','%H:%M')    
        final_hour = dt.datetime.strptime(f'{activity[2]}','%H:%M')
        time_elapsed = "{:.1f}".format((int((final_hour-initial_hour).total_seconds()))/3600)
        return time_elapsed

    def __get_prj_ctg(self,task:str):
        '''
        Function created to return a project and category string according to keywords in 'task'

        Inputs:
        - task type['str']: Expects only the title of a task

        Outputs:
        - task type['str']: String with the project, category and the Title of the task. String contains the correct tabulations between every variable.
        '''
        task_lower = task.lower()
        if task_lower in self.keywords_list:
            return self.keywords_dic[task_lower]
        elif 'couching' in task_lower:
            return f'BBP Projects\tTraining\t\t{task}'
        elif 'ticket' in task_lower:
            return f'Digital Support\tAll\t\t{task}'
        elif 'meeting' in task_lower:
            return f'Digital Support\tMeeting\t\t{task}'
        elif 'documentation' in task_lower:
            return f'Digital Support\tAll\t\t{task}'
        elif 'follow up' in task_lower:
            return f'BBP Projects\tAll\t\t{task}'
        else:
            return f'\t\t\t{task}'
        
    def __sum_breaks_elapsed_time(self,activity:str):
        '''
        Function that sums the time elapsed between 2 or more time strings

        Inputs:
        - activity type['str']: Expects a string, with raw data from 'bitacora.txt' file, following the format "[Initial hour] | [Title of activity] | [Final hour in complex format]".
            - Initial hour: String with the information of the initial hour to be consider. Must have the following format: '%H:%M'.
            - Title of Activity: String with the activity title developed during the time to calculate.
            - Final hour: String with the information of the final hour to be consider. Must have the following format: '%H:%M~{%H:%M-%H:%M}'.

        Outpus:
        - main_activity type['list']: List that follows the format ['Inital Hour' , 'Title of Activity' , 'Ending Hour']
            - Initial hour: String with the information of the initial hour to be consider.
            - Title of Activity: String with the activity title developed during the time to calculate.
            - - Final hour: String with the information of the final hour to be consider after the addition of all breaks of time execution.
        '''
        activity_times = activity.replace('\n','').split('~{')
        
        total_minutes = 0.0
        for index in range(1,len(activity_times)):
            time = (activity_times[index][:-1]).split('-')
            total_minutes += float(self.__get_elapsed_time([time[0],'Break',time[1]]))*60
        main_activity = activity_times[0].split('|')

        main_activity[2] = (dt.datetime.strptime(f'{main_activity[2]}','%H:%M') + dt.timedelta(minutes=total_minutes)).strftime('%H:%M')

        return main_activity

    def __init__(self,file_path:str,days_to_substract:int=0):
        self.keywords_dic = {
            'playlist' :'Digital Support\tAll\t\tFirst webcam and playlist monitoring',
            'playlist2':'Digital Support\tAll\t\tSecond webcam and playlist monitoring',
            'qplayer versions':'Digital Support\tAll\t\tUpdate of Qplayer versions',
            'playcounts':'Digital Support\tAll\t\tManual count of displaying creatives',
            'IT Meeting':'Digital Support\tAll\t\tIT Weekly Meeting'
            }
        self.keywords_list = [keyword for keyword in self.keywords_dic.keys()]
        
        # Headers of MX Schedule
        # Year -- Month -- Day -- Person -- (Project -- Category -- Is Sev1 -- Task) -- Hrs -- Billable Hrs -- WeekNum

        file = open(file_path)
        self.clipboard = ''
        row_number = 2
        for activity in file:
            if '~' in activity:
                activity = self.__sum_breaks_elapsed_time(activity)
            else:
                activity = ((activity).replace('\n','')).split('|')

            
            date = dt.datetime.now() - dt.timedelta(days=days_to_substract)

            row_info = f'{date.year}\t{date.month}\t{date.day}\tDiego\t{self.__get_prj_ctg(activity[1])}\t{self.__get_elapsed_time(activity)}\t\t=NUM.DE.SEMANA(FECHA(A{row_number},B{row_number},C{row_number}),1)'
            
            self.clipboard = f'{self.clipboard}{row_info}\n'
            row_number += 1
    
    def get_schedule(self):
        return self.clipboard

if __name__ == '__main__':
    import os, sys, pyperclip as pc, datetime as dt
    os.system('cls')
    try:
        __days = int(sys.argv[1])
        __schedule = generate_schedule(file_path='../Notes/bitacora.txt',days_to_substract=__days)
    except:
        __schedule = generate_schedule(file_path='../Notes/bitacora.txt')
    pc.copy(__schedule.get_schedule())
    __counts = __schedule.get_schedule().count("\n")
    print(f'\n({__counts}) Schedule copied to clipboard:\n{__schedule.get_schedule()}')