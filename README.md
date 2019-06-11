# Linux server with Flask, Apache, PostgreSQL
This project is a minimal Flask app running on an Apache server. The purpose is to provide simple boilerplate code to easily set up new Flask apps.

The project assumption is that the server is installed on a virtual machine, configured with Vagrant and Virtualbox, on a Windows computer.

The project, called `myapp`, is created under the default shared Vagrant directory `/vagrant`.

In order to make the code and instructions easily transferrable to non-Vagrant servers, the configuration requirements of the `Vagrant` file are minimal. All installment of necessary packages are done manually.

## Create and configure a Vagrant virtual Machine
Install Git, Vagrant and Virtualbox on your computer. Instructions can be found at the below links:
* [Git](https://git-scm.com/downloads)
* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)

Once the above software is installed, open Git Bash as an Administrator (necessary for later installment of the virtual environment). Create a new directory, in which you run:
`vagrant up`

The command will create a vagrant box with 'ubuntu/bionic64'.

Once the virtual machine configuration has finished its work, you may connect via SSH to the virtual machine with the command `vagrant ssh`. When you see a shell prompt starting with the word `vagrant`, you have successfully logged into the virtual machine.

## Securing the Firewall
Check status of the `ufw` firewall:
```
sudo ufw status
```

Block all incoming ports and allow all outgoing ports:
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Allow `ssh` on standard port 22 and custom port 2222, as set up by Vagrant:
```
sudo ufw allow ssh`
sudo ufw allow 2222/tcp
```

Allow the web server on port 80:
```
sudo ufw allow www
```

enable the firewall:
```
sudo ufw enable
```

## Installing the virtual environment
Using Git Bash on Windows with Vagrant, you must run Git Bash as Administrator, or the virtual environment may fail to install.

Install Python3 and Virtualenv with `apt-get`:
```
sudo apt-get -y install python3 python3-dev
sudo apt install virtualenv
```

Create directory `/vagrant/myapp`. Set up a python3 virtual environment in that directory. For more information, see [virtualenv installation](https://virtualenv.pypa.io/en/latest/installation/).
```
mkdir myapp
cd myapp
virtualenv -p python3 venv
```

Activate the virtual environment with `. venv/bin/activate`.
	
Within the activated environment, install Flask with `pip install Flask`.

To exit from the virtual environment: `deactivate`.
