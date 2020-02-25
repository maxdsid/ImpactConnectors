# Advertiser
from Advertiser import ImpactConnector as Advertiser

advertiser = Advertiser(
    accountSID='insert your advertiser SID here',
    authToken='insert your advertiser auth token here'
)

reports = advertiser.advertiser_ListReports()

campaigns = advertiser.advertiser_ListCampaigns()

campaignId = campaigns.Id[0]
reportId = reports.Id[94]

report = advertiser.advertiser_RunReport(reportId=reportId, SUBAID=campaignId)

actions = advertiser.advertiser_ListActions(campaignId=campaignId, Start_Date='2020-01-01', End_Date='2020-01-31')


# Agency
from Agency import ImpactConnector as Agency

agency = Agency(
    accountSID='insert your agency SID here',
    authToken='insert your agency auth token here'
)

reports = agency.agency_ListReports()

reportId = reports.Id[5]

report = agency.agency_RunReport(reportId=reportId)