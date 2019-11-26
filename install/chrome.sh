#!/bin/bash

function install_chromium() {
	sudo apt-get install -y chromium
}
function instruction_chrome() {
	echo -e "If you want to install google-chrome, please follow instructions\n"
	echo -e "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\n"
	echo -e "sudo apt install ./google-chrome-stable_current_amd64.deb\n"
}


echo -e "Check if google-chrome is installed\n"


which google-chrome
if [ $? == 0 ]
then
	echo -e "Ok google-chrome is installed, get chromedriver\n"
	if [ -f chromedriver ]
	then
		echo -e "Delete previous chromedriver\n"
		sudo rm chromedriver
	fi
	if [ -f chromedriver_linux64.zip ]
	then
		echo -e "Delete zip file\n"
		sudo rm chromedriver_linux64.zip
	fi

	echo -e "Get chromedriver version 78.0.3904.11 Linux 64\n"
	wget https://chromedriver.storage.googleapis.com/78.0.3904.11/chromedriver_linux64.zip
	echo -e  "Unzip chromedriver_linux64.zip \n"
	unzip chromedriver_linux64.zip
	echo -e  "Delete zip file \n"
	rm chromedriver_linux64.zip
else
	echo -e "google-chome is not installed"
	read -p "Do you want to install chromemium ? Y/y N/n " value
	case $value in
	  [Yy]*) echo -e "Ok, install chromemium" && install_chromium ;;
	  [Nn]*) echo -e "Ok, follow instruction , or use Firefox Webdriver" && instruction_chrome && exit 0 ;;
	esac

fi






