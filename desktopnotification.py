import time
from plyer import notification 

if __name__=="__main__":
	while True:
		notification.notify(
			title = "PLease Drink Water",
			message = "You need water to digest your food and get rid of waste. Water is needed for digestive",
			app_icon = "glass.ico",
			timeout = 2
			)
		time.sleep(6*6)