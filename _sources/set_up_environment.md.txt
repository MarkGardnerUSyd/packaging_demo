# Environment set up

All the packages required to complete this tutorial are defined in [here](https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements).

Copy this file into a file called dev_requirements.txt, and install with:

```
pip install -r dev_requirements.txt
```

I recomend you start this tutorial with a clean (empty) virtual environment but this is not technically required, as long as the required packages exist in you.

## Linux terminal commands

```bash
# Create and activate new virtual environment
python3 -m venv new_venv  # you may have to install e.g. sudo apt install python3.10-venv, follow the prompts
source new_venv/bin/activate  # activate 'new_venv'

mkdir new_repo
cd new_repo
wget https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements dev_requirements.txt
pip install -r dev_requirements
git init # set this folder up as a git repository. If you create a new repo on github, it will tell you the commands needed to push this repository 
```

## Windows 

Note that I normally manage windows environments through pycharm, but if you don't do that you can do the following:

### cmd commands

To open a command window anywhere from file explorer, just type ```cmd``` in the address bar and press enter.

```bat
# open a cmd window where your python installation is, or else cd, e.g:
cd C:\Users\bwhe3635\AppData\Local\Programs\Python\Python310
# create a new venv using the full path to the new location, e.g
python -m venv C:\Users\bwhe3635\Documents\temp\new_venv
# activate the venv by typing the full path to the activate script
C:\Users\bwhe3635\Documents\temp\new_venv\Scripts\activate

# make a new directory for your new repo:
mkdir C:\Users\bwhe3635\Documents\temp\new_repo
cd C:\Users\bwhe3635\Documents\temp\new_repo
# download requirements file:
curl -L https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements --output dev_requirements.txt
# install requirements
pip install requirements.txt
# initialise repo
git init
```

At this point, you will have a terminal set up that you can complete the rest of this tutorial with. 

### PowerShell commands

> **Note:** Powershell seems to work ok by default in pycharm, not very well by itself or in VScode. I honestly don't know why Microsoft want everyone's life to be hard. 

```powershell
# environment set up: I do this through pycharm, so I haven't written this yet...

# this is to get the requirements file:
Invoke-WebRequest -URI https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements -OutFile dev_requirements.txt
# install:
pip install -r dev_requirements.txt
```



If you use pycharm, then it loads a powershell terminal in the correct environment by default. 

So far I can't get a terminal working in VS code.
