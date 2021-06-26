import imaplib, emai, re, smtplib, datetime, time
from typing import List, Set, Dict, Tuple, Optional
from dateutil import parser

user = ''
passwd= ''
imap_url= ''


def set_connection(imap_url, user, password):
    """Establece la conexion con el correo
    
    Args:
        imap_url (str): Dirección del servidor de correos
        user (str):
        password (str):

    Returns:
        imaplib.IMAP4_SSL:
    """
    imap = imaplib.IMAP4_SSL=imap_url
    imap.login(user,password)
    return imap

def getMailRegexDate(route):
    f1 = open(route, 'r')
    Lines = f1.readlines()
    list =[]
    for line in Lines:
        el = line.split(",")
        el[-1] = el[-1].strip()
        el[-1] = parser.parse(el[-1])
        list.append(tuple(el))
        print(list)
    return list

def getMsgId(imap, DirMail, pathArch = None):
    """
    Args:
        imap (imaplib.IMAP4_SSL): Objeto con el que se establecio la conexion
        DirMail (str): Direcion del mail para filtrar correos
        file_path (str, optional): direccion de archivo para guardar las IDs de los correos. Defaults to None.

    """
    estado, mssges = imap.select('INBOX')
    print(f"{DirMail}\n\tObteniendo mails...")
    estado, mailsId = imap.search(None,f'(FROM"{DirMail}")')
    mailsId = str(mailsId)[3:-2].rsplit(' ')
    mssgIds= []
    if pathArch:
        outFile= open('Message-IDs.txt','w')
        for id in mailsId:
            res, msgs = imap.fetch(id, '(RFC822)')
            for msgData in msgs:
                if isinstance(msgData, tuple):
                    message = email.message_from_bytes(msgData[1])
                if pathArch:
                    outFile.write(message['Message-ID'][1:-1]+','+message['Date']+'\n')
                msg_ids.append((id,message['Message-ID'][1:-1],message['Date']))
        if pathArch:
            outFile.close()
        print(f'{DirMail}:\n\tCantidad de correos obtenidos:{len(mssgIds)}') 
    return msgsIds

def checkRegex(msgsId, regExpression, Date):
    """
    Args:
        msgsId list[ tuple(str, str)]: [description]
        regExpression (str):
        date (datetime):
    """
    for el in msgsId:
        mailDate= parser.parse(el[-1]).date()
        if mailDate > date.date():
            print("Regex desactualizado para: ", el)
        elif re.search(regExpression, el[1]):
            print("Aprobado:" , el)
        else:
            print("Hay una posible suplantación de identidad:", el)
    pass




if __name__ == "__main__":
      imap = set_connection(imap_url, user, passwd) # establece la conexion
      mail_regex = get_mail_regex_date('correos_regex.txt') # obtiene la expresion rgular desde un archivo
      for elemento in mail_regex: # Por cada expresion regular 
          msg_ids = get_msg_id(imap, elemento[0]) # Por cada elemento entrega la direccion
          check_regex(msg_ids, elemento[1], elemento[2]) # Entrega los mensajes con ID, la expresion regular y la fecha de la expresion
