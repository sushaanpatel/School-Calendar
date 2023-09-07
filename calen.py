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
calendarid = "c_ed6cdabd14779b1f159f50c6de24fbcacf53d0c46bd9bc834d44d9dbc3ff1660@group.calendar.google.com"

def event(sub, date, slotnum):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    slottime = {
        1:[9, 10, 10, 00],
        2:[10, 20, 11, 10],
        3:[11, 20, 12, 10],
        4:[12, 20, 13, 10],
        5:[13, 45, 14, 35],
        6:[14, 45, 15, 35]
    }
    service.events().insert(calendarId=calendarid, body=subject(sub, datetime.datetime(int(date[0]), int(date[1]), int(date[2]), slottime[slotnum][0], slottime[slotnum][1], 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), slottime[slotnum][2], slottime[slotnum][3], 0).isoformat())).execute()


def main():
    #creds and calendar service
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    
    #date variables
    start_date = datetime.datetime(
    2023, 6, 26, 00, 00, 00, 0).isoformat() + 'Z'
    end_date = datetime.datetime(2024, 5, 30, 23, 59, 59).isoformat() + 'Z'
    
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
                
                event('tok', date, 1)
                event('fre', date, 2)
                event('fre', date, 3)
                event('ps', date, 4)
                event('free', date, 5)
                event('bm', date, 6)
                
            elif i['summary'] == 'D2':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('phy', date, 1)
                event('ps', date, 2)
                event('cs', date, 3)
                event('cs', date, 4)
                event('ll', date, 5)
                event('maa', date, 6)
                
                
            elif i['summary'] == 'D3':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('ps', date, 1)
                event('cs', date, 2)
                event('tok', date, 3)
                event('maa', date, 4)
                event('bm', date, 5)
                event('bm', date, 6)
                
            elif i['summary'] == 'D4':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('fre', date, 1)
                event('bm', date, 2)
                event('phy', date, 3)
                event('phy', date, 4)
                event('ll', date, 5)      
                event('free', date, 6)
                       
            elif i['summary'] == 'D5':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('phy', date, 1)
                event('ll', date, 2)
                event('maa', date, 3)
                event('free', date, 4)
                event('cs', date, 5)
                event('cas', date, 6)
                
            elif i['summary'] == 'D6':
                temp = i['start']['date']
                date = temp.split('-')
                
                event('ps', date, 1)
                event('fre', date, 2)
                event('maa', date, 3)
                event('ll', date, 4)
                event('free', date, 5)
                event('free', date, 6)
                
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
            
auth()

