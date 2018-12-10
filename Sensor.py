import MySQLdb as mdb
import time
import serial

ser=serial.Serial('/dev/ttyACM0',9600)                #port may be different
while True:
        data=ser.readline()
        time.sleep(1)
        data=ser.readline()
        send=data.split("\t")                         #each sensor data is seperated by a tab
        
        soil_moisture=send[0]
        air_quality=send[1]
        temperature=send[2]
        pressure=send[3]
        
        
        con=mdb.connect('192.168.0.101','root','1234','Sense');
        with con:
                cursor=con.cursor()
                cursor.execute("""INSERT INTO test VALUES(NULL,%s,%s,%s,%s)""",soil_moisture,temperature,air_quality,pressure))
                con.commit()
                cursor.close()
                
