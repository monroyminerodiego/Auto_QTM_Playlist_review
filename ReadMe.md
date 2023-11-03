# BBP (BillboardPlanet) - Professional Repository
## Description
The following repository is 

## General Structure
- **Notes**  
    - **bitacora.txt**  
    File used to keep track of all the daily activities that were made, which have the following structure: 
        | Starting Time | Title of Activity | Ending Time |
        | :---: | :---: | :---: |
        | 7:00  | Playlist | 8:00 |
        | 8:00  | Playcounts | 9:00~{10:00-11:00}|
        | ...  | ... | ... |

        Considerations:  
        - 'Ending Time' can have two possible data formats: 'Simple' and 'Complex'.  
            **Simple format:** (E.g.: 8:00) is used when the activity did not had any break during time execution.  
            **Complex format:** ( E.g.: 9:00~{10:00-11:00} ) is used when the activity had a break during time execution.  
            E.g.: Playcounts activity started at 8:00 a.m., but at 9 a.m. the activity stopped and it was resumed from 10:00 a.m. to 11:00 a.m.  
        - Any time value needs to follow '%H:%M' format, regardless if it's 'Starting Time', 'Ending Time' in simple format or 'Ending Time' in complex format.
    <br>    

    
    - **notas.txt**  
    File with some notes about specific topics of BBP.
    
    - **pendientes.txt**  
    File where the notes of following/pending tickets tickets are stored. Also used as the file to keep track of daily pendings.
    
    - **playcounts.txt**  
    File to keep track of issues with playcounts during daily review of bbdd generated file, which follows the next structure:
        <table style="text-align:center;">
            <caption><b>Date of Incident</b></caption>
            <tr>
                <th>Company</th>
                <th>VendorFaceID</th>
                <th>Campaign</th>
                <th>Notes</th>
            </tr>
            <tr>
                <td>[PRM]</td>
                <td>133A</td>
                <td>C2109110</td>
                <td>(Campaign starts late)</td>
            </tr>
            <tr>
                <td>...</td>
                <td>...</td>
                <td>...</td>
                <td>...</td>
            </tr>
        </table>
    
    - **tickets.txt**
    File to keep track of all tickets created, which follows the next structure     
        | Date of creation | Title of Ticket | Description of ticket |
        | :---: | :---: | :---: |
        | - 02/10/2023  | [QTM] Player is not sync | Player is not sync with campaigns |
        | ...  | ... | ... |
<br><br>



- **DigitalModule**  
    Folder used to store all the scripts created to ease the development of the role 'Digital Services'.

    - **fill_schedule.py**  
        Script made to read 'bitacora.txt' data and transform it in order to follow the format of 'MX Schedule' spreadsheets, which are:<br>
        | Year | Month | Day | Person | Project | Category | Is Sev1 | Task | Hrs | Billable Hrs | WeekNum |
        | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
        | 2023  | 10 | 17 | Diego | BBP Projects | Training |     | Playlist | 1.0 |     | 42 |
        | ...  | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |<br><br>
        
        The classes involved in this file is called 'generate_schedule', which will have the following methods:
            <table style="text-align:center;">
                <tr>
                    <th>Method</th>
                    <th>Scope</th>
                    <th>Inputs</th>
                    <th>Outputs</th>
                    <th>Summary</th>
                </tr>
                <tr>
                    <td>
                </tr>
            </table>
    <br>

    - **xcel_formula.py**  


    - **constant_move.py**  
<br><br>



- **RenameTool**  
    - **Data**  

    - **List_of_IBO_companies.sql**  

    - **rename.py**
<br><br>



## Version Log
### v 1.1.0:  
- Renamed some files from 'DigitalModule' folder.
- Added 'PlaylistTool' folder.
- 

### v 1.0.3:
- Added docummentation, 'schedule.py' file, 'xcel_formula.py' file, and'constant_move.py' file.
- Modification of some parameters in 'start_sesion.py' file.
- Creation of 'Notes' folder, which will contain the '.txt' files used to keep track/order of notes required in BBP - Digital Services area. 
- Creation of 'Images' folder, which will contain the needed '.png' images for 'start_sesion.py' file to work properly.
- Creation of 'RenameTool' folder. For further documentation, check 'README.md' file from folder.