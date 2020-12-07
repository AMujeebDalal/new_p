from datetime import datetime
import pandas as pd
import smtplib
import random

df = pd.read_csv("birthdays.csv")
b_days = {(df_row.month, df_row.day): df_row for (index, df_row) in df.iterrows()}
print(b_days)
today = (datetime.now().month, datetime.now().day)
file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
my_email = "example@gmail.com"
password = "password"

if today in b_days:
    b_day_person = b_days[today]
    with open(file_path) as msg:
        letter = msg.read()
        letter = letter.replace("[NAME", b_day_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=b_day_person["email"],
                            msg=f"Subject:Happy Birthday!\n\nSalam\n{letter}")


# Can automate on python anywhere

