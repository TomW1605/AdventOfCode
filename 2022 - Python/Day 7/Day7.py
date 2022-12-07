import re

from readFile import readFile

class File:
    name = ""
    size = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size

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

    def __init__(self, name):
        super().__init__()
        self.name = name

    def add_item(self, item):
        self.append(item)

    def remove_item(self, item):
        self.remove(item)

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        """return_str = f"{self.name}["
        for item in self:
            return_str += f"{item.__str__()},"
        return_str = return_str[:-1] + "]"

        return return_str"""

        return_str = f"- {self.name} (dir)\n"
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
        return f"{self.name} (dir)"

    def __eq__(self, other):
        if isinstance(other, str):
            return other == self.name

        if isinstance(other, Folder):
            return other.name == self.name

        return False

    """def __contains__(self, item):
        return item in self"""

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

            """if new_folder in current_folder:
                current_folder.add_item(new_folder)
            else:
                current_folder = new_folder"""

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
    folder_tree = build_file_tree(input_lines)
    print(folder_tree)

def part2(input_lines):
    print(input_lines)

if __name__ == '__main__':
    test = 1
    part = 1

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)
