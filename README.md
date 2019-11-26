# python_linkedin
Python script which connect your linkedin account and search people with keywords. After connection, a file result.csv is created and put all results in this file. :thumbsup: :thumbsup:


## Important

Script will be tested on Debian 10 with virtualenv. If you want to test without virtual env, please install Python 2.7. Not tested on Python => 3

To install virtualenv, use : 
```
sudo apt-get install -y virutalenv ( Debian, Kali, Ubuntu ) and do that : 

mkdir virtual
virtualenv virtual
source virtual/bin/activate
```

Environnement is good ! :clap:


## Python Requirements

You can use :
```
pip install -r requirements.txt
```
## Knowledges :bowtie:

To connect to your linkedin's account, you must remove the double authentication :smirk: ! Pay attention with that !

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
growh.py -i chrome
growh.py -i firefox

```
If you need help, use python ``` growth.py -h ``` or ``` growth.py --help ```



## TO DO LIST

[ ] Reaching all linkedin url and take informations about profile

[ ] Put in theses informations on the file result.csv
















