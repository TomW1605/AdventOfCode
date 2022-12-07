import re

from readFile import readFile

class File:
    name = ""
    size = 0

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __str__(self):
        #return self.name
        #return f"({self.name}, {self.size})"
        return f"- {self.name} (file, size={self.size})"

    def __repr__(self):
        return f"{self.name} (file, size={self.size})"

    def __eq__(self, other):
        if type(other) == type(str):
            return other == self.name

        if type(other) == type(self):
            return other.name == self.name

        return False

class Folder(list):
    name = ""
    parent = None
    size = 0

    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_item(self, item):
        if isinstance(item, File):
            self.size += item.size
            if self.parent:
                self.parent.add_size(item.size)
        self.append(item)

    def remove_item(self, item):
        if isinstance(item, File):
            self.size -= item.size
            if self.parent:
                self.parent.remove_size(item.size)
        self.remove(item)

    def add_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_size(size)

    def remove_size(self, size):
        self.size -= size
        if self.parent:
            self.parent.remove_size(size)

    def set_parent(self, parent):
        self.parent = parent

    def get_folders(self):
        folders = [self]
        for item in self:
            if isinstance(item, Folder):
                folders += item.get_folders()

        return folders

    def __str__(self):
        """return_str = f"{self.name}["
        for item in self:
            return_str += f"{item.__str__()},"
        return_str = return_str[:-1] + "]"

        return return_str"""

        return_str = f"- {self.name} (dir, size={self.size})\n"
        for item in self:
            if isinstance(item, Folder):
                sub_return_str = f"{item.__str__()}\n"
                return_str += "\n".join([f"  {x}" for x in sub_return_str.split("\n")[:-1]])
                return_str += "\n"
            else:
                return_str += f"  {item.__str__()}\n"

        return_str = return_str[:-1]# + "]"

        return return_str

    def __repr__(self):
        return f"{self.name} (dir, size={self.size})"

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self.name

        if isinstance(other, Folder):
            return other.name == self.name

        return False


def build_file_tree(input_lines):
    root = Folder("/")
    current_folder = root

    ls_mode = False

    for line in input_lines[1:]:
        line = str(line)

        if line.startswith("$ cd "):
            if line[5:] == "..":
                current_folder = current_folder.parent
            else:
                current_folder = current_folder[current_folder.index(line[5:])]

        elif line.startswith("dir "):
            new_folder = Folder(line[4:])
            if new_folder not in current_folder:
                new_folder.parent = current_folder
                current_folder.add_item(new_folder)

        elif not line.startswith("$"):
            size, name = line.split(" ")
            new_file = File(name, size)
            if new_file not in current_folder:
                current_folder.add_item(new_file)

    return root

def part1(input_lines):
    print(input_lines)
    root_folder = build_file_tree(input_lines)
    print(root_folder.get_folders())

    total = 0
    for sub_folder in root_folder.get_folders():
        if sub_folder.size <= 100000:
            total += sub_folder.size

    print(total)

def part2(input_lines):
    print(input_lines)
    root_folder = build_file_tree(input_lines)
    print(root_folder.get_folders())

    total_fs = 70000000
    needed = 30000000
    free = total_fs-root_folder.size

    options = []
    for sub_folder in root_folder.get_folders():
        if free + sub_folder.size >= needed:
            options.append(sub_folder.size)

    options.sort()
    print(options[0])

if __name__ == '__main__':
    test = 0
    part = 2

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)
