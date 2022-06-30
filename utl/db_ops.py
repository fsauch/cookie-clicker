from datetime import datetime #for timestamp
from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)
app.config.from_pyfile('../database.cfg')

mysql.init_app(app)

def accountExists(username):
    db = mysql.connect()
    c = db.cursor()

    c.execute("SELECT * FROM accounts WHERE username = (%s)", (username,))
    rowCount = 0
    for row in c:
        rowCount += 1

    db.close()

    if (rowCount == 1):
        return True

    return False

def addAccount(username, password):
    db = mysql.connect()
    c = db.cursor()

    c.execute(
        "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (username, password, 0, 0, 0, 0, 0, 0, 0, 0)
    )

    db.commit()
    db.close()

def authenticate(username, password):
    db = mysql.connect()
    c = db.cursor()

    c.execute("SELECT * FROM accounts WHERE username = (%s)", (username,))
    rowCount = 0
    for row in c:
        rowCount += 1

    db.close()
    if (rowCount != 1):
        return False

    return password == row[1]

def changepw(username, password):
    db = mysql.connect()
    c = db.cursor()

    c.execute("UPDATE accounts SET password = (%s) WHERE username = (%s)", (password, username,))

    db.commit()
    db.close()

def reg_clicks(username, num_clicks):
    db = mysql.connect()
    c = db.cursor()

    c.execute("UPDATE accounts SET clicks = clicks + (%s) WHERE username = (%s)", (num_clicks, username,))
    c.execute("UPDATE accounts SET total_clicks = total_clicks + (%s) WHERE username = (%s)", (num_clicks, username,))

    db.commit()
    db.close()

def get_clicks(username):
    db = mysql.connect()
    c = db.cursor()

    c.execute("SELECT clicks FROM accounts WHERE username = (%s)", (username,))
    cookies = c.fetchall()[0][0]
    c.execute("SELECT total_clicks FROM accounts WHERE username = (%s)", (username,))
    total_cookies = c.fetchall()[0][0]

    db.close()
    return cookies, total_cookies

def get_trial_data(username):
    db = mysql.connect()
    c = db.cursor()

    c.execute("SELECT trial_15_sec FROM accounts WHERE username = (%s)", (username,))
    trial_15_sec = c.fetchall()[0][0]
    c.execute("SELECT trial_30_sec FROM accounts WHERE username = (%s)", (username,))
    trial_30_sec = c.fetchall()[0][0]

    db.close()
    return trial_15_sec, trial_30_sec

# Will necessitate JS that prevents buying something you already have + don't have the cookies for
def buy_perk(username, id, price):
    db = mysql.connect()
    c = db.cursor()

    if (int(id) == 0):
        c.execute("UPDATE accounts SET perk_0_lvl = perk_0_lvl + 1 WHERE username = (%s)", (username,))

    if (int(id) == 1):
        c.execute("UPDATE accounts SET perk_1_lvl = perk_1_lvl + 1 WHERE username = (%s)", (username,))

    if (int(id) == 2):
        c.execute("UPDATE accounts SET perk_2_lvl = perk_2_lvl + 1 WHERE username = (%s)", (username,))

    if (int(id) == 3):
        c.execute("UPDATE accounts SET perk_3_lvl = perk_3_lvl + 1 WHERE username = (%s)", (username,))

    print(price);
    c.execute("UPDATE accounts SET clicks = clicks - (%s) WHERE username = (%s)", (price, username))

    db.commit()
    db.close()

def record_trial(username, trial_type, clicks):
    db = mysql.connect()
    c = db.cursor()

    if (trial_type == "trial_15_sec"):
        c.execute("SELECT trial_15_sec FROM accounts WHERE username = (%s)", (username,))
        prev_record = c.fetchall()[0][0]
        if (int(clicks) > prev_record):
            c.execute("UPDATE accounts SET trial_15_sec = (%s) WHERE username = (%s)", (clicks, username))

    if (trial_type == "trial_30_sec"):
        c.execute("SELECT trial_30_sec FROM accounts WHERE username = (%s)", (username,))
        prev_record = c.fetchall()[0][0]
        if (int(clicks) > prev_record):
            c.execute("UPDATE accounts SET trial_30_sec = (%s) WHERE username = (%s)", (clicks, username))

    db.commit()
    db.close()

def get_leaderboards():
    db = mysql.connect()
    c = db.cursor()

    leaderboard_15_sec = []
    c.execute("SELECT username, trial_15_sec FROM accounts WHERE trial_15_sec > 0 ORDER BY trial_15_sec")
    for row in c:
        dict = {}
        dict['username'] = row[0]
        dict['seconds'] = row[1]
        leaderboard_15_sec.append(dict)

    leaderboard_30_sec = []
    c.execute("SELECT username, trial_30_sec FROM accounts WHERE trial_30_sec > 0 ORDER BY trial_30_sec")
    for row in c:
        dict = {}
        dict['username'] = row[0]
        dict['seconds'] = row[1]
        leaderboard_30_sec.append(dict)

    db.close()
    return leaderboard_15_sec, leaderboard_30_sec

def calc_persecond(username):
    db = mysql.connect()
    c = db.cursor()

    persecond = 0
    c.execute("SELECT perk_0_lvl, perk_1_lvl, perk_2_lvl, perk_3_lvl FROM accounts WHERE username = (%s)", (username,))

    perk_0_lvl = 0
    perk_1_lvl = 0
    perk_2_lvl = 0
    perk_3_lvl = 0

    for row in c:
        perk_0_lvl = row[0]
        perk_1_lvl = row[1]
        perk_2_lvl = row[2]
        perk_3_lvl = row[3]

    persecond += (perk_0_lvl * 0.1)
    persecond += (perk_1_lvl)
    persecond += (perk_2_lvl * 8)
    persecond += (perk_3_lvl * 47)
    persecond = int(persecond * 10) / 10 #truncate the imprecise floats

    db.close()
    return persecond
