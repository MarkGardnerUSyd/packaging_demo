# GitHub workflows for continuous integration 

## Automate tests

Now we have our tests set up, we can make github run them whenever certain actions occur. A popular way to set this up is to run the tests whenever a pull request is made - that way you can see if that request breaks your code or not.

For this to be effective, it's a good idea to stop people pushing directly to the main branch (actually, this is probably a good idea in general.) This means that whenever changes are made, they are first pushed to a different branch, then the tests will be automatically run, and - if they pass - you can except the pull request. 

### Set up main branch protection

In github, make the following changes:

- Go settings, branches, branch protection, and add new rule
  - **hint:** your 'main' branch could be called "main" or "master", you have to check and update "branch name pattern" accordingly

![](C:/Users/Brendan/Documents/temp/packaging_demo/docsrc/__resources/branch_protection.PNG)

- check 'Require a pull request....'
- uncheck "require approvals"
- If you scroll down further, there is another box "Include administrators" - check that one too

![](C:/Users/Brendan/Documents/temp/packaging_demo/docsrc/__resources/branch_protection2.PNG)

### Locally: switch to a new branch

If you are currently on the 'main' branch on your local machine, this would be a good time to switch since in the future you won't be able to push from that branch anyway. So make a new branch called e.g. "development" and switch to it.

### set up automatic tests

- from github.com, click "actions" "new workflow":

![](C:/Users/Brendan/Documents/temp/packaging_demo/docsrc/__resources/Actions_1.PNG)

- search for python and choose 'python application' - this is a basic workflow that by default will checkout our main branch and run some tests on it. 

![](C:/Users/Brendan/Documents/temp/packaging_demo/docsrc/__resources/Actions_2.PNG)

- When you click configure, you will be taken to a yml file. you can have a read through this if you want, but for this tutorial replace it with the below:

```yaml
# run pytest

name: tests

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r dev_requirements

    - name: Test with pytest
      run: |
        pytest

```

Compared with the default we have tweaked this a little bit:

- We aren't using pylint, because to be honest it's doubtful my code would pass its very stringent tests!
- I've updated the requirements installation

Click ```start commit``` then ```propose changes```.

![](C:/Users/Brendan/Documents/temp/packaging_demo/docsrc/__resources/Actions_4.PNG)

Because we banned commits directly to the main branch, this will open a new branch, and make a pull request from this new branch into main. Click ```create pull request```. Note that the tests will now run automatically.

We haven't insisted that the tests pass before merging, but we could if we want.

### Add a workflow badge 

Add the following text to the readme, right next to the 'coverage' badge line:

```markdown
![test](https://github.com/ACRF-Image-X-Institute/packaging_demo/actions/workflows/run_tests.yml/badge.svg)
```

This produces a badge on our readme, so now people know that in addition to the fact that we have implemented some tests and have 100% coverage of our code base, they are running automatically - and passing!

### add a coverage report

We can also add a cool test coverage report to our pull requests. edit the yaml file with the below:

```YAML
    - name: Test with pytest
      run: |
        pytest --cache-clear --cov=app test/ > pytest-coverage.txt
    - name: Comment coverage
      uses: coroo/pytest-coverage-commentator@v1.0.2
```

## The green tick of approval

When you have some github workflows setup to run, git will display a either a yellow dot, green tick, or red cross next to the latest commit information

- yellow dot: actions are currently running
- red cross: latest commit caused something to fail
- green tick: all actions completed without issue

![](C:\Users\Brendan\Documents\temp\packaging_demo\docsrc\__resources\green_ticl.png)

If you see some open source code that 

- has tests
- has a workflow action to run those tests
- has a green tick indicating that they passed

then you can proceed to use the code with reasonable confidence that it works - after all, the testing process involves cloning and running the code, so you know that at the very least it works when the github action runs it. 

Conversely, when these things are missing, I tend to be a bit more careful about whether or not I want to use this code...

## Automate docs build

We [read previously](https://acrf-image-x-institute.github.io/packaging_demo/documentation.html) about how to set up sphinx. It's fine to build the docs manually during setup, but to be honest it gets a bit tedious after a while; every time you change the code you need to rebuild the docs, make sure the changes are committed, push them back... luckily there is an easy way to automate this entire process with github actions!  

The first parts of this job are exactly the same as the testing; we have to check our code out and install all necessary requirements. Therefore you can follow the steps from **set up automatic tests** above. 

Once you have your yaml file ready to edit, copy the below into it:

```yaml
name: build docs

on:
  push:
    branches:
      - master
  pull_request:

jobs:
  deploy:
    runs-on: ubuntu-20.04
    permissions:
      contents: write
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python3 -m pip install --upgrade pip
          pip install -r dev_requirements
      - name: build sphinx docs
        run: |
          cd docsrc
          make github
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: ${{ github.ref == 'refs/heads/master' }}
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

Note that under the **build sphinx docs** we execute two commands:

```bash
cd docsrc
make github
```

These are exactly the commands we use to manually build our docs!

Following this we are using the third party github application to [Github pages](https://github.com/marketplace/actions/github-pages-action) to publish the build docs to a new branch,

> :warning: For some reason, some 'main' branches on github are called main, and some are called master. I've spent way too long not being able to figure out why my github action wouldn't work and it turned out to be because I used the wrong branch name!

### update location where docs are hosted

Once you successfully get your docs to build automatically, and once your main branch has the 'green tick of approval' (remember that you have to wait now for the tests to re-run and the docs to build) you will find that you have  a new branch called gh-pages! **magic!**

We now have to tell github to host from this new branch. This just looks like the image below:

![](__resources/auto_docs.png)

The power of this is that whenever the code base changes, the docs will update to reflect those changes (as long as the doc strings are kept up to date, which is probably another coding club...). Similarly, now you just have to worry about the docsrc folder - you don't have to worry any more about manually adding and committing stuff inside docs. 

You could now delete the 'docs' folder from your main branch, since you aren't using it anymore - so this has the added benefit of making your repo a little bit tidier!