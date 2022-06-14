'''Aim: Scrape an online E-Commerce Site for Data.
Extract product data from Amazon- be it any product and put these details in the MySql database. One can use pipeline. Like 1 pipeline to process the scraped data and other to put the data in the database and since Amazon has some restrictions on scraping of data, ask them to work on small set of requests otherwise proxies and all would have to be used.

Scrape the details like color, dimensions, material etc. Or customer ratings by features.
'''

# mysql download 
# 8.0.
# https://dev.mysql.com/downloads/installer/

# Mysql 5.5 version 
# https://www.professionalcipher.com/p/downloads_22.html


# 
# pip install requests
# pip install mysql.connector

# required Libraries 
import requests
from bs4 import BeautifulSoup
import mysql.connector as db
import csv



# step 1

url = '''https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'''

req = requests.get(url)
soup = BeautifulSoup(req.content , 'html.parser')

res = soup.head
#print(res)

all_products = []


products = soup.findAll('div' , {"class": "_3pLy-c row"})
#print(products)

# database connection 

#******* create database ******************

mydb = db.connect(host = 'localhost' , user = 'root'  , passwd = 'root')
cur = mydb.cursor()

query = '''create database if not exists flipkartdb;'''
cur.execute(query)

mydb.close()

# **************** create table ***************
mydb = db.connect(host = 'localhost' , user = 'root' , passwd = 'root',database = 'flipkartdb')
cur = mydb.cursor()

query = '''create table if not exists products(Mobile_name text , Price text);'''

cur.execute(query)

mydb.close()


# get products 

for product in products:
    m_name = product.select("div > div._4rR01T")[0].text.strip()
    #print(m_name)

    m_price = product.select('div > div._30jeq3')[0].text.strip()
    
    #print(m_price)

    # insert values into database 

    mydb = db.connect(host = 'localhost' , user = 'root' , passwd = 'root' , database = 'flipkartdb')
    cur = mydb.cursor()

    query = f'''insert into products(Mobile_name ,Price ) values("{m_name}" , "{m_price}")'''
    cur.execute(query)
    cur.execute("commit;")

mydb.close()
























