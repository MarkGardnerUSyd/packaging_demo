# Environment set up

All the packages required to complete this tutorial are defined in [here](https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements).

Copy this file into a file called dev_requirements.txt, and install with:

```
pip install -r dev_requirements.txt
```

I recomend you start this tutorial with a clean (empty) virtual environment but this is not technically required, as long as the required packages exist in your environme.

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

Pycharm usually manages environments in Windows quite well.
However, if you would prefer to not use PyCharm, here are instructions for getting started with the Windows command line (cmd) or Powershell.
Generally, the commands below will work for both cmd and Powershell, unless specified.

To open a command window anywhere from file explorer, just type ```cmd``` in the address bar and press enter.

1. Create a new virtual environment (venv) using the full path to the new location, e.g
    ```bat
    python -m venv C:\Users\bwhe3635\Documents\temp\new_venv
    ```
    If this raises an error, try typing just `python` into the prompt.
    If you get a similar error (`python is not recognized as...`), then it is likely the `python.exe` cannot be found.
    See the below section on troubleshooting for help.

2. Activate the venv by typing the full path to the activate script
    ```bat
    C:\Users\bwhe3635\Documents\temp\new_venv\Scripts\activate
    ```

3. make a new directory for your new repo:
    ```bat
    mkdir C:\Users\bwhe3635\Documents\temp\new_repo
    cd C:\Users\bwhe3635\Documents\temp\new_repo
    ```

4. Download the requirements file:
    * cmd:
        ```bat
        curl -L https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements --output dev_requirements.txt
        ```
    * Powershell: 
        ```powershell
        Invoke-WebRequest -URI https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements -OutFile dev_requirements.txt
        ```

5. Install requirements through `pip`
    ```bat
    pip install -r dev_requirements.txt
    ```

6. Initialise the git repository
    ```bat
    git init
    ```

At this point, you will have a terminal set up that you can complete the rest of this tutorial with. 

So far I can't get a terminal working in VS code.
