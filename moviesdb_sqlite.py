# -*- coding: utf-8 -*-
"""MoviesDB-SQLite.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BLvvPu_m_OM9fktLdSCj0u9yzWwQV6cy
"""

import sqlite3
import pandas as pd

db = sqlite3.connect('Movies.db')

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (ID INT, Movie_Name VARCHAR(30), Lead_Actor VARCHAR(30), Lead_Actress VARCHAR(30), Director_Name VARCHAR(30) ,Year_Of_Release INT)")

ids = [1,2,3,4,5]
movies = ["Bahubali","Thor: Love and Thunder","RRR","Vikram","The Gray Man"]
heros = ["Parbas","Chris Hemsworth","Ram Charan","Kamal Haasan","Ryan Gosling"]
heroines = ["Anushka","Natalie Portman","Alia Bhat","Gayathrie Shankar","Ana de Armas"]
directors = ["S. S. Rajamouli","Taika Waititi","S. S. Rajamouli","Lokesh Kanagaraj","Joe Russo, Anthony Russo"]
years = ["2015","2022","2022","2022","2022"]

columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]

for id,movie,hero,heroine,director,year in zip(ids,movies,heros,heroines,directors,years):
    cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES({},"{}","{}","{}","{}",{})'''.format(id,movie,hero,heroine,director,year))

query = """SELECT * from movies"""
cursor.execute(query)
records = cursor.fetchall()

print(pd.DataFrame(records,columns = columns),"\n")

query = """SELECT * from movies where Lead_Actor = 'Chris Hemsworth'"""
cursor.execute(query)
records = cursor.fetchall()

print(pd.DataFrame(records,columns = columns))

