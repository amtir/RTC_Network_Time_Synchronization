


import os
import sys
import threading
import urllib.parse
import urllib.request
from datetime import datetime
import time
from lib_python_logging import * 
import subprocess
import pytz



my_logger = get_logger("logger_internal_rtc")

# Simple routine to check if our server and internet are up and ready. 
def check_internet_connect():
	#return True
	production_host = "http://google.com"
	try:
		urllib.request.urlopen(production_host, timeout=3)
		#print("Online Mode")
		return True
	except:
		#print("Offline Mode")
		return False




def rtc_update():				
	cmd_status = 'date' #'sudo systemctl status systemd-timesyncd.service'
	ret_int = os.system( cmd_status )
	ret_msg = subprocess.check_output( cmd_status )
	if(ret_int == 0):
		my_logger.info("date before resync: {}".format(ret_msg.decode("utf-8")))
	
	IoT_check_connect = 0
	while( not check_internet_connect()	): 
		#print("Waiting IoT connection ...")
		my_logger.info( "Waiting IoT connection ..." )
		#time.sleep(3)
		IoT_check_connect += 1
		if(IoT_check_connect > 5): 
			break
			
	blnInternetCon = check_internet_connect()	
	print(blnInternetCon)
	
	if(check_internet_connect()	): 
		#print("Got an IoT internet connection.")
		print("------------------------------------")	
		my_logger.info( "Got an IoT internet connection - Online.")
		
		cmd_restart = 'sudo systemctl restart systemd-timesyncd.service'
		ret_int = os.system( cmd_restart )
		#ret_int = os.system( cmd_restart )
		#ret_int = os.system( 'sudo systemctl status systemd-timesyncd.service' )
		if(ret_int == 0):
			my_logger.info("systemd-timesyncd.service restarted.")
			#print("systemd-timesyncd.service status.")
			
		cmd_reload = 'sudo systemctl daemon-reload'
		ret_int = os.system( cmd_reload )
		if(ret_int == 0):
			my_logger.info("daemon-reload reloaded.")
						
		
		time.sleep(3)
		print("------------------------------------")
		
		cmd_status = 'date' #'sudo systemctl status systemd-timesyncd.service'
		ret_int = os.system( cmd_status )
		ret_msg = subprocess.check_output( cmd_status )
		if(ret_int == 0):
			my_logger.info("date after resync: {}".format(ret_msg.decode("utf-8")))
			#print("systemd-timesyncd.service status.")
			
		#time.sleep(3)
	else:
		#print("Internet connection is not set! - Not Online")
		my_logger.error("Internet connection is not set! - Not Online.")


if __name__ == "__main__":
	
	rtc_update()


