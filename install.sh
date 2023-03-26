echo "Installing needed libs"
sudo pip3 install Adafruit_BBIO
echo "Copy files"
sudo cp ./src/CPU_FAN_BBB.py /usr/lib/CPU_FAN_BBB/CPU_FAN_BBB.py
sudo cp ./CPU_FAN_BBB.service /lib/systemd/system/CPU_FAN_BBB.service

sudo systemctl daemon-reload
echo "Enabling the service"
sudo systemctl enable CPU_FAN_BBB.service
echo "Starting the service"
sudo systemctl start CPU_FAN_BBB.service
echo "Checking the service"
sudo systemctl status CPU_FAN_BBB.service