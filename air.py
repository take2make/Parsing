from airtable import Airtable
import pandas as pd
from parameters import *

#base_key = "<your base_key>"
#api_key = "<you api_key>"

def clean_table(table_name="gamifer"):
	airtable = Airtable(base_key, table_name, api_key)
	records = airtable.get_all()
	[airtable.batch_delete([rec['id']]) for rec in records]

def load_table(data, table_name="gamifer"):
	airtable = Airtable(base_key, table_name, api_key)
	for row in data:
		airtable.insert({'Name': row[1], 'Комментарии': row[2], 'Лайки':row[3], 'Баллы': row[4], 'Монеты':row[5]})