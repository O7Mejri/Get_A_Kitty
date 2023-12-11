from scrape import scrape_top_of_day
from send_email import sendMail

import os

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

if __name__ == '__main__':
    sub = "blackcats"
    img = scrape_top_of_day(sub)
    print(img)
    rec = "oussama326mejri@gmail.com"
    sendMail(rec, img)
