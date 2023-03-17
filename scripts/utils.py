from datetime import datetime


def get_formated_today():
	now = datetime.now()
	today = now.strftime('%Y%m%d')
	today = str(today)
	return today