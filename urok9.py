# import sqlite3
# connection = sqlite3.connect("itstep_DB.SL3",5)
# cur = connection.cursor()
# print(connection)
# print(cur)
# connection.close()
import sqlite3
connection = sqlite3.connect("itstep_DB.SL3",5)
cur = connection.cursor()
# cur.execute("CREATE TABLE weather (day TEXT, temp TEXT);")
import requests
import datetime
from bs4 import BeautifulSoup

response = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "lSide"})
    res = soup_list[0].find("p", {"class": "today-temp"})
    # res = soup_list[0].find("span")
    print(res.text)
    a = res.text

cur.execute(f"INSERT INTO weather  VALUES ('{datetime.datetime.now()}','{a}');")


# cur.execute("INSERT INTO first_table (day)"
#               "VALUES ('29');")
# cur.execute("INSERT INTO first_table (name)"
#             "VALUES ('TOMA');")
# cur.execute("INSERT INTO first_table (name)"
#             "VALUES ('Artem');")
# cur.execute("INSERT INTO first_table (name)"
#             "VALUES ('Stainer');")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# cur.execute("UPDATE  first_table SET name ='Tamara' WHERE rowid=3;")
# cur.execute("DELETE FROM first_table WHERE rowid=4;")
# connection.commit()
# # cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
#
# res = cur.fetchall()
# print(res)
connection.close()