## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = launcher.ui


## The main script
bin_SCRIPTS = launcher.py \
	fct.py

## Directory where .class files will be installed
launcherdir = $(pythondir)/launcher


launcher_PYTHON = \
	launcher.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
