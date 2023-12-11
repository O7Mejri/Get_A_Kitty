# Default sender
# uses SSL encryption

import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime
import os
from dotenv import load_dotenv

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

# get the vars
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PWE = os.environ.get("PWE")
SMTP_SERVER = "smtp.gmail.com"
PORT = 465

# define the function
def sendMail(rec, img_path):
    context = ssl.create_default_context()

    rec = rec
    sbj = "YOU BEING STUPID"
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"I will later provide my resons \n\n Current Date and Time: {current_datetime}"

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = rec
    msg["Subject"] = sbj

    msg.attach(MIMEText(body, "plain"))

    kitty_path = img_path
    name = os.path.basename(kitty_path)
    with open(kitty_path, "rb") as pic:
        part_pic = MIMEBase("application", "octet-stream")
        part_pic.set_payload(pic.read())

    encoders.encode_base64(part_pic)
    part_pic.add_header(
        "Content-Disposition",
        f"attachment; filename= {name}"
    )

    msg.attach(part_pic)
    text = msg.as_string()

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(EMAIL, PWE)
        server.sendmail(EMAIL, rec, text)
        print("EMAIL SENT!")


# Running

if __name__ == '__main__':
    rec = "oussama326mejri@gmail.com"
    sendMail(rec)