##Created by Logan Sanchez

##If first time using program, uncomment line 118
##else, leave line 117 commented out

##Fork of DBNew.py
##07/27/21

##Have program create Backup File automatically

##Think about program going forward


##########################
##########################

##Gives props Libraries ##

##########################
##########################


##Art Library
from art import *
##Art Library

##########################
##########################

##Gives props Libraries ##

##########################
##########################


##  Basic Libraries ##
import hashlib
import sqlite3
import json
import os
import datetime
import sys
import time

##  Basic Libraries ##

##Pieces ##

##Users Database
connUser = sqlite3.connect('testUsersListDatabase.db')
cUser = connUser.cursor()


def accountCreationOrSignIn():
##Create Userlist Table
    print('\nPLEASE SELECT AN OPTION:\n')

    print('[1]: New User\n')

    print('[2]: Returning user\n')

    print('\n\n[Z]: EXIT\n\n')
    

    print('ENTER OPTION NUMBER HERE:')
    answer = input()
    if answer == '1':
        newUser()

    if answer == '2':
        signIn(cUser)

    if answer.upper() == 'Z':
            sys.exit()

    if answer != '1':
        if answer != '2':
            if answer != '3':
                if answer != 'Z':
                    print('incorrect entry, goodbye.')
                    time.sleep(2)
                    sys.exit()
                    

def newUser():
    
    print('ENTER USERNAME: ')
    uName = (input().strip("!#$%&*^/?<>'':""}{[]\-+ '"))


    newName = (uName,)


    os.makedirs(os.getcwd() + '//' + uName)

        ##Once table is initially created, comment out this line
        ##Table has a completion marker set to = '0'/F as default

        ##Create Table

    #cUser.execute(' ' 'CREATE TABLE userList (Id INTEGER PRIMARY KEY, userName TEXT NOT NULL, password TEXT NOT NULL, date TEXT NOT NULL, completionMarker TEXT NOT NULL) ' ' ')

        ##Once table is initially created, comment out this line
        ##Table has a completion marker set to = '0'/F as default

        
        ##Keep these lines
    cUser.execute('INSERT INTO userList(UserName, Password, Date, completionMarker) values (0,0,0,0)')
    cUser.execute('update userList set UserName = ? where UserName = 0', newName)
        ##Keep these lines
        

    print('Enter Password: ')
    uPass = (input().strip("!#$%&*^/?<>'':""}{[]\-+ '"))

    passwordAsBytes = str.encode(uPass)
    ## Can change type of hash with the 'm' variable
    m = hashlib.sha256()
    m.update(passwordAsBytes)

    cUser.execute('update userList set UserName = ? where UserName = 0', newName)
    #    ##Hash Pass
    cUser.execute('update userList set Password = ? where Password = 0', (str(m.hexdigest()),))
    delDate = (datetime.datetime.now(),)
    cUser.execute('update userList set Date = ? where Date = 0', delDate)

    # Completion marker
    cUser.execute('update userList set completionMarker = 1 where completionMarker = 0')
    
    #Save new information added
    connUser.commit()
    print('\n\nSaved.\n')




def signIn(connection):
    connUser.row_factory = sqlite3.Row
    curs = connUser.cursor()
    print('ENTER USERNAME: ')
    username = (input())
    curs.execute('select * from userList')
    rows = curs.fetchall()
    for row in rows:
        if row[1] == username:
            print('ENTER PASSWORD: ')
            password = input()
            passwordAsBytes = str.encode(password)
            m = hashlib.sha256()
            m.update(passwordAsBytes)
            if row[2] == str(m.hexdigest()):
                mainMenu(username)



def mainMenu(username):

    
    ##Change Name
    tprint("Welcome to the database. " + username ,font="rnd-large")
    os.chdir(os.getcwd() + '//' + username)

    print('\n\n')

                 
    connUser.close()
    if os.path.isfile('testMainProfileDatabase.db') == True:

        ## Create Profile Database here ##
        connUserProfileInfo = sqlite3.connect('testMainProfileDatabase.db')
        cUserProfileInfo = connUserProfileInfo.cursor()

         ## Create Mailbox Database here ##
        connUserMailboxInfo = sqlite3.connect('testMainMailboxDatabase.db')
        cUserMailboxInfo = connUserMailboxInfo.cursor()

############################################################

        print('\nPLEASE SELECT AN OPTION:\n')

        print('[1]: View Profile Data')

        ##To user/ to individual group
        print('[2]: Mailbox')


        print('\n\n[Z]: EXIT\n\n')
    

        print('ENTER OPTION NUMBER HERE:')
        answer = input()
        
        if answer == '1':
            viewProfileData(connUserProfileInfo)
            connUserProfileInfo.close()

        if answer == '2':
            mailBox(username)
        ##Check if general chat is created

    
        if answer.upper() == 'Z':
            connUserProfileInfo.close()
            sys.exit()

        if answer != '1':
            if answer != '2':
                if answer != '3':
                    if answer != 'Z':
                        print('incorrect entry, goodbye.')
                        connUserProfileInfo.close()
                        time.sleep(2)
                        sys.exit()

    ############################################################
            

            

    ## Create Profile Database here ##
    else:
        ## Create Profile Database here ##
        connUserProfileInfo = sqlite3.connect('testMainProfileDatabase.db')
        cUserProfileInfo = connUserProfileInfo.cursor()

         ## Create Mailbox Database here ##
        connUserMailboxInfo = sqlite3.connect('testMainMailboxDatabase.db')
        cUserMailboxInfo = connUserMailboxInfo.cursor()

        createProfile()
        createMailBox()

        ############################################################

        print('\nPLEASE SELECT AN OPTION:\n')

        ##Create Mailbox here
        ##print('[1]: Create Profile [Recommended for new users]\n')

        print('[1]: View Profile Data')

        ##To user/ to individual group
        print('[2]: Mailbox')

        print('\n\n[Z]: EXIT\n\n')
    

        print('ENTER OPTION NUMBER HERE:')
        answer = input()

        if answer == '1':
            viewProfileData(connUserProfileInfo)
            connUserProfileInfo.close()

        if answer == '2':
            mailBox(username)
        ##Check if general chat is created

        if answer.upper() == 'Z':
            connUserProfileInfo.close()
            sys.exit()

        if answer != '1':
            if answer != '2':
                if answer != '3':
                    if answer != 'Z':
                        print('incorrect entry, goodbye.')
                        connUserProfileInfo.close()
                        time.sleep(2)
                        sys.exit()




def createProfile():
    ##Main Profile Database

    connUserProfileInfo = sqlite3.connect('testMainProfileDatabase.db')
    cUserProfileInfo = connUserProfileInfo.cursor()

    
    print('ENTER AGE: ')
    uAge = (input().strip("!#$%&*^/?<>'':""}{[]\-+ '"))


    newAge = (uAge,)


        ##Once table is initially created, comment out this line
        ##Table has a completion marker set to = '0'/F as default

        ##Create Table

    cUserProfileInfo.execute(' ' 'CREATE TABLE userProfile (Id INTEGER PRIMARY KEY, age TEXT NOT NULL, description TEXT NOT NULL, date TEXT NOT NULL, completionMarker TEXT NOT NULL) ' ' ')

        ##Once table is initially created, comment out this line
        ##Table has a completion marker set to = '0'/F as default

        
        ##Keep these lines
    cUserProfileInfo.execute('INSERT INTO userProfile(age, description, date, completionMarker) values (0,0,0,0)')
    cUserProfileInfo.execute('update userProfile set age = ? where age = 0', newAge)
        ##Keep these lines
        

    print('Enter brief description of who you are: ')
    uDescription = (input().strip("!#$%&*^/?<>'':""}{[]\-+ '"))
    newDescription = (uDescription,)
    cUserProfileInfo.execute('update userProfile set description = ? where description = 0', newDescription)

    delDate = (datetime.datetime.now(),)
    cUserProfileInfo.execute('update userProfile set date = ? where date = 0', delDate)

    # Completion marker
    cUserProfileInfo.execute('update userProfile set completionMarker = 1 where completionMarker = 0')
    
    #Save new information added
    connUserProfileInfo.commit()
    print('\n\nSaved.\n')


    


def viewProfileData(connection):
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute('select * from userProfile')
    rows = curs.fetchall()
    for row in rows:
        print(tuple(row))
        print('PRESS ENTER TO CONTINUE')
        wait = input(' ')

def createMailBox():
    connUserMailboxInfo = sqlite3.connect('testMainMailboxDatabase.db')
    cUserMailboxInfo = connUserMailboxInfo.cursor()
    ##chatGroup == 'Inbox', 'Group Name: Love Island', 'Group Name: [CLICK TO SEE]'
    cUserMailboxInfo.execute(' ' 'CREATE TABLE mailbox (Id INTEGER PRIMARY KEY, chatGroup TEXT NOT NULL, receivedMessage TEXT NOT NULL, sentMessage TEXT NOT NULL, sentUser TEXT NOT NULL, date TEXT NOT NULL, completionMarker TEXT NOT NULL) ' ' ')
    cUserMailboxInfo.execute('INSERT INTO mailbox(chatGroup, receivedMessage, sentMessage, sentUser, date, completionMarker) values (0,0,0,0,0,0)')
    connUserMailboxInfo.close()

def mailBox(username):
    connUserMailboxInfo = sqlite3.connect('testMainMailboxDatabase.db')
    cUserMailboxInfo = connUserMailboxInfo.cursor()
    print('\nWelcome to Mailbox:\n\n')
    print('\nPLEASE SELECT AN OPTION:\n')


    print('[1]: View Inbox')

    print('[3]: Send Message')


    

    print('\n\n[Z]: EXIT\n\n')
    print('ENTER OPTION NUMBER HERE:')
    answer = input()
    if answer == '1':
        inbox(connUserMailboxInfo)
        connUserMailboxInfo.close()


    if answer == '3':
        sendMessage(username)
        connUserMailboxInfo.close()
        ##Check if general chat is created

        if answer.upper() == 'Z':
                #print('Goodbye.')
            connUserMailboxInfo.close()
            sys.exit()

        if answer != '1':
            if answer != '2':
                if answer != '3':
                    if answer != 'Z':
                        print('incorrect entry, goodbye.')
                        connUserProfileInfo.close()
                        time.sleep(2)
                        sys.exit()

def inbox(mailbox):
    mailbox.row_factory = sqlite3.Row
    curs = mailbox.cursor()
    curs.execute('select * from mailbox')
    rows = curs.fetchall()
    for row in rows:
        print("###########################################")
        print('\n')
        print("Message from Chat Group: " + row[1])
        print('\n')
        print("From User: " + row[4])
        print('\n')
        print("Message: " + row[2])
        print('\n')
        print("Time stamp: " + row[5])
        print('\n')
        print("###########################################")
        print('\n')
        
    print('PRESS ENTER TO CONTINUE')
    wait = input(' ')

def sentMail(mailbox):

    mailbox.row_factory = sqlite3.Row
    curs = mailbox.cursor()
    curs.execute('select * from mailbox')
    rows = curs.fetchall()
    for row in rows:
        print("###########################################")
        print('\n')
        print("Message from Chat Group: " + row[1])
        print('\n')
        print("Sent to: " + row[4])
        print('\n')
        print("Message: " + row[2])
        print('\n')
        print("Time stamp: " + row[5])
        print('\n')
        print("###########################################")
        print('\n')
        
    print('PRESS ENTER TO CONTINUE')
    wait = input(' ')

def sendMessage(username):

   
    os.chdir("..")
    print('Who do you want to message?: ')
    usernameToFind = input()
    if os.path.isdir(os.getcwd() + '//' + usernameToFind):
        os.chdir(os.getcwd() + '//' + usernameToFind)
        connUserMailboxInfo = sqlite3.connect('testMainMailboxDatabase.db')
        cUserMailboxInfo = connUserMailboxInfo.cursor()
        
        cUserMailboxInfo.execute('INSERT INTO mailbox(chatGroup, receivedMessage, sentMessage, sentUser, date, completionMarker) values (0,0,0,0,0,0)')
        print('Enter chat group: ')
        mailChatGroupID = (input().strip("!#$%&*^/?<>'':""}{[]\-+ '"))
        newmailChatGroupID = (mailChatGroupID,)
        cUserMailboxInfo.execute('update mailbox set chatGroup = ? where chatGroup = 0', newmailChatGroupID)
        print('\n')
        newUsername = (username,)
        cUserMailboxInfo.execute('update mailbox set sentUser = ? where sentUser = 0', newUsername)
        print('\n')
        print('Enter message: ')
        uMessage = (input().strip("!#$%&*^/?<>'':""}{[]\-+ '"))
        newUMessage = (uMessage,)
        cUserMailboxInfo.execute('update mailbox set receivedMessage = ? where receivedMessage = 0', newUMessage)
        print('\n')
        uReceivedMessage = "N/A"
        newUReceivedMessage = (uReceivedMessage,)
        cUserMailboxInfo.execute('update mailbox set sentMessage = ? where sentMessage = 0', newUReceivedMessage)
        print('\n')

        delDate = (datetime.datetime.now(),)
        cUserMailboxInfo.execute('update mailbox set date = ? where date = 0', delDate)

        # Completion marker
        cUserMailboxInfo.execute('update mailbox set completionMarker = 1 where completionMarker = 0')
    
        #Save new information added
        connUserMailboxInfo.commit()
        print('\n\nSaved.\n')

        os.chdir("..")

        
        
    else:
        print('No User by this name. Goodbye.')
        time.sleep(2)
        sys.exit()
            

##TEST AREA ##
#print('NOW CONNECTED TO DATABASE...\n')
accountCreationOrSignIn()



#Close File                     
#connUser.close()

