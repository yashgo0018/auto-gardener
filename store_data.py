import sqlite3
import serial

def main():
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600)
    except:
        print('\nError: Cannot connect to arduino.\n')
        return False
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    while True:
        value = arduino.read_all().decode()
        if value != '':
            value = value.split('\r')[0]
            moisture = value[value.find('mois=') + 5: value.find('humi=')]
            humidity = value[value.find('humi=') + 5: value.find('temp=')]
            temperature = value[value.find('temp=') + 5: len(value)]
            cur.execute(f"""INSERT INTO maindata
                    (datetime, temperature, humidity, moisture)
                    values(
                        datetime('now', 'localtime'),
                        {temperature},
                        {humidity},
                        {moisture})
                """)
            conn.commit()
    conn.close()
    return True

if __name__ == '__main__':
    main()
