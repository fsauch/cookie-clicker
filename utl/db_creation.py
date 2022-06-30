#========= ONLY RUN THIS FILE IF YOU WANT TO CREATE AN EMPTY DATABASE. ========#

#import sqlite3
from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)
app.config.from_pyfile('../database.cfg')

mysql.init_app(app)

def init_db():
    db = mysql.connect()
    c = db.cursor()

    #Create accounts table (empty)
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS accounts(
            username TEXT,
            password TEXT,
            clicks INTEGER,
            total_clicks INTEGER,
            perk_0_lvl INTEGER,
            perk_1_lvl INTEGER,
            perk_2_lvl INTEGER,
            perk_3_lvl INTEGER,
            trial_15_sec INTEGER,
            trial_30_sec INTEGER
        )
        """
    )

    #Create perks table (empty)
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS perks(
            id INTEGER,
            name TEXT,
            description TEXT,
            cost INTEGER
        )
        """
    )

    db.commit() #save changes
    db.close()


def add_perks():
    db = mysql.connect()
    c = db.cursor()

    #In order: ID, name of perk, description of perk, cost of perk
    c.execute("INSERT INTO perks VALUES (%s, %s, %s, %s)", [0, "Cursor", "Generates 0.1 cookies while idle!", 15])
    c.execute("INSERT INTO perks VALUES (%s, %s, %s, %s)", [1, "Grandma", "Generates 1 cookie while idle!", 100])
    c.execute("INSERT INTO perks VALUES (%s, %s, %s, %s)", [2, "Farm", "Generates 8 cookies while idle!", 1100])
    c.execute("INSERT INTO perks VALUES (%s, %s, %s, %s)", [3, "Mine", "Generates 47 cookies while idle!", 12000])

    db.commit() #save changes
    db.close()

#Run this file to generate an empty database file. Do not run this in any other case.init_db();
init_db();
add_perks();
