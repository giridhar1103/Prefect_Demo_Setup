# Prefect_Demo_Setup

I have used a t2.micro EC2 instance for this set up.

Basic ec2 installations:
```bash
sudo apt-get update -y && sudo apt-get upgrade -y

sudo apt-get install -y git curl wget unzip nano
```

Install pip:
```bash
sudo apt-get update -y

sudo apt-get install -y python3-pip
```

Now let's set up prefect. The configurations and versions I'm using is:
```
Version:             2.20.22
API version:         0.8.4
Python version:      3.12.3
Git commit:          7bdb7b8e
Built:               Thu, Sep 11, 2025 9:55 AM
OS/Arch:             linux/x86_64
Profile:             default
Server type:         server
```

Before we install, let's create a python3 venv:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Now install prefect:
```bash
pip install "prefect>=2.14,<3"
```

After you're done setting up prefect on your ec2, go to prefect.io and create a free account on it. Next, scroll down to the API-Keys section on the website and create a pair of api keys. 

Go back to your ec2 instance and enter this command:
```bash
prefect cloud login
```
It will ask you for the API keys so enter the api keys and you will be logged in through your account.

In the same environment, change these wait times for Database timeouts for sqlite(execute in order):
```bash
echo 'export PREFECT_SERVER_DATABASE_CONNECTION_TIMEOUT=30' >> ~/.bashrc

echo 'export PREFECT_SERVER_DATABASE_TIMEOUT=30' >> ~/.bashrc

source ~/.bashrc
```

