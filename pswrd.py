# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:09:30 2020

@author: Soumitra
"""
# Importing Packages

import pprint                               #for pretty printing
from pymongo import MongoClient             #python module MongoDb

main = input("Enter your Username: ")
p = input("Enter Master Password:")
url = 'mongodb://localhost:27017/'          #url for connecting to mongo server
client = MongoClient(url)
db = client.pswtest #this is a database
res = db.authenticate(main,p)               #authentication
doc = db.doc #this is a table

#menu for CLI 
print("1. Add One")
print("2. View One")
print("3. View All")
print("4. Update one")
print("5. Delete one")
print("6. Delete all")

a  = int(input("Enter Choice: "))

if(a==1):
   ans = 'y'
   while(ans=='y' or ans == 'Y'):
       acc = input("Enter Account name:")
       psw = input('Enter Password:')
       data = {"Account":acc,"Password":psw}
       result = doc.insert_one(data)
       ans = input("Do you want to insert more passwords?(y/n)")


elif(a==2):
   acc = input("Enter Account name:")
   data = db.doc.find_one({"Account":acc})
   pprint.pprint(data)


elif(a==3):
   view = db.doc.find()
   for j in view:
       pprint.pprint(j)


elif(a==4):
    ans = 'y'
    while(ans=='y' or ans == 'Y'):
        acc = input("Enter the name of Account you want to update: ")
        psw = input("Enter New Password: ")
        result = db.doc.update_one({'Account':acc},{'$set':{'Password':psw}})
        if(result.matched_count == 1 and result.modified_count == 1):
             print("Success!")
        else:
             print("Failed to update.")
        ans = input("Do you want to insert more passwords?(y/n)")


elif(a==5):
    ans = 'y'
    while(ans=='y' or ans == 'Y'):
        acc = input("Enter the name of account you want to delete: ")
        result = db.doc.delete_one({'Account':acc})
        if(result.deleted_count == 1):
             print("Success!")
        else:
             print("Failed to update.")
        ans = input("Do you want to insert more passwords?(y/n)")

        
elif(a==6):
    db.doc.drop()