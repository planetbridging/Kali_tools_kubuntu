import os
import sys, traceback
import subprocess
import os.path



class objInstaller:
	def __init__(self):
		print("Welcome to security tools installer for ubuntu")
		self.failed = []
		self.full_total = 0
		self.AllPackages = [
		'information_gathering', 'vulnerability_analysis',
		'wireless_attacks', 'web_applications',
		'exploitation_tools', 'stress_testing',
		'forensics_tools', 'sniffing_and_spoofing',
		'password_attacks', 'hardware_hacking',
		'reporting_tools', 'maintaining_access',
		'reverse_engineering']
		self.full_path = os.getcwd()
		self.Cmd_Loop()

	def Cmd_Loop(self):
		while True:
			i = input(">")
			if i == "quit":
				print("bubye")
				break
			elif i == "ca":
				self.Check_All()
			elif i == "ia":
				self.Install_all()

	def Check_All(self):
		full_count = 0
		total_count = 0
		for p in self.AllPackages:
			#p = self.AllPackages[0]
			file_path = self.full_path + "/" + p + ".txt"
			#print(os.path.isfile(file_path))
			file1 = open(file_path, 'r') 
			Lines = file1.readlines() 
			count = 0
			total = len(Lines)
			total_count += len(Lines)
			for line in Lines:
				if " " in line:
					print("unsure: " + line)
				else:
					a = self.Check_Install(line)
					if len(a) > 0:
						count += 1
						full_count += 1
			print("----------------------------------")
			print(p + " " + str(count) + "/" + str(total))
			print("----------------------------------")
		print("----------------------------------")
		print("complete " + str(count) + "/" + str(total_count))
		print("----------------------------------")
		

	def Install_all(self):
		for p in self.AllPackages:
			#p = self.AllPackages[0]
			file_path = self.full_path + "/" + p + ".txt"
			self.Install_Packages(file_path)
		self.Check_All()


#os.system('ls -l')


	def Check_Install(self,app):
		p = subprocess.Popen("dpkg -l |grep " + app, stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		p_status = p.wait()
		return output

	def Install_Packages(self,txt):
		
		file1 = open(txt, 'r') 
		Lines = file1.readlines() 
		
		count = 0
		linecount = len(Lines)
		# Strips the newline character 
		for line in Lines: 
			app = line.strip()
			if " " not in app:
				cmd = 'apt-get install ' + app + ' -y'
				if len(self.Check_Install(app)) == 0:
					os.system(cmd)
					check = self.Check_Install(app)
					if len(check) == 0:
						os.system(cmd.lower())

	
if __name__ == "__main__":
	newobj = objInstaller()
