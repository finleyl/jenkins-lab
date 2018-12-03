import datetime
print("Hello, this is the current date and time!")
now = datetime.datetime.now()
print ("Current date and time is ")
print (now.strftime("%A, %d-%m-%Y : %H:%M"))
