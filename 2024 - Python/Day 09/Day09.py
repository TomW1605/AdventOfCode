import time

def part1(input_lines):
    file_id = 0
    block_type = 0 # 0 = file, 1 = blank
    disk = []
    for digit in input_lines[0]:
        size = int(digit)
        if block_type == 0:
            disk += [file_id] * size
            file_id += 1
            block_type = 1
        else:
            disk += ["."] * size
            block_type = 0

    # print("".join(str(block) for block in disk))
    for ii in range(len(disk)-1, -1, -1):
        if disk[ii] == ".":
            continue
        else:
            blank_index = disk.index(".")
            if blank_index < ii:
                disk[blank_index] = disk[ii]
                disk[ii] = "."
            else:
                break
        # print("".join(str(block) for block in disk))
    # print("".join(str(block) for block in disk))
    print(sum(ii*disk[ii] for ii in range(len(disk)) if disk[ii] != "."))

class File:
    def __init__(self, id, size):
        self.id = id
        self.size = size

    def __str__(self):
        return f"File({self.id}, {self.size})"

    def __repr__(self):
        return self.__str__()

class Space:
    def __init__(self, size):
        self.size = size
        self.id = 0

    def __str__(self):
        return f"Space({self.size})"

    def __repr__(self):
        return self.__str__()

def part2(input_lines):
    file_id = 0
    block_type = 0 # 0 = file, 1 = blank
    disk = []
    for digit in input_lines[0]:
        size = int(digit)
        if block_type == 0:
            disk.append(File(file_id, size))
            file_id += 1
            block_type = 1
        else:
            disk.append(Space(size))
            block_type = 0

    for ii in range(len(disk)-1, -1, -1):
        if isinstance(disk[ii], Space):
            continue
        else:
            blank_index = next((index for index, space in enumerate(disk)
                                if isinstance(space, Space) and space.size >= disk[ii].size), ii)
            if blank_index < ii:
                if disk[blank_index].size == disk[ii].size:
                    disk[blank_index] = disk[ii]
                    jj = ii
                else:
                    new_space = Space(disk[blank_index].size - disk[ii].size)
                    disk[blank_index] = disk[ii]
                    disk.insert(blank_index+1, new_space)
                    jj = ii + 1

                if jj < len(disk)-1 and isinstance(disk[jj+1], Space) and isinstance(disk[jj-1], Space):
                    disk[jj-1].size += disk[jj+1].size
                    disk.pop(jj+1)
                    disk[jj-1].size += disk[jj].size
                    disk.pop(jj)
                elif jj < len(disk)-1 and isinstance(disk[jj+1], Space):
                    disk[jj+1].size += disk[jj].size
                    disk.pop(jj)
                elif isinstance(disk[jj-1], Space):
                    disk[jj-1].size += disk[jj].size
                    disk.pop(jj)
                else:
                    disk[jj] = Space(disk[jj].size)

    # print(disk)
    raw_disk = [[disk[ii].id] * disk[ii].size for ii in range(len(disk))]
    flat_disk = [block for file in raw_disk for block in file]
    # print("".join(str(block) for block in flat_disk))
    print(sum(ii*flat_disk[ii] for ii in range(len(flat_disk))))

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = open("testInput.txt", "r").read().splitlines()
    else:
        inputLines = open("input.txt", "r").read().splitlines()

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
