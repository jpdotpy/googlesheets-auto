# googlesheets-auto
First Ever Python Script

# This is a Google Sheets automation script made specifically for updating our businesses' weekly KPI sheet

# Google Sheets Automation Script

This Python script automates tasks in Google Sheets using the gspread library. The script performs the following actions:

1. **Initialize Google Sheets API:**
   - Connects to Google Sheets using OAuth2 credentials.

2. **Access Google Sheets:**
   - Retrieves the instance of the target Google Sheets document by its URL.

3. **Update Values:**
   - Updates specified ranges with 0 values.
   - Updates a specific cell (D17) with a new date, calculated as a week from the current date.
   - Updates a target range (E17:I17) with new dates calculated from the updated cell.

4. **Copy-Paste to Desired Ranges:**
   - Copies and pastes values from one range to another in the same sheet.

5. **Batch Update:**
   - Executes a batch update, copying and pasting values to multiple specified ranges.

## Prerequisites

Before running the script, ensure you have the required dependencies installed and the necessary credentials available.

To run the script

```bash
pip install gspread pandas oauth2client
```

To run the script use:  

```bash
python gsheetskpiauto.py
```

For access to the actual sheet I use to run this script feel free to dm me here or on X @jphoopla__



