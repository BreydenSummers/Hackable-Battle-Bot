#Startup file for the website
#Put file in /lib/systemd/system
#run systemctl enable flask.service 

[Unit]
Description= Spin the robot around and around
After=network.target

[Service]
WorkingDirectory=/home/aggies/Hackable-Battle-Bot/
ExecStart=/usr/bin/python3 spin.py

[Install]
WantedBy=multi-user.target
