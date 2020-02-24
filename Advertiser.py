import requests
import pandas as pd

class ImpactConnector:
	def __init__(self, accountSID, authToken):
		self.accountSID = accountSID
		self.authToken = authToken
		self.session = requests.Session()
		self.session.auth = (self.accountSID, self.authToken)
		self.auth = self.session.post('https://api.impact.com')

	def getData(self, taskType, args={}):
		url, dataColumn = self.getUrl(taskType, args)
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

	def getUrl(self, taskType, args):
		if taskType == 'Advertiser_ListActions':
			return self.advertiser_ListActions(args), 'Actions'
		if taskType == 'Advertiser_ListCampaigns':
			return self.advertiser_ListCampaigns(args), 'Campaigns'
		if taskType == 'Advertiser_ListReports':
			return self.advertiser_ListReports(), 'Reports'
		if taskType == 'Advertiser_RunReport':
			return self.advertiser_RunReport(args), 'Records'

	### add more urls for specific API requests. Remember to create a separate function for each to check for Required arguments

	def advertiser_ListActions(self, args):
		if 'CampaignId' in args:
			url = '/Advertisers/' + self.accountSID + '/Actions.json?CampaignId=' + args['CampaignId'] + '?'
			del [args['CampaignId']]
			for key, value in args.items():
				url = url  + str(key) + '=' + str(value) + '&'
			return url
		else:
			return 'No CampaignId provided'

	def advertiser_ListCampaigns(self, args):
		url = '/Advertisers/' + self.accountSID + '/Campaigns.json' + '?'
		for key, value in args.items():
			url = url + str(key) + '=' + str(value) + '&'
		return url

	def advertiser_ListReports(self):
		url = '/Advertisers/' + self.accountSID + '/Reports.json'
		return url

	def advertiser_RunReport(self, args):
		if 'ReportId' in args:
			url = '/Advertisers/' + self.accountSID + '/Reports/' + args['ReportId'] + '.json' +'?'
			del [args['ReportId']]
			url = url + 'SUPERSTATUS_MS=APPROVED&SUPERSTATUS_MS=NA&SUPERSTATUS_MS=PENDING&SUPERSTATUS_MS=REVERSED&'
			for key, value in args.items():
				url = url + str(key) + '=' + str(value) + '&'
			return url
		return 'No ReportId provided'

