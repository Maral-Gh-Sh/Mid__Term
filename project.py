# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:10:19 2022

@author: MARAL
"""

dct_info={"nima":"123","maral":"456"}
import json
with open("info.json","w") as f:
    json.dump(dct_info,f)
dct_products={"TV":2,"camera":5}
with open("products.json","w") as a:
    json.dump(dct_products,a)
dct_shop={"nima":"TV","maral":"camera"}
with open("shop.json","w") as b:
        json.dump(dct_shop,b)
def submit():
    user=input("username: ")
    passw=input("password: ")
    if(len(passw)<5):
        print("Too short password!!!")
        return
    with open ("info.json") as f:
        dct=json.load(f) 
    if(user in dct):
        print("username already exist!")
        return 
    dct[user]=passw
    with open ("info.json","w") as f:
        json.dump(dct,f)
    print("Submit done")
def login():
    user=input("username: ")
    passw=input("password: ")
    with open ("info.json") as f:
       dct=json.load(f) 
    if user in dct and dct[user] == passw:
        print("Welcome to your account")
    else:
        print("Wrong username or password")
while True:
    plan=input("What you wanna do?")
    if(plan=="shopping"):
        account=input("Do you have an account?")
        if(account=="yes"):
            user=input("username?")
            passw=input("password?")
            with open("info.json") as f:
                dct=json.load(f)
            if(user in dct and dct[user]==passw):
                print("Welcome to your account")
                with open("products.json") as a:
                    a=json.load(a)
                print("you can buy",a)
                want=input("What do you wanna buy?")
                with open("products.json") as a:
                    dct=json.load(a)
                if(want in dct and dct[want]>0):
                    print("It registered successfully!!!")
                    x=dct[want]
                    dct.pop(want)
                    dct[want]=x-1
                    with open("products.json","w") as a:
                        json.dump(dct,a)
                    with open("shop.json") as f:
                        dct=json.load(f)
                    dct.pop(user)
                    dct[user]=dct[user]+want
                    with open("shop.json","w") as a:
                        json.dump(dct,a)
                else:
                    print("This product doesn't exist")
            else:
                print("Wrong username or password")
        else:
            print("please submit first")
    elif(plan=="submit"):
        submit()
    elif(plan=="bought"):
        login()
        with open("shop.json") as f:
            dct=json.load(f)
        print(dct[user])
    elif(plan=="used up"):
        with open("products.json") as f:
            dct=json.load(f)
        lst=[]
        for item in dct:
            if dct[item]==0:
                lst.append(item)
                