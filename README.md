# python_linkedin
Python script which connect your linkedin account and search people with keywords. After connection, a file result.csv is created and put all results in this file. :thumbsup: :thumbsup:

This script is automated from start to finish! You have nothing else to do :wink: :wink:

## Important

Script will be tested on Debian 10 with virtualenv. If you want to test without virtual env, please install Python 2.7. Not tested on Python => 3

To install virtualenv, use : 
```
pip install virtualenv ( Debian, Kali, Ubuntu ) and do that : 

mkdir virtual
virtualenv virtual
source virtual/bin/activate
```

Environnement is good ! :clap:

## Alert :exclamation: :exclamation: :exclamation:

The script may stop working if google detects the requests and sends you to the captcha page :cry: ! 

Sorry for the inconvenience.

### Update : Captcha detection

Script detect captcha, and tell you to solve it ! :smile: :smile: :smile:

## Python Requirements

You can use :
```
pip install -r requirements.txt
```
## Knowledges :bowtie:

To connect to your linkedin's account, you must remove the double authentication :smirk: ! Pay attention with that !

### Update :bowtie: :bowtie:

Script detect if you have a two step challenge, and tell you to enter the code. Then, Press ENTER on the script ! :smile: :smile:

## Usage of Python Script :

### Add credentials to parametre.py

Check parametre.py file to put your linkedin's credentials & to put keywords in url

### The script
This script allow 2 webdriver : Chrome and Firefox

To use correctly  growth.py, make this command :
```
python growth.py -d chrome 
OR
python growth.py -d firefox
```

If you need to install webdriver (chrome or firefox), you can use :
```
python growth.py -i chrome
python growth.py -i firefox

```

Attention, detection of OS is not implemented, I use apt-get install :expressionless: :expressionless: 

You can use ``` python growth -d chrome -o output.csv ``` to change the default csv file. Please, inform extension csv :sunglasses:

You can use ``` python growth -d chrome -s "site:linkedin.com/in AND python OR perl AND USA" ```. It replaces default parametre.py variable :yum: 

If you need help, use ``` python growth.py -h ``` or ``` python growth.py --help ```



## TO DO LIST

[X] Reaching all linkedin url and take informations about profile

[X] Put in theses informations on the file result.csv

[X] Detection of google captcha :weary:

[X] Add detection of Double authentication to add security ( interaction with script )

[ ] Detection of OS to install Chrome or Firefox webdriver


















