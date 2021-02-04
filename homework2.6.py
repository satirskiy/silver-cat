class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return f"{self._length} m * {self._width}m * 25 kg * 5 sm = {(self._length * self._width * 25 * 5) / 1000} т"

road_1 = Road(5000, 20)
print(road_1.get_full_profit())