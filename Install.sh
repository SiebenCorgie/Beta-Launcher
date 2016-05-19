#!/bin/bash
cd /usr/share/
echo moving_to_/usr/share	
sudo git clone -b installable https://github.com/SiebenCorgie/Beta-Launcher.git
cd Beta-Launcher
echo moved_to_it
sudo cp /usr/share/Beta-Launcher/Beta-Launcher /bin
echo Copyied_Beta-Launcher_to_/bin
sudo cp /usr/share/Beta-Launcher/UnrealEngine.desktop /usr/share/applications
echo Copied_DektopFile_To_/usr/share/applications
cd /etc
sudo mkdir Beta-Launcher
cd Beta-Launcher
sudo cp /usr/share/Beta-Launcher/settings.conf /etc/Beta-Launcher
sudo cp /usr/share/Beta-Launcher/defaults.conf /etc/Beta-Launcher
echo Copied_All_Conf_Files
sudo chmod 666 settings.conf
sudo chmod +r defaults.conf
cd /usr/share/applications
sudo chmod +x UnrealEngine.desktop
sudo chmod +x /bin/Beta-Launcher
echo changed_all_permissions
echo END
