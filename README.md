# Keypad 4x4 DTMF for  SVXLink

Wykorzystanie keypad 4x4 z modułem PCF8574 do wysyłania komend DTMF do SVXLink

keypad 4x4 podłączony via moduł **PCF8574* I2C do Raspberry PI (RaspbianOS), Orange Pi Zero (ArmBian)

Instalacja pakietu
---------------------

**sudo -s**

**cd /opt**

jeśli nie masz katalogu "fmpoland" utwórz go poleceniem

**mkdir fmpoland**

**cd fmpoland/**

**git clone https://github.com/radioprj/keydtmf.git**

**cd keydtmf/**

Czytaj plik opis.txt gdzie znajdziesz informacje o konfiguracji i plik [keydtmf.pdf](https://github.com/radioprj/keydtmf/blob/main/keydtmf.pdf) opis podłączenia keypad do PCF8574
