	
#functions for luncher main


#read default values on startup for later use

import configparser
defaultsConfig = configparser.ConfigParser()
customConfig = configparser.ConfigParser()

def readdefaults():

	global defaultsConfig
	defaultsConfig.read('defaults.conf')
	
	
	global customConfig
	customConfig.read('settings.conf')

#_______________________________________________________________________________

def name():
	name = "Beta Launcher"
	return name 
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
	
	confile = open("settings.conf", "w")

	customConfig.write(confile)


	confile.close()

def termlength(command):
	length = len(command) + 1
	return length

def termcommand(command):
	final = command + '\n'
	return final
