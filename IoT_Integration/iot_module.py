
class IoTIntegration:
    def __init__(self):
        self.connected_devices = ['SmartLight', 'SmartSpeaker', 'SmartDoor']

    def check_status(self):
        return {device: 'online' for device in self.connected_devices}

if __name__ == '__main__':
    iot = IoTIntegration()
    print('IoT Status:', iot.check_status())
