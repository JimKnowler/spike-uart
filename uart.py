import serial
import time

KNIGHTRIDER_TIME_INTERVAL = 0.1         # seconds

def test_write_from_console(ser):
    # read from console, write to port
    while True:
        c = input()
        ser.write(str.encode(c))

def test_write_counter(ser):
    # write to port
    line_count = 0

    while True:
        line_count += 1

        print(line_count, ':', end='')
        
        for i in range(20):
            c = str(i)
            print(c + ', ', end='')
            ser.write(str.encode(c))
        print('')

def test_write_knightrider(ser):
    # write to port

    while True:        
        for i in range(0, 7):
            b = bytes([1 << i])
            c = str(b)
            print(c)
            ser.write(b)
            time.sleep(KNIGHTRIDER_TIME_INTERVAL)   

        for i in reversed(range(1, 8)):
            b = bytes([1 << i])
            c = str(b)
            print(c)
            ser.write(b)
            time.sleep(KNIGHTRIDER_TIME_INTERVAL)

def test_read(ser):
    # read from port, write to console
    line_count = 0

    while True:
        for i in range(64):
            c = ser.read()
            try:
                c = c.decode('ascii')
            except:
                c='?'

            print(c, end='')
        print('')
        line_count += 1

        print(line_count, ':', end='')

def main():

    with serial.Serial('/dev/cu.usbserial-14320') as ser:
        ser.baudrate = 115200
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.bytesize = serial.EIGHTBITS
        ser.xonxoff = False

        print('port is_open:', ser.is_open)
        
        test_write_knightrider(ser)
        #test_write_from_console(ser)
        #test_write_counter(ser)
        #test_read(ser)
    
main()
