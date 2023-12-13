# Get_A_Kitty

Get_A_Kitty is a Python project that scrapes Reddit for cat pictures and sends them in an email daily. It utilizes PRAW for Reddit scraping, Python's email library for sending emails, and GitHub Actions for scheduling and automation.

## Usage

To use this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/Get_A_Kitty.git
   cd Get_A_Kitty

2. **Install Dependencies:**
   ```bash
    pip install -r requirements.txt
   
3. **Modify the Main File:**
   - recipient_email: Set this to the email address where you want to receive cat pictures.
   - subreddit: Set this to the subreddit from which you want to scrape cat pictures.

3. **Set GitHub Secrets:**
    In your GitHub repository, go to "Settings" -> "Secrets" and add the following secrets:
    
    - ID: Your Reddit API client ID.
    - SECRET: Your Reddit API client secret.
    - USERAGENT: Your Reddit API user agent.
    - USER: Your Reddit account username
    - PWR: Your Reddit account password
    - EMAIL: Your email account username.
    - PWE: Your email account password.
   
**Contributing**
  Feel free to contribute to this project by opening issues or pull requests. Your contributions are welcome
    
