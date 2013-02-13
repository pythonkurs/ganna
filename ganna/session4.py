import requests
import json
from dateutil import parser
from pandas import DataFrame

%paste
class stat_repo(object):
	
	def __init__(self, username, password):
		self.username = username
		self.password = password
		
	def df_commint(self):	
		repos = requests.get("https://api.github.com/orgs/pythonkurs/repos",auth=(self.username,self.password)) 
		repos_data = repos.json()
		comm_date = []
		comm_days = []
		comm_hours = []
		comm_messages = []
		for j in range(0, len(repos_data)):
			u=repos_data[j]["commits_url"]
			commit = requests.get(u[:-6], auth=(self.username,self.password))
			commit_data = commit.json()
			for k in range(0, len(commit_data)):
				if len(commit_data)==1:
					continue
				datetime=parser.parse(commit_data[k]["commit"]["committer"]["date"])
				comm_date.append(datetime)
				comm_days.append(datetime.strftime("%A"))
				comm_hours.append(datetime.hour)
				comm_messages.append(commit_data[k]["commit"]["message"])
		self.repo_df = DataFrame({'day': comm_days,
		                     'hour' : comm_hours,
		                     'message' : comm_messages},
		                      index = comm_days)
		return self.repo_df
		
	def common_day_hour(self):
		day_grouped = self.repo_df.groupby("day")
		most_common_day = max(day_grouped.groups.iterkeys(), key=(lambda x:  day_grouped.count()["day"][x]))
		hour_grouped = self.repo_df.groupby("hour")
		most_common_hour = max(hour_grouped.groups.iterkeys(), key=(lambda x:  hour_grouped.count()["hour"][x]))
		return(most_common_day,most_common_hour)

			
		
def show(username,password):
	stat_repos = stat_repo(username,password)
	stat_repos.df_commint()
	print stat_repos.common_day_hour()



