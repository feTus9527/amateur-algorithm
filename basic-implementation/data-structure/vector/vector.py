from typing import List


class Vector:

    def __init__(self, n: int) -> None:
        self.size: int = n
        self.count: int = 0
        self.data: List[int] = [0] * n

    def insert(self, pos: int, n: int) -> int:
        if pos < 0 or pos > self.count:
            return 0
        if self.size == self.count:
            self._expand()
        for i in range(self.count, pos - 1, -1):
            self.data[i] = self.data[i - 1]

        self.data[pos] = n
        self.count += 1
        return 1

    def remove(self, pos: int):
        if pos < 0 or pos >= self.count:
            return 0

        for i in range(pos, self.count - 1):
            self.data[i] = self.data[i + 1]

        for i in range(self.count - 1, self.size):
            self.data[i] = 0

        self.count -= 1
        return 1

    def _expand(self):
        self.data.extend([0] * self.size)
        self.size *= 2

    def __repr__(self) -> str:
        result = []

        max_index_width = max(len(str(i)) for i in range(self.size))
        max_data_width = max(len(str(self.data[i])) for i in range(self.size))

        widths = [max(max_index_width, max_data_width) for _ in range(self.size)]

        indices = " ".join([f"{i:{widths[i]}d}" for i in range(self.size)])
        data = " ".join([f"{self.data[i]:{widths[i]}d}" for i in range(self.size)])

        total_width = len(indices)

        result.append("┌─" + "─" * total_width + "─┐")
        result.append(f"│ {indices} │")
        result.append("├─" + "─" * total_width + "─┤")
        result.append(f"│ {data} │")
        result.append("└─" + "─" * total_width + "─┘")
        result.append("")

        return "\n".join(result)


if __name__ == "__main__":
    import random

    TOTAL_OPS = 20
    VECTOR_LENGTH = 4
    INSERT_RATIO = 75
    N_MAX = 100000
    POSITION_OVERFLOW = 2

    vector = Vector(VECTOR_LENGTH)

    for i in range(TOTAL_OPS):
        op = random.randint(1, 100)
        pos = random.randint(0, vector.count + POSITION_OVERFLOW)
        if op < INSERT_RATIO:
            n = random.randint(1, N_MAX)
            print(f"insert {n} at position {pos} to vector = {vector.insert(pos, n)}")
        else:
            print(f"remove position {pos} from vector = {vector.remove(pos)}")
        print(vector)
