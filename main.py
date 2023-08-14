#!/usr/bin/env python3
import time
import os
import datetime
from datetime import date
from datetime import datetime
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_moisture_sensor import GroveMoistureSensor

def main():

    #zmienna zapisujaca dane, kiedy czynnosc zostala wykonana
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    print("date and time =", dt_string)
    time.sleep(1)

    #Wykonanie zdjęcia oraz jego zapis na karte pamieci
    os.system('fswebcam -r 1280x720 {}.jpg'.format(dt_string))
    time.sleep(2)
    os.system('cp {}.jpg /media/pi/KINGSTON'.format(dt_string))
    time.sleep(2)

    #Podpiecie czujnika swiatla pod port A0
    sensor = GroveLightSensor(0)

    #Podpiecie czujnika wiglotnosci pod port A2
    sensorMoist = GroveMoistureSensor(2)

    #Podpiecie wyswietlacza LCD pod port I2C
    lcd = JHD1802()

    #Podpiecie czujnika DHT pod port D5
    sensorDHT = DHT('11', 5)
    while True:

        #zczytanie wartosci temp. i wilgotnosci oraz ich wyswietlenie
        humi, temp = sensorDHT.read()
        print('temperature {}C, humidity {}%'.format(temp, humi))
        lcd.setCursor(0, 0)
        lcd.write('temperature: {0:2}C'.format(temp))
        lcd.setCursor(1, 0)
        lcd.write('humidity: {0:5}%'.format(humi))
        time.sleep(2)

        #zczytanie i wyswietlenie wartosci czujnika swiatla
        light = sensor.light
        print('light value {}'.format(sensor.light))
        lcd.setCursor(0, 0)
        lcd.write('light: {0:>9}'.format(sensor.light))
        time.sleep(2)

        #zczytanie i wyswietlenie wartosci sondy gleby
        mois = sensorMoist.moisture
        if 0 <= mois and mois < 300:
            level = 'dry'
        elif 300 <= mois and mois < 600:
            level = 'moist'
        else:
            level = 'wet'

        print('moisture: {}, {}'.format(mois, level))
        lcd.setCursor(0, 0)
        lcd.write('moisture: {0:>6}'.format(mois))
        lcd.setCursor(1, 0)
        lcd.write('{0:>16}'.format(level))
        time.sleep(2)

        #wartosci do zapisy na karte pamieci USB
        temperature = temp
        humidity = humi
        moist = mois
        row = (now, dt_string, temperature, humidity, moist, level, light)
        with open("/media/pi/KINGSTON/dane.txt", "a") as myfile:
            myfile.write("Dane: {}\n".format(row))

if __name__ == '__main__':
    main()  