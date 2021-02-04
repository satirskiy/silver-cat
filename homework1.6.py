class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("TrafficLaght is red")
            print(" TrafficLaght is yellow")
            print("TrafficLaght is green")

trafficlight = TrafficLight()
trafficlight.running()