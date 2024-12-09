# AOC 2024
# --- Day 9: Disk Fragmenter ---

import collections as coll
from dataclasses import dataclass


@dataclass
class File:
    file_id: int


@dataclass
class P1File(File):
    positions: list[int]
    defrag_pos: int | None = None

    def __post_init__(self):
        if self.defrag_pos is None:
            self.defrag_pos = len(self.positions) - 1

    def checksum(self):
        return sum([self.file_id * x for x in self.positions])

    def move(self, new_pos) -> bool:
        if self.defrag_pos == -1:
            return False

        if self.positions[self.defrag_pos] < new_pos:
            return False

        self.positions[self.defrag_pos] = new_pos
        self.defrag_pos -= 1
        return True

    def __repr__(self):

        return f"P1File(id: {self.file_id}, positions: {self.positions}, checksum: {self.checksum()})"


@dataclass
class P2File(File):
    start: int
    end: int

    def checksum(self):
        return sum([self.file_id * x for x in range(self.start, self.end, 1)])

    def move(self, new_start) -> bool:
        new_end = new_start + len(self)
        if new_start > self.start:
            return False
        self.start = new_start
        self.end = new_end
        return True

    def __len__(self):
        return self.end - self.start


@dataclass
class FreeSpace:
    start: int
    end: int

    def __len__(self):
        return self.end - self.start

    def __lt__(self, other: "FreeSpace"):
        return self.end < other.end


def solve_part_1(data):

    files, free_blocks = [], []
    block_nr, file_nr = 0, 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            files.append(P1File(file_nr, list(range(block_nr, block_nr + x))))
            file_nr += 1
        else:
            free_blocks.extend(list(range(block_nr, block_nr + x)))
        block_nr += x

    free_deque = coll.deque(free_blocks)
    block_pos = len(files) - 1
    while free_deque:
        if block_pos < 0:
            break
        cur_free = free_deque.popleft()
        cur_block = files[block_pos]
        freed = cur_block.move(cur_free)
        if not freed:
            free_deque.appendleft(cur_free)
            block_pos -= 1

    return sum([x.checksum() for x in files])


def solve_part_2(data: list[int]) -> int:

    files: list[File] = []
    free_spaces: list[FreeSpace] = []
    block_nr, file_nr = 0, 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            files.append(P2File(file_id=file_nr, start=block_nr, end=block_nr + x))
            file_nr += 1
        elif x != 0:
            free_spaces.append(FreeSpace(start=block_nr, end=block_nr + x))
        block_nr += x

    files_deque = coll.deque(files)

    while files_deque:
        cur = files_deque.pop()
        moved_to = None
        for x in free_spaces:
            if len(x) >= len(cur):
                if cur.move(x.start):
                    moved_to = x
                break

        if moved_to:
            space_left = len(moved_to) - len(cur)
            free_spaces.remove(moved_to)
            if space_left > 0:
                free_spaces.append(FreeSpace(start=cur.end, end=cur.end + space_left))
            free_spaces.sort()

    return sum([x.checksum() for x in files])


def solve():
    with open("input.txt", encoding="utf-8") as fp:
        data = [int(x) for x in fp.read().strip() if x]
    return solve_part_1(data), solve_part_2(data)


if __name__ == "__main__":
    part_1, part_2 = solve()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
    assert part_1 == 6201130364722
    assert part_2 == 6221662795602
