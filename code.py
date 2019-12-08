# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Path of the file
path

#Code starts here

#Reading the file
data=pd.read_csv(path)

#Renaming a column
data.rename(columns={'Total':'Total_Medals'},inplace=True)

#Printing the first five columns
print(data.head(10))


#Code ends here




# --------------
#Code starts here
#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)


# --------------
#Code starts here

#Subsetting the dataframe
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last column
top_countries=top_countries[:-1]

#Function for top 10
def top_ten(data, col):
    
    #Creating a new list
    country_list=[]
    
    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))
    
    #Returning the top 10 list
    return country_list



#Calling the function for Top 10 in Summer
top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")

#Code ends here
  



# --------------
#Code starts here
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
df=pd.DataFrame([top_10_summer,top_10_winter,top_10])

summer_df= data[data['Country_Name'].isin(top_10_summer)]
winter_df= data[data['Country_Name'].isin(top_10_winter)]
top_df= data[data['Country_Name'].isin(top_10)]
summer_df.plot.bar('Country_Name','Total_Summer')
winter_df.plot.bar('Country_Name','Total_Winter')
top_df.plot.bar('Country_Name','Total_Medals')


# --------------
#Code starts here
summer_df= data[data['Country_Name'].isin(top_10_summer)]
summer_df['Golden_Ratio']=data['Gold_Summer']/data['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
winter_df= data[data['Country_Name'].isin(top_10_winter)]
winter_df['Golden_Ratio']=data['Gold_Winter']/data['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
top_df= data[data['Country_Name'].isin(top_10)]
top_df['Golden_Ratio']=data['Gold_Total']/data['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=summer_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points']=(data['Gold_Total']*3)+(data['Silver_Total']*2)+(data['Bronze_Total'])
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)


# --------------
#Code starts here

#Subsetting the dataframe
best=data[data['Country_Name']==best_country]
best.reset_index(drop = True, inplace = True)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]


#Plotting bar plot
best.plot.bar(stacked=True)

#Changing the x-axis label
plt.xlabel('United States')

#Changing the y-axis label
plt.ylabel('Medals Tally')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Updating the graph legend
l=plt.legend()
l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))



#Code ends here


