# CS50 Final Project - Ink

The project is a website, called Ink, where people can find jobs for themself or post jobs to hire someone. I chose this kind of website because I thought that it would be interesting and that it would help me learn a lot, which it did.

### Technology Used: 

- HTML
- CSS
- JavaScript
- Python
- Flask
- Jinja
- SQL
- SQLite
- Bootstrap

## How Ink works

### Register and Log in

To **register**, you need to give the following information:

- Username
- Password (and its confirmation)
- First, middle and/or last name.
- Profession
- Skills (can insert only 6 skills at max, separating with a comma between each skill)
- Email

Then, to **log in**, you only need to insert your username and password.

### Profile

In **profile**, there just a few things you can do, such as:

- Edit your information
- Edit and reset your profile picture
- Change password
- Change username

### Search

In **search**, you can look other people profiles, in a card format. The card show their name, profession, skills and email, so you can contact them.

### Jobs

In **jobs**, you can look for a job to do or post your own job for somebody else to do. To post a job, you need to give the following information:

- Title of the job
- What the worker will need to know to do the job
- Description of the job
- Deadline of the job
- Email for contact

## How to launch the website

1. Make sure you have visual studio code downloaded with open with code allowed
2. Clone the repository
3. Go to the `Ink Project` folder
4. Click with the right button on the `Ink` folder, then click in `Open with Code`
5. Open the VS Code terminal (Windows: `Ctrl + Shift + '`
6. On the terminal of VS CODE, type `python -m flask run`
7. Open the link provided on the terminal
8. To stop, press `Ctrl + C`
