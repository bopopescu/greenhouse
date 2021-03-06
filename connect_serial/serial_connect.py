import serial
from config import COUNT_PARAM, PORT_NAME
from connect_serial.serial_ports import serial_ports


class SerialConnectArduino:

    def __init__(self, port='/dev/ttyACM0', baud=9600):
        self._port = port
        self._baud = baud
        try:
            self.arduino = serial.Serial(self._port, self._baud)
        except:
            self._port = self.ports()[0]
            self.arduino = serial.Serial(self._port, self._baud)

    def __del__(self):
        self.arduino.close()

    def ports(self):
        return serial_ports()

    def readline(self):
        result = {}
        data = self.arduino.readline()
        data = data[:-2]
        data = data.decode('utf-8')
        data_list = data.split(',')
        if len(data_list) > COUNT_PARAM:
            result['pipe'] = data_list[0]
            result['temp1'] = data_list[1]
            result['hum1'] = data_list[2]
            result['modeBMP'] = data_list[3]
            result['temp2'] = data_list[4]
            result['hum2'] = data_list[5]
            result['press'] = data_list[6]
        return result

    def read_line_str(self):
        result = self.readline()
        res_text = ""
        for key in result:
            res_text += "{0}: {1}".format(key, str(result[key])).ljust(18, ' ')
        return res_text


if __name__ == "__main__":
    arduino = SerialConnectArduino(port=PORT_NAME)
    while True:
        try:
            data = arduino.readline()
            print(data)
        except KeyboardInterrupt:
            print("\nExit !!!")
            break

