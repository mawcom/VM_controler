__context__

first of all, it's necessary a properly configure of your VM, to ensure that all will work fine.

The distro used in this project was Ubuntu 13 (Trixie), you can easily access the main page of this distro here: [Trixie](https://www.debian.org/releases/trixie/).
inside linux, you will install rsyslog to create log's and a ssh server, to share all informations for our application. to access the rsyslog documation click here: [Rsyslog](https://www.rsyslog.com/doc/index.html)

to connect the aplication in the VM, we will use a ssh server, due this, it's necessary install, if you dont know if you have check executing this command in your machine `ssh`, if the output was : _command not found_ execute this prompt: `sudo apt update`,
`sudo apt install openssh-server -y` to install the ssh server. 

after install, active your server using: `sudo systemctl enable ssh`,  `sudo systemctl start ssh` and `sudo systemctl status ssh` to see the status of your serve, you should see Active: active (running) or just enable  

the main user of your vm need to be a sudoes user, otherwise, you wont have permision to execute some commands like `cat /var/log/syslog` to get the logs. so, you need to add the user to sudoers users. try this: `su -`, `usermod -aG sudo USER_NAME`, after this, restart your enviromment and try this: `groups USER_NAME` you should see something like : `USER_NAME: USER_NAME sudo`
