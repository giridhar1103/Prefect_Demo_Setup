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
