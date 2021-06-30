import imaplib
import re, os 
from time import sleep

#datos
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('', '')
imap.select('Inbox')

def GetMsgId(Mail, path):
    typ, data = imap.search(None,'FROM', Mail)
    f = open(path+"MsgId-"+Mail+".txt","a")

    for num in data[0].split():
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        MailExtracted= data[0][1].decode()
        MailExtracted=MailExtracted.replace("Message-ID:", "")
        MailExtracted=MailExtracted.replace(">", "")
        MailExtracted=MailExtracted.replace("<", "")
        MailExtracted=MailExtracted.replace("Message-Id:", "")
        MailExtracted=MailExtracted.strip()
        f.write(MailExtracted+'\n')
        print(MailExtracted)



def GetFrom(Mail, path):
    typ, data = imap.search(None,'FROM', Mail)
    f = open(path+"From-"+Mail+".txt","a")

    for num in data[0].split():
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
        MailExtracted= data[0][1].decode()
        MailExtracted=MailExtracted.replace("From:", "")
        MailExtracted=MailExtracted.replace(">", "")
        MailExtracted=MailExtracted.replace("<", "")
        MailExtracted=MailExtracted.replace(Mail, "")
        MailExtracted=MailExtracted.replace("From:", "")
        MailExtracted=MailExtracted.strip()
        f.write(MailExtracted+'\n')
        print(MailExtracted)


def GetDate(Mail, path):
    typ, data = imap.search(None,'FROM', Mail)
    f = open(path+"Date-"+Mail+".txt","a")

    for num in data[0].split():
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (DATE)])')
        MailExtracted= data[0][1].decode()
        MailExtracted=MailExtracted.replace("Date:", "")
        MailExtracted=MailExtracted.replace(">", "")
        MailExtracted=MailExtracted.replace("<", "")
        MailExtracted=MailExtracted.replace("Date:", "")
        MailExtracted=MailExtracted.replace("(UTC)", "")
        MailExtracted=MailExtracted.strip()
        f.write(MailExtracted+'\n')
        print(MailExtracted)

def Receiveds (Mail):
    Mail = Mail.strip()
    Mail = re.split("\s", Mail)
    indice = 0
    lines = []
    count = 0
    print(Mail)
    for i in range(0, len(Mail)):
        if Mail[i] == 'Received:' and count == 0:
            indice = i
            count = count+1
        elif Mail[i] == 'Received:' and count > 0:
            lines.append(Mail[indice:i])
            indice = i
        if i == len(Mail)-1:
            lines.append(Mail[indice:i])
    RecStr, SecondToLastRec = []
    for i in range( 0, len(lines)):
        RecStr.append([])
        for j in range(0, len(lines[i])):
            if lines[i][j] != '':
                if len(RecStr[i])== 0:
                    RecStr[i]= str(lines[i][j])+ " " 
                else:
                    RecStr[i]= str(RecStr[i])+  str(lines[i][j])+ " " 
    FirstRec = RecStr[0]
    if len(RecStr) == 2:
        SecondToLastRec = RecStr[1]
    elif len(RecStr) >= 3:
        SecondToLastRec = RecStr[len(RecStr)-2]
    else:
        print("ERROR")
    

        
                
    print("//////////////////////////////")
    print(RecStr)
    print("//////////////////////////////")
    return FirstRec, SecondToLastRec
    #receives = []

def GetReceiveds(Mail, path):
    typ, data = imap.search(None,'FROM', Mail)
    f = open(path+"Received-"+Mail+".txt","a")

    for num in data[0].split():
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        MailExtracted= data[0][1].decode()
        v1 , v2 = Receiveds(MailExtracted)
        MailExtracted=MailExtracted.replace(">", "")
        MailExtracted=MailExtracted.replace("<", "")
        MailExtracted=MailExtracted.strip()
        #Data = Receiveds(MailExtracted)
        f.write(MailExtracted+'\n')
        print(MailExtracted)
        sleep(2)



ThePath = "Data/"
correos = ['no-reply@digital.gob.cl','no-reply@e.udemymail.com','googleplay-noreply@google.com','no-reply@mail.instagram.com', 'noreply@medium.com']

for element in range(len(correos)):
    #msg=GetMsgId(correos[element], ThePath)
    #xFrom=GetFrom(correos[element], ThePath)
    #Date=GetDate(correos[element], ThePath)
    TheReceiveds = GetReceiveds(correos[element], ThePath)



imap.close()