import smtplib
import datetime
import random as rd
import pandas as pd

MY_MAIL = 'ragulshopify26@gmail.com'
MY_PASS = 'xxhhdzatmxbmvjgv'

dt = pd.read_csv("email.csv")

textfile = 'pythontips.txt'

now = datetime.datetime.now()

if now.weekday() < 5:
    if now.hour == 20:#and now.minute == 0:
        with open(textfile,'r') as file_data:
            file_lines =file_data.readlines()
            choice = rd.choice(file_lines)
            
            with open(textfile,'w') as file_data1:
                for i in file_lines:
                    if i !=choice:
                        file_data1.write(i)
                        
        name_data = dt['name']
        mail_data = dt['email']    
        len_datas = len(name_data)            
                                        
        for i in range(len_datas):
            with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
                connection.starttls()
                connection.login(MY_MAIL,MY_PASS)
                connection.sendmail(from_addr=MY_MAIL,to_addrs=mail_data[i],msg=f"Subject:Today's Python Tricks!\nGud Morning {name_data[i]}!\n\n{choice}")
        
             