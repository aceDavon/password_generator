import datetime as dt
import pandas
from random import randint
from mail_sender import send_mail

email = "maakojidavid@gmail.com"
password = "eggmghpjmhuguihr"
host = "smtp.gmail.com"
mail_header = "Hurray!"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

file = "birthdays.csv"

data_frame = pandas.read_csv(file)

birthday_dict = {(row_data.month, row_data.day): row_data
                 for (index, row_data) in data_frame.iterrows()}

if today_tuple in birthday_dict:
    file_path = f"letters_directory/letter_{randint(1, 3)}.txt"
    person_birthday = birthday_dict[today_tuple]

    with open(file_path) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", person_birthday["name"])

    send_mail(username=email, password=password, host=host,
              destination=person_birthday["email"], subj=mail_header, msg=letter)

