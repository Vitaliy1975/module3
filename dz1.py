from datetime import datetime

def get_days_from_today(date):
    try:
        parsed_date=datetime.strptime(date,"%Y-%m-%d").date()
    except Exception:
        return "Wrong input date format. Please, use YYYY-MM-DD date format."
    today_date=datetime.today().date()
    days_between=today_date-parsed_date
    days_between_int=days_between.days
    days_between_int=int(days_between_int)
    return days_between_int

