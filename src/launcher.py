#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-
#
# main.py
# Copyright (C) 2016 siebencorgie <siebencorgie@siebencorgie>
#
# Launcher is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Launcher is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
import gi.repository
gi.require_version('WebKit', '3.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GdkPixbuf, Gdk, WebKit
import os, sys, fct,subprocess


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/launcher.ui"
#UI_FILE = "/usr/local/share/launcher/ui/launcher.ui"


class GUI:
	
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')


		window.show_all()

		fct.readdefaults()
#updating startup values:
		#Install dialog
		Eloc = self.builder.get_object('E_Location')
		Eloc.set_text(fct.readconf('defloc','~/unrealengine'))
		

#HelpBrowser____________________________________________________________________

#initialise help browser
		helpurl = fct.readconf('defurl', 'https://docs.unrealengine.com/latest/INT/')

		helpbrowser = WebKit.WebView()
# To disallow editing the webpage. 
		helpbrowser.set_editable(False) 
#load url and show window
		helpbrowser.load_uri(helpurl)
		sw = self.builder.get_object('Help_Browser')
		sw.add(helpbrowser)
		helpbrowser.show()
		print('Opened')
		
#BlogBrowser____________________________________________________________________
		

		blogurl = fct.readconf('blogurl', 'https://www.unrealengine.com/blog')

#initialise blog browser
		blogbrowser = WebKit.WebView()
		
#disable editing
		blogbrowser.set_editable(False)
		
#load default URL
		blogbrowser.load_uri(blogurl)
		bsw = self.builder.get_object('Blog_Browser')
		bsw.add(blogbrowser)
		blogbrowser.show()

#Install____________________**********************______________________________		
#VersionHelper__________________________________________________________________
	def on_E_VerHelper_clicked (self, button):
		verhelper = self.builder.get_object('Version_Helper')
		verhelper.show()



	def on_B_Verhelper_Close_clicked (self, button):
		verhelper = self.builder.get_object('Version_Helper')
		verhelper.hide()



	
#AboutWindow________________________________________________________________
	#open about on click
	
	def on_B_about_activate (self, menuitem):
		about = self.builder.get_object('aboutdialog')
		#get name
		name=fct.name()
		about.set_program_name(name)
		about.get_program_name()
		about.show()

	#close about	
	def on_B_About_Close_clicked (self, button):
		
		about = self.builder.get_object('aboutdialog')
		about.hide()
#Libary_____________________________________________________________________
#load new image on changed location

	def on_UP_Chooser_file_set (self, filechooserbutton):
		global Uproject

		Path = self.builder.get_object('UP_Chooser')
		
		Uproject = Path.get_filename()
		print(str(Uproject))
		currentFolder = Path.get_current_folder()
		print('folder = ' + str(currentFolder))
		Image = self.builder.get_object('Libary_Image')
		Image.set_from_file(currentFolder + '/Saved/AutoScreenshot.png')
#Start of engine!!!
	def on_Engine_Start_clicked (self, button):
		subprocess.call('cd ' + fct.readconf('defloc' , '~/unrealengine') + ' && ./UE4Editor', shell=True)
		print('engine started!')


#Prefernces_________________________________________________________________

	def on_B_Edit_Dependencies_clicked (self, button):
		WinDep = self.builder.get_object('Dependencies_Dialog')
		WinDep.show()

	def on_B_Dep_Close_clicked (self, button):
		WinDep = self.builder.get_object('Dependencies_Dialog')
		WinDep.hide()

		
	def on_B_Preferences_activate (self, menuitem):
		#show main window 
		WinPref=self.builder.get_object('Win_Preferences')
		WinPref.show()

		#show dependecies
		WinDep = self.builder.get_object('Dependencies_Dialog')
		WinDep.show()
		WinDep.hide()

		#set all propertys
			#get them
		vulkan = self.builder.get_object('TB_Vulkan')
		version = self.builder.get_object('E_Version')
		defloc = self.builder.get_object('FCB_DefLocation')
		defloclabel = self.builder.get_object('L_DefLoc')
		defengine = self.builder.get_object('E_Pref_StartEngine')
		defhelpurl = self.builder.get_object('E_Pref_HelpURL')
		stream = self.builder.get_object('TB_Web')
		blogurl = self.builder.get_object('E_Blog_Url')
		#geting values 

		Vvulkan = fct.readconf('vulkan' , '0')
		Vversion = fct.readconf('version' , '4.10')
		Vdefloc = fct.readconf('defloc' , '~/unrealengine_teddy')
		Vdefengine = fct.readconf('defeng' , '4.10')
		Vdefhelpurl = fct.readconf('defurl' , 'https://docs.unrealengine.com/latest/INT/')
		Vstream = fct.readconf('stream' , '0')




		#set them_______________________________________________________________

		if Vvulkan == "0" :
			vulkan.set_active(False)
		else:
			vulkan.set_active(True)

		#set default version number
		version.set_text(Vversion)
		
		#set default location
		defloclabel.set_text("default location is: " + Vdefloc)

		#set default engine
		defengine.set_text(Vdefengine)

		#set default help url
		defhelpurl.set_text(Vdefhelpurl)

		#set streaming property
		if Vstream == '1':
			stream.set_active(True)
		else:
			stream.set_active(False)

		#set blog url
		blogurl.set_text(fct.readconf('blogurl', 'https://www.unrealengine.com/blog'))
		

		#set Distro
		dist = fct.readconf('distibution', '4')

		print('dist = ' + dist)
		
		Edistribution = self.builder.get_object('CB_Distro')
		Edistribution.set_active(int(dist))

		#set depencies
		dependencies_Arch = self.builder.get_object('E_Dep_Arch')
		dependencies_Ubuntu = self.builder.get_object('E_Dep_Ubuntu')
		dependencies_Mint = self.builder.get_object('E_Dep_Mint')

		dependencies_Arch.set_text(fct.readconf('deparch', 'sudo pacman -S mono clang35 dos2unix cmake'))
		dependencies_Ubuntu.set_text(fct.readconf('depubuntu', 'sudo apt-get install build-essential mono-gmcs mono-xbuild mono-dmcs libmono-corlib4.0-cil libmono-system-data-datasetextensions4.0-cil libmono-system-web-extensions4.0-cil libmono-system-management4.0-cil libmono-system-xml-linq4.0-cil cmake dos2unix clang-3.5 libfreetype6-dev libgtk-3-dev libmono-microsoft-build-tasks-v4.0-4.0-cil xdg-user-dirs'))
		dependencies_Mint.set_text(fct.readconf('depmint', 'sudo apt-get install git build-essential clang-3.5 libglew-dev libcheese7 libcheese-gtk23 libclutter-gst-2.0-0 libcogl15 libclutter-gtk-1.0-0 libclutter-1.0-0  xserver-xorg-input-all'))
		
		#set GitURL and step commands
		git = self.builder.get_object('E_GitURL')
		s1 = self.builder.get_object('E_S1')
		s2 = self.builder.get_object('E_S2')
		s3 = self.builder.get_object('E_S3')
		s4 = self.builder.get_object('E_S4')

		git.set_text(fct.readconf('giturl', 'echo unknown step'))
		s1.set_text(fct.readconf('s1', 'echo unknown step'))
		s2.set_text(fct.readconf('s2', 'echo unknown step'))
		s3.set_text(fct.readconf('s3', 'echo unknown step'))
		s4.set_text(fct.readconf('s4', 'echo unknown step'))

		#additional steps arch and mint
		sar = self.builder.get_object('E_Pref_Arch_Com')
		sm1 = self.builder.get_object('E_Pref_mint_Clang')
		sm2 = self.builder.get_object('E_Pref_mint_SV')
		sm3 = self.builder.get_object('E_Pref_mint_ED')
		
		sar.set_text(fct.readconf('steparch', 'echo unknown step'))
		sm1.set_text(fct.readconf('stepmint', 'echo unknown step'))
		sm2.set_text(fct.readconf('stepmintslate', 'echo unknown step'))
		sm3.set_text(fct.readconf('stepminteditor', 'echo unknown step'))


		print('prefences updated!')

#saving new properties

	def on_B_Pref_Save_clicked (self, button):
#change prefences
#get all the information

		#page 1
		Evulkan = self.builder.get_object('TB_Vulkan')
		Eversion = self.builder.get_object('E_Version')
		Edefloc = self.builder.get_object('FCB_DefLocation')
		Edefloclabel = self.builder.get_object('L_DefLoc')
		Edefengine = self.builder.get_object('E_Pref_StartEngine')
		Edefhelpurl = self.builder.get_object('E_Pref_HelpURL')
		Eblogurl = self.builder.get_object('E_Blog_Url')
		Estream = self.builder.get_object('TB_Web')
		#page 2
		Edistribution = self.builder.get_object('CB_Distro')
		#dialog
		dependencies_Arch = self.builder.get_object('E_Dep_Arch')
		dependencies_Ubuntu = self.builder.get_object('E_Dep_Ubuntu')
		dependencies_Mint = self.builder.get_object('E_Dep_Mint')
		#enddialog
		Egit = self.builder.get_object('E_GitURL')
		Es1 = self.builder.get_object('E_S1')
		Es2 = self.builder.get_object('E_S2')
		Es3 = self.builder.get_object('E_S3')
		Es4 = self.builder.get_object('E_S4')
		#additional steps
		Esar = self.builder.get_object('E_Pref_Arch_Com')
		Esm1 = self.builder.get_object('E_Pref_mint_Clang')
		Esm2 = self.builder.get_object('E_Pref_mint_SV')
		Esm3 = self.builder.get_object('E_Pref_mint_ED')
#write the stuff to a dictonary
#page 1
		#vulkan
		if Evulkan.get_active() == True:
			fct.newdi('vulkan', str(1))
		else:
			fct.newdi('vulkan', str(0))

		#version
		fct.newdi('version', str(Eversion.get_text()))

		#default location
		
		if Edefloc.get_filename() == None:
			fct.newdi('defloc', fct.readconf('defloc' , '~/unrealengine'))
		else:
			fct.newdi('defloc',Edefloc.get_filename())

#page 2
		#default engine
		fct.newdi('defeng',Edefengine.get_text())

		#default help url
		fct.newdi('defurl',Edefhelpurl.get_text())

		#streaming?

		if Estream.get_active() == True:
			fct.newdi('stream','1')
			print('stream true')
		elif Estream.get_active() == False:
			print('stream false')
			fct.newdi('stream','0')

		#blogurl
		fct.newdi('blogurl' , Eblogurl.get_text())

#page 3
		#distro
		dID = Edistribution.get_active_text()

		if dID == 'Arch Linux':
			fct.newdi('distibution', str(0))
		elif dID == 'Ubuntu':
			fct.newdi('distibution', str(1))
		elif dID == 'Mint':
			fct.newdi('distibution', str(2))
		else:
			fct.newdi('distibution', str(3))

		#dpendencies
		#dependecies text vault:
		fct.newdi('deparch',dependencies_Arch.get_text())
		fct.newdi('depubuntu',dependencies_Ubuntu.get_text())
		fct.newdi('depmint',dependencies_Mint.get_text())
		fct.newdi('depunknown','dependencies_unknown')
		
		#git URL
		fct.newdi('giturl', Egit.get_text())

		#Step1
		fct.newdi('s1', Es1.get_text())
		#Step2
		fct.newdi('s2', Es2.get_text())
		#Step3
		fct.newdi('s3', Es3.get_text())
		#Step4
		fct.newdi('s4', Es4.get_text())	

#page 4
		#Arch s1
		fct.newdi('steparch', Esar.get_text())
		#mint s1
		fct.newdi('stepmint', Esm1.get_text())
		#mint s2
		fct.newdi('stepmintslate', Esm2.get_text())
		#mint s3
		fct.newdi('stepminteditor', Esm3.get_text())

#write to file

		fct.writefile()

		print('file written!')
		
#end of preferences ________________________________________________________		



#Other_______________________________________________________________________
	#helpclick

	def on_B_Help_InBrowser_clicked (self, button):

		#get property
		path = fct.readconf('defurl' , 'https://docs.unrealengine.com/latest/INT/')
		os.system("xdg-open " + path)

	#open blog url in brower
	def on_B_Blog_Browser_clicked (self, button):
	#open blog in browser
		url = fct.readconf('blogurl' , 'https://www.unrealengine.com/blog')
		os.system('xdg-open ' + url)
		
	

	#close
	def on_B_Quit_activate (self, menuitem):
		Gtk.main_quit()

	#closing prefences via x button
	def on_Win_Preferences_destroy (self, widget):
		WinPref=self.builder.get_object('Win_Preferences')
		print('hidden')
		WinPref.hide()
		
	#closing prefences via close button
	def on_B_Pref_Close_clicked (self, button):
		WinPref=self.builder.get_object('Win_Preferences')
		WinPref.hide()
		print('hidden')

#quit program
	def on_window_destroy(self, window):
		print('quit!')
		Gtk.main_quit()		



def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())