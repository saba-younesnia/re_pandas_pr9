import pandas as pd

data=pd.read_csv('C:\\Users\\YOONES-NIA\\Desktop\\csv_files\\nba.csv')

same_team_college=data.groupby(['Team','College'])
print(same_team_college.groups)

ave_age=same_team_college['Age'].mean()
print(ave_age.to_string())

