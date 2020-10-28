import os
import sys, traceback
import subprocess



#os.system('ls -l')
failed = []

def Check_Install(app):
	p = subprocess.Popen("dpkg -l |grep " + app, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()
	return output

def Install_Packages(txt):
	
	file1 = open(txt, 'r') 
	Lines = file1.readlines() 
	  
	count = 0
	linecount = len(Lines)
	# Strips the newline character 
	for line in Lines: 
		app = line.strip()
		cmd = 'apt-get install ' + app + ' -y'
		if len(Check_Install(app)) == 0:
			os.system(cmd)
			check = Check_Install(app)
			if len(check) == 0:
				os.system(cmd.lower())
				checkagain = Check_Install(app.lower())
				if len(checkagain) == 0:
					failed.append(app)


		#print(osout.len)
		count+=1
		#print( str(count) + "/" + str(linecount))
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

print("----------------------------------")
print("Finished!!!!")
print("----------------------------------")

for f in failed:
	print("Failed to install: " + f)
