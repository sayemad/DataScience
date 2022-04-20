import json
import pandas as pd

with open("FBI_CrimeData_2016.json") as json_file:
    crime_list = json.load(json_file)
    def accum_crime(key,crime,crime_list):
        murder_by_region ={}
        
        for crime_dict in crime_list:
            if crime_dict[key] in murder_by_region:
                Region = crime_dict[key]
                murders = int(crime_dict[crime])
                murder_by_region[Region]= murders + int(murder_by_region[Region])
            else:
                Region = crime_dict[key]
                murders = int(crime_dict[crime])
                murder_by_region[Region] = murders
        return murder_by_region
    
    murder_by_region= accum_crime('Region','Murder',crime_list)
    
    def barchart(murder_by_region,title):
    
        dataSeriesY = pd.Series(list(murder_by_region.values()))
        dataSeriesX = pd.Series(list(murder_by_region.keys()))
        pdDict = {"Incidents":dataSeriesY, "Regions":dataSeriesX}
        df = pd.DataFrame(pdDict)
        print('\n')
        print(title)
        print(df)
        df.plot.bar(x="Regions", y="Incidents", title= title,figsize=(8,6),legend=False,
                color=['#0059b3', '#ff9933', '#009900', '#ff0000'])
    
