# ServerNode

##AWS Ec2 configuration
Server nodes are Amazon Ec2 instances.
We have two of them ServerNode1 and ServerNode2.
There are running on debian.
Each one have a security group where inbound and outbounds rules are added depending on the security we want to have.

Server node 1 data:
- private_ip :  172.31.28.167
- public ip : Changing at each instance start

Connection requires a ssh private key pair
 ssh -i "servernode1keypair.pem" admin@ec2-(public-ip).us-east-2.compute.amazonaws.com
 
 ##Start api
 To start the api you need to:
 - cd ServerNode
 - source env/bin/activate
 - uwsgi dev.ini
 
 ##Add new server
 First you need to create a new Ec2 instance or an Azure VM.
 
 Install docker:
 Follow https://runnable.com/docker/install-docker-on-linux
 
 Other installations:
- sudo apt-get update
- python3 --version (to check if installed)
- sudo apt-get install python3.6 (if not installed)
- sudo apt-get install git-all (to install git if not installed)
- git clone https://github.com/mguillevic/ServerManagerApp.git
- cd ServerNode/
- sudo apt-get install gcc
- sudo apt-get install python3-dev
- sudo apt install python3-venv
- sudo apt-get install python3-pip
- python3 -m venv env
- pip install Flask
- pip install psutil
- pip install requests
- pip install uwsgi 
And you should be able to start the api

For game images
- sudo scp shell_scripts ../
- cd ../shell_scripts
- sudo docker bash pull_jeu.sh


