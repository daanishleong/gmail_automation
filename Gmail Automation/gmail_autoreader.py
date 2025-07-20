import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#Refer to https://developers.google.com/workspace/gmail/api/guides
#Refer to quickstart guide. Code is based on there with changes to label unread ids to read ids instead of returning only labels
#Step 1: Authentication and Authorization: setiing up OAuth2 and scope 
#OAuth2 is done alrd on the Google Cloud Console
#Scope: https://mail.google.com/ used to Read, compose, send, and permanently delete all your email from Gmail

scopes = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    creds = None
    #Checks if from os.path if a token.json file exists to be used in auth
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    else:
        if not creds or creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request()) #Request a refresh of access tokens
            else: #If token cannot be refreshed, we re-login to get a new token
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
                creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        client = build('gmail', 'v1', credentials=creds)
        result = client.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
        messages = result.get('messages', [])

        if not messages:
            return print('No unread messages')
        
        print(f'Found {len(messages)} unread messages.')
        query = input('Would you like to proceed? <Y/N>: ').lower().strip()

        if query == 'y':
            print('Beginning to mark unread messages...')
            for msg in messages:
                client.users().messages().modify(userId='me', id=msg['id'], body={'removeLabelIds':['UNREAD']}).execute()
            print(f'All {len(messages)} messages have been read')
        elif query == 'n':
            return print('Terminating...')
    
    except HttpError as error:
        print(f'An error has occurred: {error}')

if __name__ == '__main__':
    main()
    


    
