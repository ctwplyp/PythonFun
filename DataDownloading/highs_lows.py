import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for i, column_header in enumerate(header_row):
		print(i, column_header)
