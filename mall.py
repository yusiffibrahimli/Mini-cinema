from datetime import datetime
today = datetime.today().hour
baglanis = 23
acilis = 10
class Malls:
    def __init__(self, location, floor, hall_count):
        self.location = location
        self.floor = floor
        self.hall_count = hall_count

    def hours_info(self):
        if acilis <= today < baglanis:
            return "Mall open"
        else:
            exit("Mall closed")

    
    def age_info(self,age):
        try:
            if int(age) < 14:
                exit("Age less than 14")
            else:
                return 'You can enter the moll'
        except ValueError:
            return "Please enter a valid age."

    def vaccinate_info(self,status):
        try:
            if status == 'Active': 
                return 'Vaccination active'
            else:
                exit("Vaccination inactive")
        except ValueError:
            return "Please enter a valid value for vaccination."
        
class GanjlikMall(Malls):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)
        # self.season = season
        # self.episodes = episodes

class DenizMoll(Malls):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)

class AygunMoll(Malls):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)

class GancaMoll(Malls):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)

class NizamiMoll(Malls):
    def __init__(self, location, floor, hall_count):
        super().__init__(location, floor, hall_count)
