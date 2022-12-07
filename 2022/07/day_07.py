# --- Day 7: No Space Left On Device ---

from dataclasses import dataclass, field
from typing import Optional

from aocd.models import Puzzle


@dataclass
class Folder:
    name: int
    parent_dir: Optional["Folder"]
    folders: dict["Folder"] = field(default_factory=dict)
    size_of_files: int = 0

    def folder_size(self):
        return self.size_of_files + sum([x.folder_size() for x in self.folders.values()])

    def path(self):
        if self.parent_dir == None:
            return ""
        return f"{self.parent_dir.path()}/{self.name}"


def solve():
    puzzle = Puzzle(year=2022, day=7)
    root_dir = cur_dir = None
    all_dirs = {}

    for x in puzzle.input_data.split("\n"):
        command = x.split()
        match command:
            case ["$", "cd", "/"]:
                if not root_dir:
                    root_dir = Folder(
                        name=command[2], parent_dir=None, folders={}
                    )
                    all_dirs[root_dir.path()] = root_dir
                cur_dir = root_dir
            case ["$", "cd", ".."]:
                cur_dir = cur_dir.parent_dir
            case ["$", "cd", folder_name]:
                if folder_name in cur_dir.folders:
                    cur_dir = cur_dir.folders[folder_name]
                else:
                    new_folder = Folder(
                        name=folder_name, parent_dir=cur_dir, folders={}
                    )
                    all_dirs[new_folder.path()] = new_folder
                    cur_dir = new_folder
            case ["dir", folder_name]:
                if folder_name not in cur_dir.folders:
                    new_folder = Folder(
                        name=folder_name, parent_dir=cur_dir, folders={}
                    )
                    cur_dir.folders[command[1]] = new_folder
                    all_dirs[new_folder.path()] = new_folder
            case [file_size, _] if file_size != "$":
                cur_dir.size_of_files += int(file_size)

    total_size = 70000000
    free_space = total_size - root_dir.folder_size()
    required_space = 30000000 - free_space
    folder_sizes = [x.folder_size() for x in all_dirs.values()]

    puzzle.answer_a = sum([x for x in folder_sizes if x <= 100000])
    puzzle.answer_b = min([x for x in folder_sizes if x > required_space])
    return puzzle.answer_a, puzzle.answer_b


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
