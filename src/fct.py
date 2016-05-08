	
#functions for luncher main


#read default values on startup for later use
#test commi

def readdefaults():

	#make global variables
	
	global startlist
	global deflistc
	global newdict

	#create new dict for later use

	newdict = {}
	
	get = open("Beta_Launcher.conf", "r")

	#first define global variables
	
	startlist = []
	deflistc = 0

	for line in get:
		line = line.strip()
		startlist.append(str(line))
		deflistc = deflistc + 1

	get.close
#_______________________________________________________________________________

def name():
	name = "Beta Launcher"
	return name 
#_______________________________________________________________________________

def readconf(option, default):

	global deflistc
	global startlist
	
	conf = open("Beta_Launcher.conf", "r")

	#create data dictonary

	fconf={}

	for line in conf:
		line = line.strip()
		#split at space
		kv = line.split(" = ")
		fconf[kv[0]] = kv[1]
		#break when ending
		#get option value
		ret = fconf.get(option, default)

		ret = str(ret)
		
	conf.close
	
	return ret

#_____________________________________________________________________________
#create new list which gets apended to file


def newdi(option, newinput):

	global newdict

	#create new dict entry

	newdict[option] = str(newinput)
	


def writefile():
	global newdict
	confile = open("Beta_Launcher.conf", "w")


	#write new dictonary to file
	for lines in newdict:
		confile.write('{} = {}\n'.format(lines, newdict[lines]))

	confile.close()

def termlength(command):
	length = len(command) + 1
	return length

def termcommand(command):
	final = command + '\n'
	return final
