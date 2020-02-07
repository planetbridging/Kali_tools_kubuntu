import os
import sys, traceback



#os.system('ls -l')



def Install_Packages(txt):

	file1 = open(txt, 'r') 
	Lines = file1.readlines() 
	  
	count = 0
	linecount = len(Lines)
	# Strips the newline character 
	for line in Lines: 
		cmd = 'apt-get install ' + line.strip() + ' -y'
		os.system(cmd)
		count+=1
		print( str(count) + "/" + str(linecount))
	print("----------------------------------")
	print(txt + " done")
	print("----------------------------------")

Install_Packages('information_gathering.txt')
Install_Packages('vulnerability_analysis.txt')
Install_Packages('wireless_attacks.txt')
Install_Packages('web_applications.txt')
Install_Packages('exploitation_tools.txt')
Install_Packages('stress_testing.txt')
Install_Packages('forensics_tools.txt')
Install_Packages('sniffing_and_spoofing.txt')
Install_Packages('password_attacks.txt')
Install_Packages('hardware_hacking.txt')
Install_Packages('reporting_tools.txt')
Install_Packages('maintaining_access.txt')
Install_Packages('reverse_engineering.txt')
