# League,Team,Players
## About project
* LTP is an application where you can find info about the most popular football leagues, teams playing in it and players of a given team.
* What's more, you can also add more league, more teams and players!
* One of an interesting possibility is also transferring players between clubs that already existing in the database.

## Technologies used in the project
**Python 🐍**

- FastAPI
- SQLAlchemy

## Setup

After cloning the repository you need to install requirements.txt in main folder:

<sub>To install you should have Python 3.9</sub>
```
pip install -r requriments.txt 
```

## Simple data

In ltp.db you already have some simple data (3 leagues, 3 clubs and 4 players)

## Local server

To start your local web server type:

```
 uvicorn main:app --reload
```

## Remote server

You can also use a [Remote server](https://2sr7j0.deta.dev/).

## Configuration on website

To create, delete and make other operations, you can get access to it by login with:
- email: `admin@example.com` with password `admin`

Or create new user in [Docs](https://2sr7j0.deta.dev/docs).

### Author

*Radosław Bujny*