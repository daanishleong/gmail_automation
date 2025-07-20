# gmail_automation

**DISCLAIMER:** I do not take credit for this code. The code shown is based of the quickstart code from the Google API guide. I have merely modified the example to suit my own needs.

A Python Script to automate marking unread messages to read using the Gmail API.

Overview:
This project was my first hands-on experience working with APIs. Using Google API services, I built a Python script to access my inbox and change unread labels to read - helping me streamline my inbox management

Features:
- Connects to Gmail using Google API
- Accesses and filters out inbox messages based on labelIds
- Changes labelIds from 'UNREAD' to 'READ'

Technology used:
- Language: Python
- Libraries: os, google,  googleapiclient, google_auth_oauthlib

Motivations:
**"You really need to clean up your inbox. Over 1000 unread messages?!"**
That was a comment by my dad one day. While Gmail has a built in function to help achieve this, it gave an opportunity for me to explore how APIs can help automate real-life problems. This eventually led me down the rabbit hole into the world of APIs and how we can communicate with external services via our code.

Challenges Faced:
1. Unfamiliar with APIs and OAuth
     - No prior experice working with APIs or OAuth authentication
     - Overwhelmed by volume of extensive documentation and flows
     - Learnt the importance of reading official online documentation and breaking down complex processes into smaller experiments
2. Limited scope
   - Script only works for one Gmail account per authentication session
   - Realized that in order to scale to multiple accounts, proper methods of storing unique token.json files must be implemented

Learning Outcomes:
- Gained hands-on experience working with APIs (Google Gmail API)
- Understood how OAuth2 authentication works in a practical setting
- Understood how to read an apply official documentation
- Discovered how APIs can be used for personal automation
- Learnt about API potential in Chemical Engineering applications (automating lab data into a Google Sheet)
   
