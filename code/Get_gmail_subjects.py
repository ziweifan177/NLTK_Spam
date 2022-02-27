import imaplib 
import re
import csv 
import path_config

csv_path = path_config.csv_path

header = ['Subject', 'spam']
username = 'youremail@gmail.com' 
password = 'Yourpassword' 
url = "imap.gmail.com" 
email_account = imaplib.IMAP4_SSL(url) 
email_account.login(username, password) 
email_account.select() 
typ, data = email_account.search(None, 'ALL') 

all_subjects = []

for num in data[0].split(): 
    typ, data = email_account.fetch(num, '(BODY[HEADER.FIELDS (FROM TO SUBJECT)])') 
    splits = data[0][1].split(b'\r\n')
    print('~~~', splits)
    
    subject_ele= [ele for ele in splits if b'Subject:' in ele]
    
    if subject_ele:
        subject = subject_ele[0].decode("utf-8").replace('Subject: ', '')
        print(subject)
    else:
        continue

    row = [subject, '']
    all_subjects.append(row)

print(all_subjects)
email_account.close() 
email_account.logout() 


with open(csv_path, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(all_subjects)
