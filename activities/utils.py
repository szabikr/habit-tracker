from datetime import date, datetime

def get_activity_date(partial_date: str) -> date:
	full_date = f"{partial_date} {date.today().year}"

	# TODO: Allow partial_date to have a few different date formats
	try:
		result = datetime.strptime(full_date, '%d %b %Y').date()
	except ValueError:
		raise ValueError(f"Partial date '{partial_date}' has incorrect format, use '%d %b', i.e. 10 Aug")
		
	return result

def convert_str_to_date(date_str: str) -> date:
	return datetime.strptime(date_str, '%Y-%m-%d').date()
