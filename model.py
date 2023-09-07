def subject(sub, start, end):
    if sub == 'maa':
        return {
            'summary': 'Math AA HL Batch-1',
            'location': 'Room number - 126',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'll':
        return {
            'summary': 'Language SL Batch-2',
            'location': 'Room number - 125',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'bm':
        return {
            'summary': 'Business Management SL Batch-1',
            'location': 'Room number - 124',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'cs':
        return {
            'summary': 'Computer Science HL',
            'location': 'Room number - 128',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'phy':
        return {
            'summary': 'Physcis HL',
            'location': 'Room number - 127',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'fre':
        return {
            'summary': 'French Batch-2',
            'location': 'Room number - 126',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'free':
        return {
            'summary': 'Free Slot',
            'location': 'Basketball court/Grounds/Senoir Library',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'tok':
        return {
            'summary': 'TOK',
            'location': 'Room number - 121',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'cas':
        return {
            'summary': 'CAS/EE',
            'location': 'Room number - 128',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    elif sub == 'ps':
        return {
            'summary': 'PS',
            'location': 'Grounds',
            'start': {
                'dateTime': start,
                'timeZone': 'GMT+05:30',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'GMT+05:30',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
