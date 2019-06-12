# Linux server with Flask, Apache, and PostgreSQL
This project is a minimal Flask app running on an Apache server. The purpose is to provide simple boilerplate code to easily set up new Flask apps.

The project assumption is that the server is installed on a virtual machine, configured with Vagrant and Virtualbox, on a Windows computer.

The project, called `myapp`, is created under the default shared Vagrant directory `/vagrant`.

In order to make the code and instructions easily transferrable to non-Vagrant servers, the configuration of the `Vagrant` file is minimal. All installment of necessary packages are done manually.

## Create and configure a Vagrant virtual Machine
Install Git, Vagrant and Virtualbox on your computer. Instructions can be found at the below links:
* [Git](https://git-scm.com/downloads)
* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)

To get the Vagrant configuration file of the Virtual Machine, fork and clone the following repository:
```
https://github.com/codeballet/server-bionic.git
```

Inside the cloned directory, there is a `vagrant` directory. Change directory to that `vagrant` directory and run the command `vagrant up`.
Once the virtual machine configuration has finished to install, you may connect via SSH to the virtual machine with the command `vagrant ssh`.

When you see a shell prompt starting with the word `vagrant`, you have successfully logged into the virtual machine.

The command will create a vagrant box with 'ubuntu/bionic64'. The only configuration change from a default installation is a port forwarding from guest port 80 to host port 8080. The Vagrant file has the following line uncommented:
```
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
```

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

## Installing and connecting to PostgreSQL
This part of the project is not yet finished.

## Accessing the app in a browser
On the host computer, the Flask app is served by Apache on:
```
http://localhost:8080
```

## Contributions
Given that I am really new in the field of coding and using git, I am not yet quite sure how to accept contributions. If you want to contribute to the project, please do contact me. I am open for advice.

## MIT License

Copyright (c) 2019 Johan Stjernholm

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.