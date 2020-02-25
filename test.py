# Advertiser
from Advertiser import ImpactConnector as Advertiser

advertiser = Advertiser(
    accountSID='IR6mK8kE8ZLX1309971UKr5HMvV7Jj3Fo1',
    authToken='w-UkTGG29VXqGvgMA-ZTruKzMocNzpyY'
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
    accountSID='IRV7RTUdQpTC1271468rv87WToq4KCrZR1',
    authToken='LuWp-zuyDhyHCY-KoTRVEY3wEYUohi3n'
)

reports = agency.agency_ListReports()

reportId = reports.Id[5]

report = agency.agency_RunReport(reportId=reportId)