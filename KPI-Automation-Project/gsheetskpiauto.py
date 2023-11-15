import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta


#define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('kpi-automation-project-a25ba919c699.json',scope)

#authorize the clientsheet
client = gspread.authorize(creds)

#Get the instance of the spreadsheet
Spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1_G_IdOs0gLqVa4kCEI0jaA1em6b08zBwzfRPC3uxglc/edit#gid=1110613513')

#Get the two sheets you want of the spreadsheet
sheet_instance1 = Spreadsheet.get_worksheet(0)
sheet_instance2 = Spreadsheet.get_worksheet(2)

#sheet_instance1.update("B7:C10", [[0,0],[0,0],[0,0],[0,0]])

#Update value in specified range to 0
sheet_instance1.update("D18:D25", [[0],[0],[0],[0],[0],[0],[0],[0]])
sheet_instance1.update("D28:D32", [[0],[0],[0],[0],[0]])
sheet_instance1.update("D38:D40", [[0],[0],[0]])
sheet_instance1.update("D42:D48", [[0],[0],[0],[0],[0],[0],[0]])

#Cell to update (or range)
cell_to_update = "D17"

#Get the current value of the cell
current_value = sheet_instance1.acell(cell_to_update).value

#Convert the current value to a date object (assuming the current value is in date format)
current_date = datetime.strptime(current_value, "%m/%d/%Y")

#Calculate the new date that is a week from the current date
new_date = current_date + timedelta(weeks=1)

#Format the new date as a string
new_date_str = new_date.strftime("%m/%d/%Y")

#Update D17 with new value
sheet_instance1.update(cell_to_update, new_date_str)

#Define my target range
target_range = "E17:I17"

#Update target range with the new date
sheet_instance1.update(target_range, [[(new_date + timedelta(days=i)).strftime("%m/%d/%Y") for i in range(1,6)]])


#Copy Paste to desired ranges
request_body = {
    'requests': [
        {
            'copyPaste': {
                'source' : {
                    'sheetId': 1110613513,
                    'startRowIndex':17,
                    'endRowIndex': 26,
                    'startColumnIndex':3,
                    'endColumnIndex': 4 
                },
                'destination': {
                    'sheetId': 1110613513,
                    'startRowIndex': 17,
                    'endRowIndex':26,
                    'startColumnIndex':4,
                    'endColumnIndex': 9
                },
                'pasteType': 'PASTE_VALUES'
            }
        },
        {
            'copyPaste': {
                'source' : {
                    'sheetId': 1110613513,
                    'startRowIndex':27,
                    'endRowIndex': 35,
                    'startColumnIndex':3,
                    'endColumnIndex': 4 
                },
                'destination': {
                    'sheetId': 1110613513,
                    'startRowIndex': 27,
                    'endRowIndex':35,
                    'startColumnIndex':4,
                    'endColumnIndex': 9
                },
                'pasteType': 'PASTE_VALUES'
            }
        },
        {
            'copyPaste': {
                'source' : {
                    'sheetId': 1110613513,
                    'startRowIndex':37,
                    'endRowIndex': 41,
                    'startColumnIndex':3,
                    'endColumnIndex': 4 
                },
                'destination': {
                    'sheetId': 1110613513,
                    'startRowIndex': 37,
                    'endRowIndex':41,
                    'startColumnIndex':4,
                    'endColumnIndex': 9
                },
                'pasteType': 'PASTE_VALUES'
            }
        },
        {
            'copyPaste': {
                'source' : {
                    'sheetId': 1110613513,
                    'startRowIndex':41,
                    'endRowIndex': 49,
                    'startColumnIndex':3,
                    'endColumnIndex': 4 
                },
                'destination': {
                    'sheetId': 1110613513,
                    'startRowIndex': 41,
                    'endRowIndex':49,
                    'startColumnIndex':4,
                    'endColumnIndex': 9
                },
                'pasteType': 'PASTE_VALUES'
            }
        }
    ]
}


#Update 
Spreadsheet.batch_update(request_body)
print("Update successful!")







print(sheet_instance1.col_count)
