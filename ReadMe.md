# BBP (BillboardPlanet) - Professional Repository
## Description
The following repository is 

## Description of files
- **Images**  
Folder used to store the images that the AOPP Robots will refer to accomplish their tasks.

- **Notes**  
    - **bitacora.txt**  
    File used to keep track of all the daily activities that were made, which have the following structure: 
        | Starting Date | Activity Description | Ending Date |
        | :---: | :---: | :---: |
        | 7:00  | Playlist Review | 8:00 |
        | ...  | ... | ... |
    
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
    File to keep track of all tickets created, which follows the next structure:
        
        | Date of creation | Title of Ticket | Description of ticket |
        | :---: | :---: | :---: |
        | - 02/10/2023  | [QTM] Player is not sync | Player is not sync with campaigns |
        | ...  | ... | ... |

- **schedule.py**  
Script made to read 'bitacora.txt' data and transform it in order to follow the 

- **start_sesion.py**  


- **xcel_formula.py**  



## Version Log
### v 1.0.3:
- Added docummentation, 'schedule.py' file, 'xcel_formula.py' file.
- Modification of some parameters in 'start_sesion.py' file.
- Creation of folder 'Notes', which will contain the '.txt' files used to keep track/order of notes required in BBP - Digital Services area. 
- Creation of folder 'Images', which will contain the needed '.png' images for 'start_sesion.py' file to work properly.