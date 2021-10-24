import pandas as pd
import requests as r
import unittest

def test_fun(self):
	regexp = re.compile('[^0-9a-zA-Z]+')
	with self.assertRaises(TypeError):
	if regexp.search(self):
    	vin_df.values = True

with pd.ExcelFile('Data Products Coding Exercise.xlsx') as xl:
	est_df = pd.read_excel(xl, 'estimates', usecols = ['dim_asset_id', 'estimate_id', 'total']).drop_duplicates()
	assets_df = pd.read_excel(xl, 'assets', usecols = ['dim_asset_id', 'vin']).drop_duplicates()


df = cost_df = est_df.merge(assets_df, how = 'inner', on = 'dim_asset_id')
df = cost_df.group_by(['vin'])[['total']].agg('sum')
df['vin'] = df['vin'].map(lambda x: re.sub(r'\W+', '', x))

df.to_csv('dpce.csv', index = 'False')

vin_df = assets_df['vin'].to_list()

try:
	test_fun(vin_df)
except e:
	raise

url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
post_fields = {'format': 'json', 'data':vin_df}

try:
	r = requests.post(url, data = post_fields)
	j = r.json()
except e:
	'no info'

carInfo_df = pd.DataFrame.from_dict(j)