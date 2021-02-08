class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return "\n".join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("sum of cell is:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("subtraction of cell is")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "ячеек в первой клетке меньше второй , вычитане невозможно!"

    def __mul__(self, other):
        print("multiply of cell is:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("truedive of cell is:")
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)