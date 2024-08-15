#!/bin/bash

dis=`lsb_release -i|cut -d: -f2 |tr -d '[:space:]'`
ver=`lsb_release -r|cut -d: -f2 |tr -d '[:space:]'`


if [ $dis == "Raspbian" ] || [ $dis == "Debian" ]; then

   if [ $ver == "11" ]; then

    echo "Instalacja pakietów dla keypad 4x4 na bazie Debian 11"
    echo ""
    sudo apt-get update
    sudo apt install -y python3 python3-pip python3-smbus python3-dev i2c-tools
    sudo python3 -m pip install --upgrade setuptools --root-user-action=ignore
    sudo python3 -m pip install smbus2 --root-user-action=ignore
    sudo usermod -a -G i2c svxlink
    sudo chown svxlink:svxlink /opt/fmpoland/keydtmf/keydtmf.py
    sudo chown svxlink:svxlink /opt/fmpoland/keydtmf/keydtmf.ini
    echo ""
    echo "Kopiowanie keydtmf.service do /lib/systemd/system/"
    sudo cp /opt/fmpoland/keydtmf/keydtmf.service /lib/systemd/system/
    echo ""
    echo "Instalacja zakonczona ...."
    echo ""
   fi

   if [ $ver == "12" ]; then

    echo "Instalacja pakietów dla keypad 4x4 na bazie Debian 12"
    echo ""
    sudo apt-get update
    sudo apt install -y python3 python3-pip python3-smbus python3-smbus2 python3-dev i2c-tools
    sudo usermod -a -G i2c svxlink
    echo ""
    sudo chown svxlink:svxlink /opt/fmpoland/keydtmf/keydtmf.py
    sudo chown svxlink:svxlink /opt/fmpoland/keydtmf/keydtmf.ini
    echo "Kopiowanie keydtmf.service do /lib/systemd/system/"
    sudo cp /opt/fmpoland/keydtmf/keydtmf.service /lib/systemd/system/
    echo ""
    echo "Instalacja zakonczona ...."
    echo ""

   fi

else

  echo ""
  echo " UWAGA - proces instalacji bibliotek systemowych przerwany"
  echo " Uzywasz dystrybucji systemu na bazie: $dis $ver"
  echo " Instalacja bibliotek przygotowana dla dystrubucji na bazie Debian v11 lub v12"
  echo ""

fi
