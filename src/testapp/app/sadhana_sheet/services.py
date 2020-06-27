from datetime import date, timedelta, datetime
from werkzeug.exceptions import BadRequest

from .models import SadhanaSheet, UserSadhana
from testapp.app.users.models import User
from testapp import db


def get_all_sadhana_sheets():
    sadhana_sheets = SadhanaSheet.query.all()
    active_sheet = [sheet for sheet in sadhana_sheets if sheet.is_active][0]
    previous_sheets = [sheet for sheet in sadhana_sheets if not sheet.is_active]
    return active_sheet, previous_sheets

def days_cur_month(month, year):
    m = datetime.strptime(month, '%B').month
    y = datetime.strptime(year, '%Y').year
    ndays = (date(y, m+1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1
    return [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

def get_sadhana_sheet_data(sheet_id):
    sheet_data = []
    sadhana_sheet = SadhanaSheet.query.get(sheet_id)
    all_dates = days_cur_month(sadhana_sheet.month, sadhana_sheet.year)
    user_sadhanas = UserSadhana.query.filter_by(sadhana_sheet_id=sheet_id, user_id=1)
    user = UserSadhana.query.filter_by(sadhana_sheet_id=sheet_id, user_id=1)[0].users.name
    user_sadhana_dates = [str(i.date) for i in user_sadhanas]
    for date in all_dates:
        if date in user_sadhana_dates:
            sadhana = [i for i in user_sadhanas if str(i.date) == date ][0]
            sheet_data.append({
                'date': int(sadhana.date.day),
                'do_wakeup': sadhana.do_wakeup,
                'do_prayer': sadhana.do_prayer,
                'do_exercise': sadhana.do_exercise,
                'do_listen': sadhana.do_listen,
                'do_namasmarana': sadhana.do_namasmarana,
                'do_drink_water': sadhana.do_drink_water,
                'do_no_tv': sadhana.do_no_tv,
            })
        else:
            sheet_data.append({
                'date': datetime.strptime(date, '%Y-%m-%d').day,
                'do_wakeup': None,
                'do_prayer': None,
                'do_exercise': None,
                'do_listen': None,
                'do_namasmarana': None,
                'do_drink_water': None,
                'do_no_tv': None,
            })
    all_dates = [datetime.strptime(date, '%Y-%m-%d').day for date in all_dates]
    return all_dates, sheet_data, sadhana_sheet, user


def get_sadhana_sheet_for_edit(sheet_id):
    sadhana_sheet = SadhanaSheet.query.get(sheet_id)
    all_dates = days_cur_month(sadhana_sheet.month, sadhana_sheet.year)
    today = datetime.strftime(datetime.now(), '%Y-%m-%d')
    if datetime.now().day == 1:
        return [datetime.strptime(date, '%Y-%m-%d') for date in all_dates]
    else:
        return [datetime.strptime(date, '%Y-%m-%d') for date in all_dates[all_dates.index(today):]], sadhana_sheet


def add_user_sadhana(sheet_id, date):
    sadhana_sheet = SadhanaSheet.query.get(sheet_id)
    return sadhana_sheet

def save_user_sadhana(sheet_id, date, request_data):
    sadhana_sheet = SadhanaSheet.query.get(sheet_id)
    us_data = UserSadhana.query.filter_by(sadhana_sheet_id=sheet_id,
                                          user_id=1, date=date)
    do_wakeup = True if request_data.form.get('do_wakeup') == 'Yes' else False
    do_prayer = True if request_data.form.get('do_prayer') == 'Yes' else False
    do_exercise = True if request_data.form.get('do_exercise') == 'Yes' else False
    do_listen = True if request_data.form.get('do_listen') == 'Yes' else False
    do_namasmarana = True if request_data.form.get('do_namasmarana') == 'Yes' else False
    do_drink_water = True if request_data.form.get('do_drink_water') == 'Yes' else False
    do_no_tv = True if request_data.form.get('do_no_tv') == 'Yes' else False
    if us_data:
        us_data.do_wakeup = do_wakeup
        us_data.do_prayer = do_prayer
        us_data.do_exercise = do_exercise
        us_data.do_listen = do_listen
        us_data.do_namasmarana = do_namasmarana
        us_data.do_drink_water = do_drink_water
        us_data.do_no_tv = do_no_tv
        db.session.commit()
    else:
        user_sadhana = UserSadhana(
            sadhana_sheet_id=sheet_id,
            user_id=1,
            date=date,
            do_wakeup=do_wakeup,
            do_prayer=do_prayer,
            do_exercise=do_exercise,
            do_listen=do_listen,
            do_namasmarana=do_namasmarana,
            do_drink_water=do_drink_water,
            do_no_tv=do_no_tv,
        )
        db.session.add(user_sadhana)
        db.session.commit()



