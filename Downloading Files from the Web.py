from urllib import request
google_url='https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisionalz-size-bands.csv'
def company_data(csv_url):
 response=request.urlopen(csv_url)
 csv=response.read()
 csv_str=str(csv)
 csv_str = csv.decode('utf-8')
 dest_url=r'comapany.csv'
 fx=open(dest_url,"w")
 for line in lines:
    fx.write(line + "\n")
    fx.close()
company_data(google_url)