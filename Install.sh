#!/bin/bash
cd /opt
sudo git clone https://github.com/SiebenCorgie/Beta-Launcher.git
sudo cp /opt/Beta-Launcher/Beta-Launcher /bin
sudo cp /opt/Beta-Launcher/UnrealEngine.desktop /usr/share/applications
cd /opt/Beta-Launcher
sudo chmod 666 settings.conf
sudo chmod +r defaults.conf
cd /bin 
sudo chmod +x Beta-Launcher
cd /usr/share/applications
sudo chmod +x UnrealEngine.desktop
