from plyer import notification
import requests
import time
def notifyMe(title,message):
	notification.notify(
		title=title,
		message=message,
		timeout=20,
		app_icon="C:/Users/Nandu/OneDrive/Documents/GitHub/Python/python_/project/covid.ico",
		)

def getData(url):
	r=requests.get(url)
	return r.text
if __name__=="__main__":
	Data=getData('https://corona-rest-api.herokuapp.com/Api/india')
	list=Data[12:255]
	list1=list.split(",")
	text=f"{list1[0]} {list1[1]}\n{list1[2]} {list1[3]}\n{list1[4]} {list1[5]}\n{list1[6]} {list1[7]}\n\
	{list1[8]} {list1[9]}\n{list1[10]} {list1[11]}"
	notifyMe("COVID updates",text)
	time.sleep(86400)