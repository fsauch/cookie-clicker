# Cookie Clicker by Team POGGERS

**Roster/Roles**
- Kelvin Ng:
  - Project Manager
  - Update README, make sure design doc is current, manage devlog
  - Minor coding tasks if necessary
- Tanzim Elahi
  - Backend implementation of databases and interactions with frontend
  - Help with frontend (templates, routes, styling with Bootstrap)
- Kevin Li
  - Interfacing with the API to retrieve the necessary data
  - Backend interactions with the frontend cookie clicker
  - Backend implementation of accounts
- Justin Shaw
  - JavaScript necessary for clicking the cookie and purchasing perks
  - Frontend (templates, routes, styling with Bootstrap)

## Website Description
Leaderboard data is fetched from the [speedrun.com REST API](https://docs.google.com/document/d/1Hk-0V1E2hvxjx1BrCcwk33yCHaMnbO_hza4GzxjVcZM). We will plaster that data as a table on our website's leaderboards page, so that users may compare their accomplishments with those from all over the world.

This website is a recreation of [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) with the skills we've learned over the course of this semester. Clicks will function as the currency of this game. Currency may be used to purchase perks such as autoclickers. An account will be required so that progress can be saved. There will also be a leaderboards page so that you can compare your ability with others. One section is for comparing stats with other users of the website, and another will be for comparing with top players, whose data will be sourced from the speedrun.com API.

## Instructions for running this project

**Dependencies**

You must install the pip modules listed in the /doc/requirements.txt file. To do so, install them in a Terminal with:
```bash
pip install -r <location of requirements.txt file>
```

The -r flag is necessary to distinguish it from a typical pip install. Without the -r, pip will look for a package online called "requirements.txt". That is obviously not desirable.

**Create the database**

Load the dump

```bash
mysql < dump.sql
```

Information to connect to the DB : `database.cfg`

```bash
python3 utl/db_creation.py
```

**Run the program**

After installing the required dependencies, all you need to do to run the program is to type into a terminal session:
```bash
python3 app.py
```
*Again, remove the 3 after the "python" if necessary.*
