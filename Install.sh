#!/bin/bash
cd /usr/share/
sudo mkdir Beta-Launcher
cd Beta-Launcher	
sudo git clone -b installable https://github.com/SiebenCorgie/Beta-Launcher.git
sudo cp /usr/share/Beta-Launcher/Beta-Launcher /usr/share/
chmod +x /usr/share/Beta-Launcher
sudo cp /usr/share/Beta-Launcher/UnrealEngine.desktop /usr/share/applications
cd /etc
mkdir Beta-Launcher
cd Beta-Launcher
cp /usr/share/Beta-Launcher/settings.conf /etc/Beta-Launcher
cp /usr/share/Beta-Launcher/defaults.conf /etc/Beta-Launcher
sudo chmod 666 settings.conf
sudo chmod +r defaults.conf
cd /usr/share/applications
sudo chmod +x UnrealEngine.desktop
