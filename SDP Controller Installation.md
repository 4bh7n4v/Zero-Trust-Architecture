# SDP Installation
## Install and Configure required packages
- Install Node.js
```
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt update
sudo apt install nodejs -y
```
- Install MYSQL
```
sudo apt install mysql-server -y
```
- Secure MYSQL Installation
```
sudo mysql_secure_installation
```
- Start and verify MYSQL
```
sudo systemctl start mysql
sudo systemctl status mysql
```
- Create a database and a User and grant the access
```
sudo mysql -u root -p
create database sdp;
create user sdpuser@localhost identified by password;
GRANT ALL PRIVILEGES ON . TO 'sdp'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit;
```
- Import the setup file
```
mysql -u sdpuser -p sdp < setup/sdp.sql
```
- Insert the appropriate data into the database
## Setup SDP Controller
- git clone the repo
```
https://github.com/WaverleyLabs/SDPcontroller.git
```
- Run the Certificate_Gen.sh from github in setup directory
```
cd SDPcontroller
setup/Certificate_Gen.sh
```

- Edit Config.js change the following things.
    * Set debug to true
    * Correct the paths for cert files
    * Change your username and password

- Edit sdpController.js
    * Set var mysql to 

    ```
    var mysql  = require("mysql2");
    ```




