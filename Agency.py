import requests
import pandas as pd

class ImpactConnector:
	def __init__(self, accountSID, authToken):
		self.accountSID = accountSID
		self.authToken = authToken
		self.session = requests.Session()
		self.session.auth = (self.accountSID, self.authToken)
		self.auth = self.session.post('https://api.impact.com')

	def agency_ListReports(self):
		url = '/Agencies/' + self.accountSID + '/Reports.json'
		dataColumn = 'Report'
		result = pd.DataFrame()
		while url != '':
			response = self.session.get('https://api.impact.com' + url)
			if response.status_code != 200:
				raise Exception(response.text.replace('\n', ': '))
			response = response.content.decode('utf-8')
			data = pd.read_json(response, typ='series')
			url = data['@nextpageuri']
			for record in data[dataColumn]:
				result = result.append(record, ignore_index=True, )
		return result

	def agency_RunReport(self, reportId, args):
		url = f'/Agencies/{self.accountSID}/Reports/{reportId}.json?'
		for key, value in args.items():
			url = url + str(key) + '=' + str(value) + '&'
		dataColumn = 'Records'
		result = pd.DataFrame()
		while url != '':
			response = self.session.get('https://api.impact.com' + url)
			if response.status_code != 200:
				raise Exception(response.text.replace('\n', ': '))
			data = response.content.decode('utf-8')
			data = pd.read_json(data, typ='series')
			url = data['@nextpageuri']
			for record in data[dataColumn]:
				result = result.append(record, ignore_index=True, )
		return result, response

