import pandas as pd
from datetime import datetime
import smtplib
import os
os.chdir(r"E:\Python_VSC\PPP\Birthday_Wisher")
os.mkdir("testing")

GMAIL_ID = 'chaudharyanshirsingh2050@gmail.com'
GMAIL_PSWD = '9045441245'
def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()

if __name__ == "__main__":
   # f =  open('Birthdays.xlsx','rb')
    df = pd.read_excel('Birthdays.xls')
    # print(df)
    today = datetime.now().strftime("%d-%m")
    print(today)

    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        # print(item['Birthday'])
        bday = item['Birthday']
        #print(bday)
        if (today == bday):
            sendEmail(item['Email'], "Happy Birthday"+item['Name'], item['Dialogue'])
