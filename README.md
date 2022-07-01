# machine_learning_project
This is my first machine learning project

## Start Machine Learning Project:

## Pre-requisites :
1. Github Account
2. Heroku Account
3. Git Cli(Git CLient)
4. VS Code IDE

# Creating Conda Environment
conda create -p <env_name> python==3.7 -y
# Activate Conda
conda activate <env_name>/
            OR
conda activate venv

# Command to install Flask
pip install -r requirements.txt

# To add files to GIT
git add .
git add <filename>

Note: To ignore file/folder from  git we can write name of file/folder in .gitignore file

# To check git status
git status

# TO check all version maintained by git
git log

# To reate version/commit all cheanges by git
git commit -m <message with in double quotes>

# To send version/change to github
git push origin main

# To check remote url
git remote -v

# Git Rollback
git revert

# To check the branch in github
git branch

[Git Documentation](https://git-scm.com/docs/gittutorial)


# To setup CI/CD pipeline in Heroku we need 3 information:
1. HEROKU_EMAIL = <mailid>
2. HEROKU API KEY = <API KEY>
3. HEROKU APP NAME = <HEROKU APP NAME>

# Create docker file in VS Code
NewFile==>Give name Dockerfile

# Build Docker Image
docker build -t <image_name>:<tag_name> <location_name>

> Note : Image_name for docker must be lowercase. And as location of the docker file is in same directory so we specify the location name as .(dot)
docker build -t ml-project:latest .

# To list docker images
docker images

# To Run docker image
docker run -p <port_number> -e PORT=<environment variable_portnumber> <docker_image_id>

docker run -p 5000:5000 -e PORT=5000 <docker image id which you build>

# To check running containers in docker
docker ps

# To stop any container on docker
docker stop <container_id>

>Note : we can check container id using docker ps command

python setup.py install to run setup.py