	
#functions for luncher main


import subprocess

#read default values on startup for later use

import configparser
defaultsConfig = configparser.ConfigParser()
customConfig = configparser.ConfigParser()

#set the return value to False to make it behave like in installed mode or to True to start from anjuta

def anjuta():
	VALUE = False
	return VALUE

def readdefaults():
	
	global defaultsConfig
	global customConfig

	if anjuta() == True:
		
		defaultsConfig.read('defaults.conf')
		
		customConfig.read('settings.conf')		
	else:
		
		defaultsConfig.read('/etc/beta-launcher/defaults.conf')
		
		
		customConfig.read('/etc/beta-launcher/settings.conf')

#_______________________________________________________________________________

def name():
	name = "Beta Launcher"
	return name 

def version():
	version = 'version 0.1'
#_______________________________________________________________________________

def readconf(option):
	
	global defaultsConfig
	global customConfig
	
	if not option in customConfig['main']:
		return defaultsConfig['main'][option]
	else:
		return customConfig['main'][option]

#_____________________________________________________________________________
#create new list which gets apended to file


def newdi(option, newinput):

	global customConfig

	#create new dict entry

	customConfig['main'][option]=str(newinput)
	


def writefile():
	global customConfig
	
	if anjuta() == True:
		confile = open("settings.conf", "w")
	else:
		confile = open("/etc/beta-launcher/settings.conf", "w")

	customConfig.write(confile)


	confile.close()

def termlength(command):
	length = len(command) + 1
	return length

def termcommand(command):
	final = command + '\n'
	return final

#makeList from folder 
def get_folder_content(location):

	try:
		final = []
		#call subprocess
		callcommand = 'ls ' + location
		subprocess.call(callcommand , shell=True)
		out = subprocess.check_output(callcommand, shell=True)
		#split list
		contentlist = out.split()
		item = 0
		for Byteitem in contentlist:
			#convert to string and add to final list
			bytestring = contentlist[item]
			Endstring = bytestring.decode('utf-8')
			final.append(Endstring)
			item = item+1
			if item == Byteitem:
				break
	except:
		final = ['location' , 'not' , 'found']
	return final

#execute a command
def execute_command(execommand , output):
	subprocess.call(execommand , shell=True)
	if output == True:
		return subprocess.check_output(execommand, shell=True)
	



	
