#Github repository for Beta Launcher
## version 0.3 BETA ##

A small launcher project I started, to make compiling and using UE4 on Linux easier.
Things done so far:

Features:

-    Distributions: Ubuntu, Linux Mint, Arch Linux
-    Loading Unreal-Blog
-    Loading Unreal-Help page
-    Loading Marketplace page (by default its CG-Trader, because they also sell ".uasset" models. I did not choose the Unreal-Marketplace, because it is still not possible to buy stuff from there and download it to Linux)
-    Installing different versions of Unreal Engine
-    Loading projects from the Launcher
-    Start in OpenGl4 mode
-    Start in OpenGl3 mode (when openGL4 is disabled)
-   Start with Primus-run enabled (for Nvidia + Intel hybrid graphic solutions)
-    Disable webpage loading on start (disabled by default, for enabling, enable "stream")
-   Change Installation procedure to other distribution (ATM: Ubuntu, Mint, Arch)
-    Changing all the commands, which will be executed when installing the engine
-    Change the distribution specific commands
-    Last but not least: Save all options into a readable .conf file in the the main directory of the launcher
-    Create Desktop-File etc. from "Install.sh (see installation below)



Things I want to do in the future

-    get Vulkan working with the engine (you actually can try to enable Vulkan in the preferences menu, this will add the -vulkan option to the start-command. However, it does not start correctly on my system, but maybe I installed Vulkan the wrong way)
-    Add an option to make backups from project-folders, as well as restoring them
-    Add a small tool for combining one-channel Textures like hight-maps with three channel Textures like albedo-maps
-    Add a small tool for adding pre-made project-files (like base materials and blueprints) to existing new projects
-    to be continued 


**Installation:**

*Install Dependencies:*

Ubuntu/Mint: download .deb from the master branch and double klick the file!

Arch: Download the .tar.xz file from the master branch and install it via packman with `sudo pacman -U *filename*`

for more Information, please visit the [forum-post](https://forums.unrealengine.com/showthread.php?110795-Beta-Launcher-for-Linux&p=532928#post532928) on the Unreal forum!


[further information:]

Distribution I am writing on : Arch Linux
Started:  around Easter 2016
software needed to run: GTK 3.18+ , WebKit (PyWebKit), Python 3, Vte 2.91+ 

[Note about me:]

Please keep in mind that I learn Python since fall 2015, so the code will be far from perfect.
If you have questions feel free to contact me at siebencorgie@googlemail.com 

