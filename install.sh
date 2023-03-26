sudo pip3 install Adafruit_BBIO
sudo cp ./src/CPU_FAN_BBB.py /usr/lib/CPU_FAN_BBB/CPU_FAN_BBB.py
sudo cp ./CPU_FAN_BBB.service /lib/systemd/system/CPU_FAN_BBB.service

sudo systemctl daemon-reload
sudo systemctl enable CPU_FAN_BBB.service
sudo systemctl start CPU_FAN_BBB.service
sudo systemctl status CPU_FAN_BBB.service