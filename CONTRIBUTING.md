## Contributing to Bloomfield Pedestrian Data Analysis

  1- Before starting, create the virtual environment:
    virtualenv --python=python3 .

  2- Activate the virtualenv:  
    source bin/activate

  3 -Then get the packages:

    pip install -r requirements.txt

  3.1 - if you need to update python packages please use this command below :
        "note that when updating python packages, update should run on same level with src folder"  
    pip freeze > requirements.txt  





## GIT Contribution :

  To check :
    git status

  to Add :

    git add <folder name> or
    git add .

  to commit :

    git commit -m "some text here"

  to push :

    git push -u origin <branch name>


  to remove :

    git rm -r --cached bin
