#!/bin/bash

function dl_gecko () {
	echo -e "Get geckodriver\n" && wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
	echo -e "Untar geckodriver\n" && tar xvf geckodriver-v0.26.0-linux64.tar.gz
	echo -e "Delete tar file\n" && rm -r geckodriver-v0.26.0-linux64.tar.gz
}

function where_install () {
	read -p "Where do you want copy geckodriver ? /usr/local/bin (1) || /usr/bin (2)     " response
	case $response in
	  1) echo -e "Ok, copy to /usr/local/bin\n" && sudo cp  geckodriver /usr/local/bin && rm geckodriver && echo -e "geckodriver was copied in /usr/local/bin \n";;
          2) echo -e "Ok, copy to /usr/bin\n" && sudo cp geckodriver /usr/bin && rm geckodriver && echo -e "gechodriver was copied in /usr/bin\n" ;; 
	  *) echo -e "Please select 1 or 2 \n" ;;
	esac
}

echo -e "Install Firefox webdriver for selenium\n"
echo -e "The webdriver is named geckodriver\n"

read -p  "Do you want install geckodriver ? Yy/Nn " value
	case $value in
	  [Yy]*) dl_gecko && where_install ;;
	  [Nn]*) echo -e "Ok, do nothing" && exit 0;;
	esac


