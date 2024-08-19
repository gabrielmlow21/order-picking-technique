class Results:
    def __init__(self) -> None:
        self.time = []
        self.distance = []
    
    def add_time(self, timeArr: list) -> None:
        self.time.append(timeArr)

    def add_dist(self, distArr: list) -> None:
        self.distance.append(distArr)

    def get_time(self) -> list:
        return self.time
    
    def get_dist(self) -> list:
        return self.distance