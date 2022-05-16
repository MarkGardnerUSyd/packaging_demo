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

## Windows cmd commands

