from readFile import readFile


def part1(input_lines):
    print(input_lines)

    seeds = [int(x) for x in input_lines.pop(0).split(': ')[1].split(' ')]

    maps = {
        'seed_soil': [],
        'soil_fertilizer': [],
        'fertilizer_water': [],
        'water_light': [],
        'light_temperature': [],
        'temperature_humidity': [],
        'humidity_location': []
    }

    section = ""
    for line in input_lines:
        if line == '':
            continue
        if "seed-to-soil" in line:
            section = 'seed_soil'
            continue
        elif "soil-to-fertilizer" in line:
            section = 'soil_fertilizer'
            continue
        elif "fertilizer-to-water" in line:
            section = 'fertilizer_water'
            continue
        elif "water-to-light" in line:
            section = 'water_light'
            continue
        elif "light-to-temperature" in line:
            section = 'light_temperature'
            continue
        elif "temperature-to-humidity" in line:
            section = 'temperature_humidity'
            continue
        elif "humidity-to-location" in line:
            section = 'humidity_location'
            continue

        input_range_start = int(line.split(' ')[1])
        output_range_start = int(line.split(' ')[0])
        range_len = int(line.split(' ')[2])
        maps[section].append(
            (
                range(input_range_start, input_range_start + range_len),
                # range(output_range_start, output_range_start + range_len),
                output_range_start - input_range_start
            )
        )

    print(maps)

    print(seeds)

    for map_name, map_values in maps.items():
        print(map_name)
        for ii in range(0, len(seeds)):
            for map_value in map_values:
                if seeds[ii] in map_value[0]:
                    # print(f"{seeds[ii]}: {map_value}")
                    seeds[ii] += map_value[1]
                    break

        print(seeds)
    print(min(seeds))

def part2(input_lines):
    print(input_lines)

    seed_ranges = [int(x) for x in input_lines.pop(0).split(': ')[1].split(' ')]
    seeds = []

    for ii in range(0, len(seed_ranges), 2):
        seeds += list(range(seed_ranges[ii], seed_ranges[ii]+seed_ranges[ii+1]))
    print("seeds")

    maps = {'seed_soil': [], 'soil_fertilizer': [], 'fertilizer_water': [], 'water_light': [], 'light_temperature': [],
        'temperature_humidity': [], 'humidity_location': []}

    section = ""
    for line in input_lines:
        if line == '':
            continue
        if "seed-to-soil" in line:
            section = 'seed_soil'
            continue
        elif "soil-to-fertilizer" in line:
            section = 'soil_fertilizer'
            continue
        elif "fertilizer-to-water" in line:
            section = 'fertilizer_water'
            continue
        elif "water-to-light" in line:
            section = 'water_light'
            continue
        elif "light-to-temperature" in line:
            section = 'light_temperature'
            continue
        elif "temperature-to-humidity" in line:
            section = 'temperature_humidity'
            continue
        elif "humidity-to-location" in line:
            section = 'humidity_location'
            continue

        input_range_start = int(line.split(' ')[1])
        output_range_start = int(line.split(' ')[0])
        range_len = int(line.split(' ')[2])
        maps[section].append((range(input_range_start, input_range_start + range_len),
                              # range(output_range_start, output_range_start + range_len),
                              output_range_start - input_range_start))

    print("maps")

    # print(seeds)

    for map_name, map_values in maps.items():
        print(map_name)
        for ii in range(0, len(seeds)):
            for map_value in map_values:
                if seeds[ii] in map_value[0]:
                    # print(f"{seeds[ii]}: {map_value}")
                    seeds[ii] += map_value[1]
                    break

        # print(seeds)
    print(min(seeds))


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

