from flight_control_sys import FlightControlSystem
from sensor_sys import SensorSystem
from navigation_sys import NavigationSystem
from communication_sys import CommunicationSystem

"""
Определите классы для каждой из этих систем и реализуйте методы, 
которые демонстрируют взаимодействие между ними. 
Например, система управления полетом должна получать данные от 
сенсорной системы и отправлять команды навигации.
"""

# Примерв заимодействия
fcs = FlightControlSystem()
sensors = SensorSystem()
nav_system = NavigationSystem()
comm_system = CommunicationSystem()

sensor_data = sensors.collect_data()
fcs.receive_sensor_data(sensor_data)
fcs.send_navigation_command()
