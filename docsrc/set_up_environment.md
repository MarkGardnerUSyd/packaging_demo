# Environment set up

All the packages required to complete this tutorial are defined in [here](https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements).

Copy this file into a file called dev_requirements.txt, and install with:

```
pip install -r dev_requirements.txt
```

I recommend you start this tutorial with a clean (empty) virtual environment but this is not technically required, as long as the required packages exist in your environment.

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

## Windows Command Line and PowerShell

PyCharm usually manages environments in Windows quite well. However, if you would prefer to not use PyCharm, here are instructions for getting started with the Windows command line (cmd) or PowerShell. Generally, the commands below will work for both cmd and PowerShell, unless specified.

To open a command window anywhere from file explorer, just type ```cmd``` in the address bar and press enter.

1. Create a new virtual environment (venv)
    ```bat
    python -m venv new_venv
    ```
    If this raises an error, try typing just `python` into the prompt. If you get a similar error (`...python is not recognized as...`), then it is likely the `python.exe` cannot be found. See the below section on troubleshooting for help.
    
2. Activate the venv by typing the full path to the activate script
    ```bat
    new_venv\Scripts\activate
    ```

3. make a new directory for your new repo:
    ```bat
    mkdir new_repo
    cd new_repo
    ```

4. Download the requirements file:
    * cmd:
        ```bat
        curl -L https://github.com/ACRF-Image-X-Institute/packaging_demo/raw/master/dev_requirements --output dev_requirements.txt
        ```
    * PowerShell: 
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

### Troubleshooting Windows Issues

* Can't find `python.exe`

    When python can't be found, it is usually because location of `python.exe` is not on the `PATH`. There are a few ways to fix this, and best practice depends on how you installed python:
    
    **Anaconda/conda**
    
    Anaconda comes with the Anaconda Prompt, which you can use instead of cmd. This will have python set up correctly.
    
    Alternatively, you can use conda environments:
    ```sh
    conda create -n python3 python
    conda activate python3
    ```
    
    **From the Python [website](https://www.python.org/)**

    If you have yet to install python, you can let the installer add the location of the python executable to `PATH`. 

    Select "Add Python to PATH" when installing:

    ![Adding python to `PATH` during installation](__resources/installing_python_windows.png)

    If Python is already installed, see the next part about adding python to `PATH`

    **Adding Python to `PATH`**

    Finally, regardless of how python is installed, you can always add it to `PATH`. This will make it available in cmd or PowerShell. This is a bit tricky as you need to find out where Python is installed. Common locations are:
    
    * `C:\Program Files\`
    * `C:\Program Files (x86)\`
    * `C:\Users\<username>\AppData\Local\`
    * `C:\Users\<username>\AppData\Local\Programs\`
    
    You will have to dig around in these locations for folders that may contain the python installation. You are looking for the full path to the folder containing `python.exe`. For example, if `python.exe` is located at `C:\path\to\python.exe`, you want `C:\path\to\`.
    
    Once you have the path, you add to `PATH` by:
    1. Search for "Edit the system environment variables" in the start menu, and open the top result.
    2. Click on "Environment Variables..."
    3. Under "User variables for <username>", select the variable named "Path" and click "Edit"
    4. In the new window, click "New", then copy the path you found into the field.
    5. Exit out of all menus by clicking "OK"
    
    Python should be available when a new PowerShell or cmd prompt is opened.

