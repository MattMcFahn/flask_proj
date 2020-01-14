import smtplib
import config

def email_comments(email_target, comments):
    """
    (str, str) -> email
    Emails a user noting that their comments have been
    noted, and giving them a copy of their submission.
    """
    # NOTE - I should really reformat this as layout is awful
    
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # Connect to gmail stmp provider, 'smtp.gmail.com'
    smtpObj.ehlo() # Say "hello" to the server
    smtpObj.starttls() # Connect to port 587 (TLS encryption)
    secret_password = config.passwords['gmail']
    smtpObj.login(config.emails['gmail'], secret_password) #Log in to access email
    #Send the mail
    smtpObj.sendmail(from_addr=config.emails['gmail'],
                     to_addrs = email_target,
                     msg = '''Subject: Submission to my webpage\n
                     Hi! \n\n
                     Thank you for submitting a message on my webpage. \n
                     I will try and get back to you.\n\n\n

                     --- Copy of submission ---\n\n
                     Comments: '{}' '''.format(comments))
