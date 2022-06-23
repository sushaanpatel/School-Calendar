import os.path
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def subject(sub, start, end):
    if sub == 'maa':
        return {
            'summary': 'Math AA HL Batch-2',
            'location': 'Room number - 226',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            }
        }
    elif sub == 'll':
        return {
            'summary': 'Language SL Batch-2',
            'location': 'Room number - 222',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            }
        }
    elif sub == 'bm':
        return {
            'summary': 'Business Management SL Batch-1',
            'location': 'Room number - 226',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            }
        }
    elif sub == 'cs':
        return {
            'summary': 'Computer Science HL',
            'location': 'Room number - 226',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            }
        }
    elif sub == 'phy':
        return {
            'summary': 'Physcis HL',
            'location': 'Room number - 221',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            }
        }
    elif sub == 'fre':
        return {
            'summary': 'French Batch-1',
            'location': 'Room number - 227',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            }
        }

# start maa - datetime.datetime(2022, 6, 22, 14, 50, 0).isoformat()
# end maa - datetime.datetime(2022, 6, 22, 15, 35, 0).isoformat()

def main():
    #creds and calendar service
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    
    #date variables
    start_date = datetime.datetime(
    2022, 6, 9, 00, 00, 00, 0).isoformat() + 'Z'
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
                
                # LL
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('ll', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 55, 0).isoformat())).execute()
                
                #BM
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('bm', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 10, 15, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 0, 0).isoformat())).execute()
                
                #Phy
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('phy', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 0, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 45, 0).isoformat())).execute()
                
                #MAA
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('maa', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 50, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 15, 35, 0).isoformat())).execute()
            elif i['summary'] == 'D2':
                temp = i['start']['date']
                date = temp.split('-')
                
                #MAA
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('maa', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 55, 0).isoformat())).execute()
                
                #Phy
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('phy', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 5, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 50, 0).isoformat())).execute()
                
                #LL
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('ll', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 55, 0).isoformat())).execute()
                
                #LL
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('ll', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 0, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 45, 0).isoformat())).execute()
                
                #French
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('fre', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 50, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 15, 35, 0).isoformat())).execute()
            elif i['summary'] == 'D3':
                temp = i['start']['date']
                date = temp.split('-')
                
                #BM
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('bm', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 10, 15, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 0, 0).isoformat())).execute()
                
                #BM
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('bm', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 5, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 50, 0).isoformat())).execute()
                
                #phy
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('phy', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 55, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 12, 40, 0).isoformat())).execute()
                
                #fre
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('fre', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 55, 0).isoformat())).execute()
                
                #CS
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('cs', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 0, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 45, 0).isoformat())).execute()
                
                #MAA
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('maa', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 50, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 15, 35, 0).isoformat())).execute()
            elif i['summary'] == 'D4':
                temp = i['start']['date']
                date = temp.split('-')
                
                #BM
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('bm', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 55, 0).isoformat())).execute()
                
                #CS
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('cs', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 5, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 50, 0).isoformat())).execute()
                
                #MAA
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('maa', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 55, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 12, 40, 0).isoformat())).execute()
                
                #French
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('fre', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 55, 0).isoformat())).execute()
                
                #Phy
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('phy', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 0, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 45, 0).isoformat())).execute()
                
                #Phy
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('phy', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 50, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 35, 0).isoformat())).execute()                
            elif i['summary'] == 'D5':
                temp = i['start']['date']
                date = temp.split('-')
                
                # LL
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('ll', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 9, 55, 0).isoformat())).execute()
                
                #CS
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('cs', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 10, 15, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 00, 0).isoformat())).execute()
                
                #CS
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('cs', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 5, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 50, 0).isoformat())).execute()
                
                #BM
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('bm', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 55, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 12, 40, 0).isoformat())).execute()
                
                #French
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('fre', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 0, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 14, 45, 0).isoformat())).execute()
            elif i['summary'] == 'D6':
                temp = i['start']['date']
                date = temp.split('-')
                
                #MAA
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('maa', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 10, 15, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 0, 0).isoformat())).execute()
                
                #MAA
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('maa', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 5, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 50, 0).isoformat())).execute()
                
                #LL
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('ll', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 55, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 12, 40, 0).isoformat())).execute()
                
                #CS
                service.events().insert(calendarId='c_va10iprivobsv1act5kehp4mas@group.calendar.google.com', body=subject('cs', datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 10, 0).isoformat(), datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 13, 55, 0).isoformat())).execute()
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

