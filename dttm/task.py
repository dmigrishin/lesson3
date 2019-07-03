from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "russian")
dt_yesterday = datetime.now()-timedelta(days=1)
dt_now = datetime.now()
dt_month_ago = datetime.now()-timedelta(days=30)

print('Вчера: ', dt_yesterday.strftime('%d.%m.%Y'))
print ('Сегодня: ',dt_now.strftime('%d.%m.%Y'))
print ('Месяц назад: ',dt_month_ago.strftime('%d.%m.%Y'))

date_string='01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

print ('Это объект типа ДАТА: ',date_dt)