import configparser
import os
import re
import shutil

import requests as requests

config = configparser.ConfigParser()
config.read('config.ini')

folder = config['general']['year'] + " - " + config['general']['language']

os.makedirs(os.path.join('.', folder), exist_ok=True)

completedDays = next(os.walk(os.path.join('.', folder)))[1]
completedDays.sort(key=lambda f: int(re.sub(r'\D', '', f)))
if len(completedDays) > 0:
    dayNum = int(completedDays[-1].split(" ")[-1]) + 1
else:
    dayNum = 1

if dayNum > 25:
    print("There are only 25 challenges in "+config['general']['year']+". Make sure the year is right in config.ini")
    exit(1)

response = requests.get("https://adventofcode.com/"+config['general']['year']+"/day/"+str(dayNum)+"/input", cookies={"session": config['general']['sessionID']})
if "unlocks" not in response.text:
    os.mkdir(os.path.join(folder, f"Day {dayNum:02d}"))

    with open(os.path.join(folder, f"Day {dayNum:02d}", "input.txt"), "w") as inputFile:
        inputFile.write(response.text)

    with open(os.path.join(folder, f"Day {dayNum:02d}", "testInput.txt"), "w") as testInputFile:
        testInputFile.write("")

    shutil.copyfile(os.path.join(folder, "template."+config['general']['extension']), os.path.join(folder, f"Day {dayNum:02d}", f"Day{dayNum:02d}.{config['general']['extension']}"))
else:
    print("please wait until the challenge has unlocked")
