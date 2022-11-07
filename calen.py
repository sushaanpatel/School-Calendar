import os.path
import datetime
from model import subject
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

# start maa - datetime.datetime(2022, 6, 22, 14, 50, 0).isoformat()
# end maa - datetime.datetime(2022, 6, 22, 15, 35, 0).isoformat()
calendarid = "c_sb0am0avhl5pstf3ilk30s0630@group.calendar.google.com"

def event(sub, date, slotnum):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    slottime = {
        1:[9, 20, 10, 40],
        2:[11, 5, 11, 50],
        3:[12, 0, 13, 0],
        4:[13, 30, 14, 30],
        5:[14, 40, 15, 35]
    }
    service.events().insert(calendarId=calendarid, body=subject(sub, datetime.datetime(int(date[0]), int(date[1]), int(date[2]), slottime[slotnum][0], slottime[slotnum][1], 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), slottime[slotnum][2], slottime[slotnum][3], 0).isoformat())).execute()


def main():
    #creds and calendar service
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    
    #date variables
    start_date = datetime.datetime(
    2022, 11, 7, 00, 00, 00, 0).isoformat() + 'Z'
    end_date = datetime.datetime(2023, 6, 1, 23, 59, 59).isoformat() + 'Z'
    
    #all events in 2022 to 2023
    calendar = service.events().list(
    calendarId='fountainheadschools.org_0emneups26ttn44bkg00lpji7s@group.calendar.google.com', timeMin=start_date, timeMax=end_date, singleEvents=True, orderBy='startTime').execute()
    items = calendar.get('items',[]) 
    for i in items:
        try:
            # print(i['start'])
            if i['summary'] == 'D1':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('fre', date, 1)
                event('ps', date, 2)
                event('tok', date, 3)
                event('cs', date, 4)
                event('phy', date, 5)
                
            elif i['summary'] == 'D2':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('free', date, 1)
                event('bm', date, 2)
                event('maa', date, 3)
                event('ll', date, 4)
                event('cas', date, 5)
            elif i['summary'] == 'D3':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('cs', date, 1)
                event('bm', date, 2)
                event('tok', date, 3)
                event('free', date, 4)
                event('maa', date, 5)
            elif i['summary'] == 'D4':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('phy', date, 1)
                event('ps', date, 2)
                event('free', date, 3)
                event('cs', date, 4)
                event('fre', date, 5)             
            elif i['summary'] == 'D5':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('ll', date, 1)
                event('bm', date, 2)
                event('phy', date, 3)
                event('maa', date, 4)
                event('free', date, 5)
            elif i['summary'] == 'D6':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('ps', date, 1)
                event('tok', date, 2)
                event('ll', date, 3)
                event('fre', date, 4)
                event('maa', date, 5)
        except Exception as e:
            print(e)
    

        
def auth():
    # Google login and Oauth
    creds = None
    if os.path.exists('token.json'):
        main()
    else:
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'creds.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
            
auth()

