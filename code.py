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
         def accum_violent_crime(key,crime,crime_list):
        
        violent_by_region ={}
        for crime_dict in crime_list:
            if crime_dict[key] in violent_by_region:
                Region = crime_dict[key]
                violent_crimes = int(crime_dict[crime[0]])+int(crime_dict[crime[1]])+int(crime_dict[crime[2]])+int(crime_dict[crime[3]])
                violent_by_region[Region]= violent_crimes + int(violent_by_region[Region])
            else:
                Region = crime_dict[key]
                violent_crimes = int(crime_dict[crime[0]])+int(crime_dict[crime[1]])+int(crime_dict[crime[2]])+int(crime_dict[crime[3]])
                violent_by_region[Region] = violent_crimes
        return violent_by_region
    
    crimes = ['Murder','Rape','Robbery','Assault']
    violent_by_region = accum_violent_crime('Region',crimes,crime_list)
    violent_by_state = accum_violent_crime('State',crimes,crime_list)
    TotalCrime = 0 
    Violentstate=[]
    for crime in violent_by_state.values():
        TotalCrime += crime
    
    Average = TotalCrime/len(violent_by_state.keys())


    for crime in violent_by_state.items():
        Distance = crime[1] - Average

        violentByState = (crime[0],crime[1],Distance)
        Violentstate.append(violentByState)
    
    print("National Average Violent Crime", Average)
    print("{}  {}   {}".format('State','Crimes','Distance from Mean'))
    for state_tuple in Violentstate:
        print("{0}    {1}  {2}".format(state_tuple[0], state_tuple[1], state_tuple[2]))
    
    def piechart(violent_by_region,title):
        dataSeries = pd.Series(list(violent_by_region.values()),index=list(violent_by_region.keys()))
        pdDict = { "Quarter": dataSeries}
        df = pd.DataFrame(pdDict)
        df.plot.pie(y='Quarter',label="",title="Violent crimes in percentage by Region",legend=False,figsize=(8,8),autopct='%1.2f%%',shadow=True)


    
