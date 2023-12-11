import praw
import requests
from datetime import datetime
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

# get the vars
load_dotenv()

ID = os.environ.get("ID")
SECRET = os.environ.get("SECRET")
USERAGENT = os.environ.get("USERAGENT")
PWR = os.environ.get("PWR")
USER = os.environ.get("USER")


def scrape_top_of_day(sub, output_folder=".\cats"):
    # Initialize the Reddit API client
    reddit = praw.Reddit(client_id=ID,
                         client_secret=SECRET,
                         user_agent=USERAGENT,
                         password=PWR,
                         username=USER)
    print("Logged in to : ", reddit.user.me())
    subreddit = reddit.subreddit(sub)
    day_tops = subreddit.top(time_filter='day', limit=100)

    for day_top in day_tops:
        if day_top.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
            image_url = day_top.url            
            img_path = download_image(image_url, output_folder)
            return img_path
        else:
            print("Top post of the day is not an image.")         
            
def getDate():
    return datetime.now().strftime("%d%m")

def download_image(url, output_folder="\pics"):
    os.makedirs(output_folder, exist_ok=True)
    image_response = requests.get(url)
    if image_response.status_code == 200:
        _ , extension = os.path.splitext(os.path.basename(urlparse(url).path))
        filename = f"kitty{getDate()}{extension}"
        image_filename = os.path.join(output_folder, filename)
        with open(image_filename, 'wb') as image_file:
            image_file.write(image_response.content)
        print(f"Image downloaded and saved as {image_filename}")
        return image_filename
    else:
        print(f"Failed to download image from {url}")
        
        
        
if __name__ == '__main__':
    sub = "IllegallySmolCats"
    img = scrape_top_of_day(sub)
    print(img)
