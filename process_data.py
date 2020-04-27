import re

import pandas as pd

CHAT_PATTERN = r'''\[(\d{1,2}\/\d{1,2}\/\d{1,4}, \d{1,2}:\d{1,2}:\d{1,2} [A-Z]{2})\] ([\w\s]+):(.*)'''


def load_file(file, path=''):

	print('Import file begins..')

	with open(path + file, 'r', encoding='UTF-8') as datafile:
		all_msgs = datafile.readlines()


	parsed_data = []
	rgx_srch = re.compile(CHAT_PATTERN)

	for msg in all_msgs:
		srch = rgx_srch.search(msg)
		if srch:
			parsed_data.append([srch.group(1).replace(', ', ' '), srch.group(2), srch.group(3)])
		else:
			parsed_data[-1][2] = parsed_data[-1][2] + ' ' + msg.strip()

	df = pd.DataFrame(parsed_data, columns=['datetime', 'user', 'message'])

	print(f'Total rows imported: {len(df.index)}')
	print('Import file complete..')

	return df


def preprocess(df):
	""" Preprocesses the data and enriches the data with additional attributes

	Parameters:
	df : Pandas dataframe

	Returns:
	df : Pandas dataframe

	"""

	# clean the message to just have the words
	# this will remove the emojis and other special characters
	df['message_clean'] = df.message.replace('\W+', ' ', regex=True)

	# Update datetime column and add new date related columns
	df.datetime = pd.to_datetime(df.datetime, format='%d/%m/%y %I:%M:%S %p')
	df['date'] = pd.to_datetime(df.datetime.dt.date)
	df['time'] = df.datetime.dt.time
	df['hour'] = df.datetime.dt.hour
	df['week'] = df.datetime.dt.week
	df['weekday'] = df.datetime.dt.weekday
	df['month'] = df.datetime.dt.month
	df['year'] = df.datetime.dt.year

	return df

def export(df):
	pass
