import smtplib
try:
    import config
except:
    pass

import os

def email():
    """
    Retreive email
    """
    try:
        from config import emails
        from_email_add = emails['gmail']
    except ImportError:
        from_email_add = os.environ['GMAIL']
    return from_email_add


def email_password():
    """
    Retreive password based on os
    """
    try:
        from config import passwords
        gmail_password = passwords['gmail']
    except ImportError:
        gmail_password = os.environ['GMAIL_PASSWORD']
    return gmail_password

def email_comments(email_target, comments):
    """
    (str, str) -> email
    Emails a user noting that their comments have been
    noted, and giving them a copy of their submission.
    """

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # Connect to gmail stmp provider, 'smtp.gmail.com'
    smtpObj.ehlo() # Say "hello" to the server
    smtpObj.starttls() # Connect to port 587 (TLS encryption)

    from_addr = email()
    secret_password = email_password()
    smtpObj.login(config.emails['gmail'], secret_password) #Log in to access email
    # - Write message
    msg = '''Subject: Submission to my webpage\n
             Hi! \n\n
             Thank you for submitting a message on my webpage. \n
             I will try and get back to you.\n\n\n

             --- Copy of submission ---\n\n
             Comments: '{}' '''.format(comments)
    # - Write message

    #Send the mail
    
    smtpObj.sendmail(from_addr=from_addr,
                     to_addrs = email_target,
                     msg = msg)