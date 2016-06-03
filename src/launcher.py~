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

#try to import VTE 2.90 for older distros, else import v. 2.91

try:
	gi.require_version('Vte', '2.90')
	VTEver = 290
except:
	gi.require_version('Vte', '2.91')
	VTEver = 291

from gi.repository import Gtk, GdkPixbuf, Gdk, Vte, GLib
from gi.repository.GdkPixbuf import Pixbuf
import os, sys, fct, subprocess, time

#set some paths
if fct.anjuta() == True:
	UIFILE = 'src/launcher.ui'
	PIXMAP = 'src/pixmaps/MainSymbol.png'
else:
	UIFILE = "/usr/share/beta-launcher/src/launcher.ui"
	PIXMAP = '/usr/share/beta-launcher/src/pixmaps/MainSymbol.png'

#updating startup values:
fct.readdefaults()
if fct.readconf('stream') == '1':
	from gi.repository import WebKit
else:
	print("Not Importing Webkit!")

#ENDED BEVORE RUNNING===========================================================
#START_GUI______________________________________________________________________

class GUI:
	
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UIFILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')
#show main window

		window.show_all()

		global Uproject
		Uproject = None
		global ProjectList
		ProjectList = None
		
#Init_Install___________________________________________________________________
#Init_Editor_Window
		Editor_WW = self.builder.get_object('Editor_Working')
		
#init Editor VTE
		EDITORVTE = self.builder.get_object('VTE_Editor')
		self.Editor_terminal     = Vte.Terminal()

#decide the vte version
		if VTEver == 290:
			
			self.Editor_terminal.fork_command_full(
				Vte.PtyFlags.DEFAULT,
				os.environ['HOME'],
				["/bin/sh"],
				[],
				GLib.SpawnFlags.DO_NOT_REAP_CHILD,
				None,
				None,
				)
			print("old VTE used! (v 2.90) *WINDOW_INIT*")
		else:
			
			self.Editor_terminal.spawn_sync(
				Vte.PtyFlags.DEFAULT,
				os.environ['HOME'],
				["/bin/sh"],
				[],
				GLib.SpawnFlags.DO_NOT_REAP_CHILD,
				None,
				None,
				)
			print("New VTE Used () v. 2.91 *WINDOW_INIT*")
		
		EDITORVTE.add(self.Editor_terminal) 

		Editor_WW.show_all
		Editor_WW.hide()

#HelpBrowser____________________________________________________________________

#initialise help browser
		if fct.readconf('stream') == '1':
			helpurl = fct.readconf('defurl')

			helpbrowser = WebKit.WebView()
# To disallow editing the webpage. 
			helpbrowser.set_editable(False) 
#load url and show window
			helpbrowser.load_uri(helpurl)
			sw = self.builder.get_object('Help_Browser')
			sw.add(helpbrowser)
			helpbrowser.show()
			print('Opened help URL')
		else:
			print('Not Loading Internet URL (Learn Tab)')
		
#BlogBrowser____________________________________________________________________
		
		if fct.readconf('stream') == '1':
			blogurl = fct.readconf('blogurl')

#initialise blog browser
			blogbrowser = WebKit.WebView()
		
#disable editing
			blogbrowser.set_editable(False)
		
#load default URL
			blogbrowser.load_uri(blogurl)
			bsw = self.builder.get_object('Blog_Browser')
			bsw.add(blogbrowser)
			blogbrowser.show()
		else:
			print('Not Loading Internet URL (BLOG)')

#Marketplace
		if fct.readconf('stream') == '1':
			mpurl = fct.readconf('mpurl')
			mpbrowser = WebKit.WebView()

			mpbrowser.set_editable(False)
			mpbrowser.load_uri(mpurl)
			mpwin = self.builder.get_object('SW_Marketplace')
			mpwin.add(mpbrowser)
			mpbrowser.show()
		else:
			print("Not Loading Internet URL (MARKETPLACE)")

#UpdateSymbol
		Symbol = self.builder.get_object('MAIN_Launcher_Symbol')
		Symbol.set_from_file(PIXMAP)

#add text to textbuffer
		vTextbuffer = self.builder.get_object('VersionTextBuffer')
		BufferTextList = fct.get_folder_content(str(fct.readconf('defloc')))
		items = len(BufferTextList)
		finaltext = ''
		for itemcount in range(items):
			finaltext = finaltext + str('Unreal Branch: ' + str(BufferTextList[itemcount]) + '\n' )
		vTextbuffer.set_text(finaltext)

#ShowStartup on first start
		if fct.readconf('firststart') == '1':
			startwin = self.builder.get_object('FirstStartupMessage')
			startwin.show_all()
			fct.newdi('firststart', '0')
		else:
			print('not showing firststart')

#make the library list__________________________________________________________

		#make the iconview plus liststore

		ProjectList = fct.get_folder_content(fct.readconf('proloc'))
		projectstore = Gtk.ListStore(GdkPixbuf.Pixbuf, str)
		
		LibraryView = self.builder.get_object('LibraryIconView')
		LibraryView.set_model(projectstore)
		LibraryView.set_pixbuf_column(0)
		LibraryView.set_text_column(1)

		#create the etrys
		for i in range(len(ProjectList)):
			pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(str(str(fct.readconf('proloc') + '/' + str(ProjectList[i]) + '/Saved/AutoScreenshot.png')), 64, 64)
			projectstore.append([pixbuf , ProjectList[i]])
			

#ENDED INITIALISING
#Install========================================================================		
#Install_Dialog_________________________________________________________________		
#show install dialog
	def on_B_Install_clicked (self, button):
		instwin = self.builder.get_object('Install_Dialog')
#init VTE
		termwin = self.builder.get_object('VTE')

		self.term     = Vte.Terminal()

#decide the vte version

		if VTEver == 290:
			
			self.term.fork_command_full(
				Vte.PtyFlags.DEFAULT,
				os.environ['HOME'],
				["/bin/sh"],
				[],
				GLib.SpawnFlags.DO_NOT_REAP_CHILD,
				None,
				None,
				)
			print("old VTE used! (v 2.90) *WINDOW_INSTALLDIALOG*")
		else:
			
			self.term.spawn_sync(
				Vte.PtyFlags.DEFAULT,
				os.environ['HOME'],
				["/bin/sh"],
				[],
				GLib.SpawnFlags.DO_NOT_REAP_CHILD,
				None,
				None,
				)
			print("New VTE Used (v. 2.91) *WINDOW_INSTALLDIALOG*")
			
		termwin.add(self.term)
		instwin.show_all()
#set texts______________________________________________________________________

#default location
		defaultlocation =  self.builder.get_object('E_Install_DefLoc')
		defaultlocation.set_text(fct.readconf('defloc'))	

#Dependecies
		deps = self.builder.get_object('E_Install_Dependencies')
		distroversion = fct.readconf('distribution')
		print("distro = " + str(distroversion))
		if distroversion == '0':
			deps.set_text(str(fct.readconf('deparch')))
		elif distroversion == '1':
			deps.set_text(str(fct.readconf('depubuntu')))	
		elif distroversion == '2':
			deps.set_text(str(fct.readconf('depmint')))
		else:
			deps.set_text('Unknown distribution,please check settings!')

#set text in "Download
		EditGit = self.builder.get_object('E_Install_GitHub')
		EditConfig = self.builder.get_object('E_Install_Config')
		EditSlate = self.builder.get_object('E_Install_SlateViewer')
		SlateCheck = self.builder.get_object('CB_SlateCheck')
		#set texts
		EditGit.set_text(str(fct.readconf('giturl')))
		EditConfig.set_text(str(fct.readconf('s1')))
		EditSlate.set_text(str(fct.readconf('s2')))

#set text in "Build"
		ES3 = self.builder.get_object('E_Install_S3')
		ES4 = self.builder.get_object('E_Install_S4')
		infolabel = self.builder.get_object('L_Install_Info')
		if fct.readconf('distribution' ) == '0':
			infolabel.set_text('  Please add "export PATH=$HOME/bin:$PATH" to your \n  .bashrc or .zshrc in your home folder before \n  continuing.\n')
		else:
			print("leaving arch info out")

		ES3.set_text(fct.readconf('s3'))
		ES4.set_text(fct.readconf('s4'))

#install depencies
	def on_B_Install_Dep_clicked (self, button):
		text = self.builder.get_object('E_Install_Dependencies')
		#printing wait window and reading terminal
		command = text.get_text()
		self.term.feed_child(fct.termcommand(command), fct.termlength(command))

#Download Engine and (optional) make SlateCheck
	def on_B_Install_DownloadEngine_clicked (self, button):
		#get all options
		Link = self.builder.get_object('E_Install_GitHub')
		S1 = self.builder.get_object('E_Install_Config')
		wait = self.builder.get_object('wait_dialog')
		version_number = self.builder.get_object('E_Install_number')
		version_typ = self.builder.get_object('CB_Branch')
		infolabel = self.builder.get_object('L_Install_Info')
		expander_Download = self.builder.get_object('Install_Exp_Download')
		expander_Configure = self.builder.get_object('Install_Exp_Configure')
		#set some variables
		branch = version_typ.get_active_text()
		version_number = version_number.get_text()
#fixing Linkingproblem on Arch
		if fct.readconf('distribution' ) == '0':
			LinkArch = fct.readconf('steparch')
			infolabel.set_text('please add "export PATH=$HOME/bin:$PATH" to your \n .bashrc or .zshrc in your home folder.')
		else:
			LinkArch = 'echo leaving ArchLinking out ... not on arch'
		self.term.feed_child(fct.termcommand(LinkArch), fct.termlength(LinkArch))
		
		
		#cd in directory
		CDcommand = 'cd ' + str(fct.readconf('defloc'))
		self.term.feed_child(fct.termcommand(CDcommand), fct.termlength(CDcommand))
		#delete old directory
		if branch == 'by_version':
			DelDircommand = 'rm -rf ' + str(version_number)
		else:
			DelDircommand = 'rm -rf ' + str(branch)
		self.term.feed_child(fct.termcommand(DelDircommand), fct.termlength(DelDircommand))
		#make new directory
		if branch == 'by_version':
			MKDircommand = 'mkdir ' + str(version_number)
		else:
			MKDircommand = 'mkdir ' + str(branch)
		self.term.feed_child(fct.termcommand(MKDircommand), fct.termlength(MKDircommand))	
		#cd in new made directory
		if branch == 'by_version':
			CDNEWcommand = 'cd ' + str(version_number)
		else:
			CDNEWcommand = 'cd ' + str(branch)
		self.term.feed_child(fct.termcommand(CDNEWcommand), fct.termlength(CDNEWcommand))		

		#make install command
		print("branch = " + str(branch))

		if branch == 'by_version':
			Gitcommand = 'git clone -b '  + str(version_number) + ' ' + str(Link.get_text())
		else:
			Gitcommand = 'git clone -b ' + str(branch) + ' ' + str(Link.get_text())
		print(str('donwload command: ' + Gitcommand))
		#print to terminal
		self.term.feed_child(fct.termcommand(Gitcommand), fct.termlength(Gitcommand))		

		expander_Download.set_expanded(False)
		expander_Configure.set_expanded(True)

#Configuring
	def on_B_Configure_clicked (self, button):
		# after cloning
		Slate = self.builder.get_object('E_Install_SlateViewer')
		SlateCheck = self.builder.get_object('CB_SlateCheck')
		expander_Download = self.builder.get_object('Install_Exp_Download')
		expander_Configure = self.builder.get_object('Install_Exp_Configure')
		#cd into new unrealengine directory
		print("cd in new directory")
		UECDcommand = 'cd UnrealEngine' 
		self.term.feed_child(fct.termcommand(UECDcommand), fct.termlength(UECDcommand))
		print("run setup")
		#run step one commands
		S1command = str(fct.readconf('s1'))
		self.term.feed_child(fct.termcommand(S1command), fct.termlength(S1command))
#make slate if ticked "yes"
		if SlateCheck.get_active() == True:
			SLATEcommand = fct.readconf( 's2' )
		else:
			SLATEcommand = 'echo passing_slate!'
		self.term.feed_child(fct.termcommand(SLATEcommand), fct.termlength(SLATEcommand))	
#linking clang and clang++ and linking slate  when on mint 
#linking clang
		if SlateCheck.get_active() == True:				
			if fct.readconf('distribution') == '2':
				print("linking clang and slate")
				SlateCommand = fct.readconf('stepmintslate')				
				ClangCommand = fct.readconf('stepmint')
				ClangCommand_Slate = './SlateViewer'
			else:
				print('not linking clang and slate')
				ClangCommand = "echo passing_clang_link_for_mint"
				SlateCommand = "echo passing_slate_link_for_mint"
				ClangCommand_Slate = 'echo passing_first_slate_execute_no_on_mint'
				
			self.term.feed_child(fct.termcommand(SlateCommand), fct.termlength(SlateCommand))	
			self.term.feed_child(fct.termcommand(ClangCommand), fct.termlength(ClangCommand))
			self.term.feed_child(fct.termcommand(ClangCommand_Slate), fct.termlength(ClangCommand_Slate))
		else:
			comment = 'echo passing_linking_of_clang_and_slate_not_on_Mint'
			self.term.feed_child(fct.termcommand(comment), fct.termlength(comment))	

		expander_Download.set_expanded(True)
		expander_Configure.set_expanded(False)
#Ending "Download"

#Starting "Building"
	def on_B_Install_Build_clicked (self, button):
		ES3 = self.builder.get_object('E_Install_S3')
		ES4 = self.builder.get_object('E_Install_S4')
		Editing = self.builder.get_object('CB_Install_ChangeBuildSettings')
		version_number = self.builder.get_object('E_Install_number')
		version_typ = self.builder.get_object('CB_Branch')
		#set some variables
		branch = version_typ.get_active_text()
		version_number = version_number.get_text()

		#editing xml
		#making path
		if Editing.get_active() == True:
			if branch == 'by_version':
				EDITPath = 'gedit ' + str(fct.readconf('defloc') + '/' + str(version_number) + '/UnrealEngine' + '/Engine/Saved/UnrealBuildTool/BuildConfiguration.xml')
				print(EDITPath)
			else:
				EDITPath = 'gedit ' + str(fct.readconf('defloc') + '/' + str(branch) + '/UnrealEngine' +  '/Engine/Saved/UnrealBuildTool/BuildConfiguration.xml')
				print(EDITPath)
			self.term.feed_child(fct.termcommand(EDITPath), fct.termlength(EDITPath))
		else:
			print('leaving xml editing out')
		#getting the text and printing to terminal
		Step3 = ES3.get_text()
		Step4 = ES4.get_text()

		print("beginning step 3")
		self.term.feed_child(fct.termcommand(Step3), fct.termlength(Step3))
		print('ending step 3')
		print('beginning step 4')
		self.term.feed_child(fct.termcommand(Step4), fct.termlength(Step4))	
		print('ending step 4')
#link Editor on Mint
		if fct.readconf('distribution') == '2':
			LinkEditorCommand = fct.readconf('stepminteditor')
		else:
			LinkEditorCommand = 'echo leaving Editor linking out ... not on mint'
		self.term.feed_child(fct.termcommand(LinkEditorCommand), fct.termlength(LinkEditorCommand))	
		
#close waiting dialog
	def on_B_install_Wait_Close_clicked (self, button):
		wait = self.builder.get_object('wait_dialog')
		wait.hide()		

			
#cancel install
	def on_B_Install_Cancel_clicked (self, button):
		instwin = self.builder.get_object('Install_Dialog')
		notebook = self.builder.get_object('install_note')
#reseting view
		notebook.set_current_page(0)
		instwin.hide()

#clicking next
	def on_B_Install_Next_clicked (self, button):
		notebook = self.builder.get_object('install_note')
		notebook.next_page()

#clicking help
	def on_B_Install_Help_clicked (self, button):
		insthelp = self.builder.get_object('Install_Help')
		insthelp.show()

#close help
	def on_B_install_help_Close_clicked (self, button):
		insthelp = self.builder.get_object('Install_Help')
		insthelp.hide()		


#Libary_____________________________________________________________________
#load new image on changed location

#Closing Engine_Run_Dialog
	def on_B_Engine_Working_Close_clicked (self, button):
		Runwin = self.builder.get_object('Editor_Working')
		Runwin.hide()
		


#Updating Project
	def on_UP_Chooser_file_set (self, filechooserbutton):
		global Uproject

		Path = self.builder.get_object('UP_Chooser')
		
		Uproject = Path.get_filename()
		print(str(Uproject))
		currentFolder = Path.get_current_folder()
		print('folder = ' + str(currentFolder))
		Image = self.builder.get_object('Libary_Image')
		Image.set_from_file(currentFolder + '/Saved/AutoScreenshot.png')
		ProjectName = self.builder.get_object('E_ProjectName')
		ProjectName.set_text(str(Path.get_preview_filename))

#Start of engine!!!
	def on_Engine_Start_clicked (self, button):
		global Uproject

		EngineBranch = self.builder.get_object('CB_Start_Version')		
		Engine = self.builder.get_object('E_Version_Start')
		LaunchProject = self.builder.get_object('UP_Chooser')
		enginwin = self.builder.get_object('Editor_Working')
		#pass to terminal
		Branch = EngineBranch.get_active_text()
		version = Engine.get_text()
		LP = LaunchProject.get_filename()
		Project = Uproject

#making executing command

		C1 = 'cd '
		C2 = str(fct.readconf('defloc')) + '/'

		#Engine type
		if Branch == 'by_version':
			C3 = str(version) + '/UnrealEngine' + '/Engine/Binaries/Linux'
		else:
			C3 = str(Branch) + '/UnrealEngine' + '/Engine/Binaries/Linux'

		#primusrun
		if fct.readconf('primusrun' ) == '1':
			C4 = ' && PRIMUS_SYNC=1 primusrun ./UE4Editor'
		else:
			C4 = ' && ./UE4Editor'

		#LibaryEntry
		if LP == None:
			C5 = ' '
		else:
			C5 = ' "' + Uproject + '" '

		#Opengl4 or vulkan
		if fct.readconf('vulkan') == '1':
			C6 = '-vulkan -nosplash -windowed'
		else:
			if fct.readconf('opengl') == '1':
				C6 = '-opengl4'
			else:
				C6 = ' '

		Startpath = C1 + C2 + C3 + C4 + C5 + C6

		enginwin.show_all()
		print(Startpath)
		self.Editor_terminal.feed_child(fct.termcommand(Startpath), fct.termlength(Startpath))
		print('engine started!')
		


#Prefernces_________________________________________________________________
	#closing prefences via x button
	def on_Win_Preferences_destroy (self, widget):
		WinPref=self.builder.get_object('Win_Preferences')
		WinPref.hide()
		
	#closing prefences via close button
	def on_B_Pref_Close_clicked (self, button):
		WinPref=self.builder.get_object('Win_Preferences')
		WinPref.hide()

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
		primus = self.builder.get_object('TB_Primus')
		opengl = self.builder.get_object('CB_Opengl')
		version = self.builder.get_object('E_Version')
		defloc = self.builder.get_object('FCB_DefLocation')
		defloclabel = self.builder.get_object('L_DefLoc')
		defengine = self.builder.get_object('E_Pref_StartEngine')
		defhelpurl = self.builder.get_object('E_Pref_HelpURL')
		stream = self.builder.get_object('TB_Web')
		blogurl = self.builder.get_object('E_Blog_Url')
		mpurl = self.builder.get_object('E_MP_URL')

		projectlocation = self.builder.get_object('E_PREF_DefProj_Loc')
		startup = self.builder.get_object('Pref_CB_SSUA')
		#geting values 

		Vvulkan = fct.readconf('vulkan' )
		Vprimus = fct.readconf('primusrun' )
		Vopengl = fct.readconf('opengl')
		Vversion = fct.readconf('version')
		Vdefloc = fct.readconf('defloc')
		Vdefengine = fct.readconf('defeng')
		Vdefhelpurl = fct.readconf('defurl')
		Vstream = fct.readconf('stream')
		V_Projectloc = fct.readconf('proloc')
		V_startup = fct.readconf('firststart')




		#set them_______________________________________________________________
		#vulkan
		if Vvulkan == "0" :
			vulkan.set_active(False)
		else:
			vulkan.set_active(True)

		#primusrun
		if Vprimus == '0':
			primus.set_active(False)
		else:
			primus.set_active(True)

		#opengl4
		if Vopengl == '0':
			opengl.set_active(False)
		else:
			opengl.set_active(True)
		
		#set default version number
		version.set_text(Vversion)
		
		#set default location
		defloclabel.set_text("Default Location Is:\n" + Vdefloc)

		#set default engine
		defengine.set_text(Vdefengine)



		#set streaming property
		if Vstream == '1':
			stream.set_active(True)
		else:
			stream.set_active(False)
			
		#set default help url
		defhelpurl.set_text(Vdefhelpurl)
		#set blog url
		blogurl.set_text(fct.readconf('blogurl'))
		#set marketplace URL
		mpurl.set_text(fct.readconf('mpurl'))

		#default project location
		projectlocation.set_text('Default Location Is:\n' + V_Projectloc)
		
		
		#show startup again?
		if V_startup == '0':
			startup.set_active(False)
		else:
			startup.set_active(True)

		#set Distro
		dist = fct.readconf('distribution')

		print('dist = ' + dist)
		
		Edistribution = self.builder.get_object('CB_Distro')
		Edistribution.set_active(int(dist))

		#set depencies
		dependencies_Arch = self.builder.get_object('E_Dep_Arch')
		dependencies_Ubuntu = self.builder.get_object('E_Dep_Ubuntu')
		dependencies_Mint = self.builder.get_object('E_Dep_Mint')

		dependencies_Arch.set_text(fct.readconf('deparch'))
		dependencies_Ubuntu.set_text(fct.readconf('depubuntu'))
		dependencies_Mint.set_text(fct.readconf('depmint'))
		
		#set GitURL and step commands
		git = self.builder.get_object('E_GitURL')
		s1 = self.builder.get_object('E_S1')
		s2 = self.builder.get_object('E_S2')
		s3 = self.builder.get_object('E_S3')
		s4 = self.builder.get_object('E_S4')

		git.set_text(fct.readconf('giturl'))
		s1.set_text(fct.readconf('s1'))
		s2.set_text(fct.readconf('s2'))
		s3.set_text(fct.readconf('s3'))
		s4.set_text(fct.readconf('s4'))

		#additional steps arch and mint
		sar = self.builder.get_object('E_Pref_Arch_Com')
		sm1 = self.builder.get_object('E_Pref_mint_Clang')
		sm2 = self.builder.get_object('E_Pref_mint_SV')
		sm3 = self.builder.get_object('E_Pref_mint_ED')
		
		sar.set_text(fct.readconf('steparch'))
		sm1.set_text(fct.readconf('stepmint'))
		sm2.set_text(fct.readconf('stepmintslate'))
		sm3.set_text(fct.readconf('stepminteditor'))


		print('prefences updated!')

#saving new properties

	def on_B_Pref_Save_clicked (self, button):
#change prefences
#get all the information

		#page 1
		Evulkan = self.builder.get_object('TB_Vulkan')
		Eprimus = self.builder.get_object('TB_Primus')
		Eopengl = self.builder.get_object('CB_Opengl')
		Eversion = self.builder.get_object('E_Version')
		Edefloc = self.builder.get_object('FCB_DefLocation')
		Edefloclabel = self.builder.get_object('L_DefLoc')
		Edefengine = self.builder.get_object('E_Pref_StartEngine')
		Edefhelpurl = self.builder.get_object('E_Pref_HelpURL')
		Eblogurl = self.builder.get_object('E_Blog_Url')
		Estream = self.builder.get_object('TB_Web')
		Empurl = self.builder.get_object('E_MP_URL')
		E_proloc = self.builder.get_object('CB_PREF_DefProjLoc')
		E_startup = self.builder.get_object('Pref_CB_SSUA')
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

		#primus
		if Eprimus.get_active() == True:
			fct.newdi('primusrun' , '1')
		else:
			fct.newdi('primusrun' , '0')

		#opengl4
		if Eopengl.get_active() == True:
			fct.newdi('opengl', '1')
		else:
			fct.newdi('opengl','0')

		#version
		fct.newdi('version', str(Eversion.get_text()))

		#default location
		
		if Edefloc.get_filename() == None:
			fct.newdi('defloc', fct.readconf('defloc'))
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
		#marketplace url
		fct.newdi('mpurl' , Empurl.get_text())

		#projectlocation
		if E_proloc.get_filename() == None:
			print('passing new entry for default project location')
		else:
			fct.newdi('proloc' , E_proloc.get_filename())

		#startup
		if E_startup.get_active() == True:
			fct.newdi('firststart' , '1')
		else:
			fct.newdi('firststart' , '0')

#page 3
		#distro
		dID = Edistribution.get_active_text()

		if dID == 'Arch Linux':
			fct.newdi('distribution', str(0))
		elif dID == 'Ubuntu':
			fct.newdi('distribution', str(1))
		elif dID == 'Mint':
			fct.newdi('distribution', str(2))
		else:
			fct.newdi('distribution', str(3))

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

#close prefences
		prefs = self.builder.get_object('Win_Preferences')
		prefs.hide()
#end of preferences ________________________________________________________		

#AboutWindow________________________________________________________________
	#open about on click
	
	def on_B_about_activate (self, menuitem):
		about = self.builder.get_object('aboutdialog')
		#get name
		name=fct.name()
		about.set_program_name(name)
		about.get_program_name()
		about.show_all()

	#close about	
	def on_B_About_Close_clicked (self, button):
		
		about = self.builder.get_object('aboutdialog')
		about.hide()

#Other_______________________________________________________________________
#close startup window
	def on_B_FirstStartup_Close_clicked (self, button):
		startwin = self.builder.get_object('FirstStartupMessage')
		startwin.hide()

#helpclick
	def on_B_Help_InBrowser_clicked (self, button):
		path = fct.readconf('defurl')
		os.system("xdg-open " + path)

	#open blog url in brower
	def on_B_Blog_Browser_clicked (self, button):
	#open blog in browser
		url = fct.readconf('blogurl')
		os.system('xdg-open ' + url)
	#show building wiki
	def on_B_Install_Help_OpenWiki_clicked(seld, button):
		url = 'https://wiki.unrealengine.com/Building_On_Linux'
		os.system('xdg-open ' + url)

	#close
	def on_B_Quit_activate (self, menuitem):
		Gtk.main_quit()

	#open marketplace in browser
	def on_B_Marketplace_Open_clicked (self, button):
		os.system('xdg-open ' + fct.readconf('mpurl', 'https://google.com'))


#quit program
	def on_window_destroy(self, window):
		Gtk.main_quit()		



def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())
