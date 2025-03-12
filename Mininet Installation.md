
# Mininet Installation

- Git clone the repo of contrust from  using the command
```bash 
git clone https://github.com/contrust/mininet.git
```

- Then install mininet using the command
```bash
mininet/util/install.sh
```
- To check whether everything is installed correctly please run 
```bash
sudo mn
```
- Mininet by default installs pox controller but we found a lot of issues with it. So we are using Ryu controller. To install this downgrade the python version to python 3.9 with the following commands.
```bash
sudo apt update 
sudo apt install software-properties-common -y 
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
```
- Now install pip for python 3.9 using
``` bash
sudo apt install python3.9 python3.9-venv python3.9-dev -y
curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.9 get-pip.py
```
- Now add python 3.9 to alternatives
```bash
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
```
- Symlink pip and pip3 to pip3.9
```bash
sudo ln -sf /usr/local/bin/pip3.9 /usr/bin/pip
sudo ln -sf /usr/local/bin/pip3.9 /usr/bin/pip3
```
- Now Install eventlet version 0.30.2
```bash
python3 -m pip install eventlet==0.30.2
```
- Then install ryu manager and check the version using
```bash
python3 -m pip install ryu
ryu-manager --version
```
- You can now start ryu manager using
```bash
ryu-manager --ofp-tcp-listen-port <portnumber> ryu.app.simple_switch_13 --verbose
```


