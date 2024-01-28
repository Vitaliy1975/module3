import datetime

def get_upcoming_birthdays(users):
    congratulation_list=[]
    today_date=datetime.datetime.today().date()
    today_year=today_date.year
    today_year_string=str(today_year)
    for user in users:
        birthday=datetime.datetime.strptime(user["birthday"],"%Y.%m.%d").date()
        birthday_noyear_string=birthday.strftime("%m.%d")
        birthday_this_year_string=today_year_string+"."+birthday_noyear_string
        birthday_this_year=datetime.datetime.strptime(birthday_this_year_string,"%Y.%m.%d").date()
        weekday=birthday_this_year.weekday()
        difference=birthday_this_year-today_date
        if difference.days<0:
            birthday_next_year_string=str(int(today_year_string)+1)+"."+birthday_noyear_string
            congratulation_list.append({"name":user["name"],"congratulation_date":("Next year birthday "+birthday_next_year_string)})
            continue
        elif difference.days>7:
            continue
        elif weekday==6:
            bday_monday=birthday_this_year+datetime.timedelta(days=1)
            congratulation_list.append({"name":user["name"],"congratulation_date":(datetime.datetime.strftime(bday_monday,"%Y.%m.%d"))})
            continue
        elif weekday==5:
            bday_monday=birthday_this_year+datetime.timedelta(days=2)
            congratulation_list.append({"name":user["name"],"congratulation_date":(datetime.datetime.strftime(bday_monday,"%Y.%m.%d"))})
            continue
        else:
                        congratulation_list.append({"name":user["name"],"congratulation_date":birthday_this_year_string})
    return congratulation_list

