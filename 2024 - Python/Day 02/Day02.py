import time

from readFile import readFile

def part1(input_lines):
    reports = [list(map(int, report.split(" "))) for report in input_lines]
    total_safe = 0
    for report in reports:
        safe = True
        if report[1] > report[0]:
            report_inc = True
        else:
            report_inc = False
        for ii in range(len(report)-1):
            if report_inc:
                if not (report[ii+1] > report[ii] and report[ii+1] - report[ii] <= 3):
                    safe = False
                    break
            else:
                if not (report[ii+1] < report[ii] and report[ii] - report[ii+1] <= 3):
                    safe = False
                    break
        if safe:
            total_safe += 1
    print(total_safe)

def check_report(report):
    unsafe_levels = 0
    if report[1] > report[0]:
        report_inc = True
    else:
        report_inc = False
    for ii in range(len(report)-1):
        if report_inc:
            if not (report[ii+1] > report[ii] and report[ii+1] - report[ii] <= 3):
                unsafe_levels += 1
                # break
        else:
            if not (report[ii+1] < report[ii] and report[ii] - report[ii+1] <= 3):
                unsafe_levels += 1
                # break
    return unsafe_levels

def part2(input_lines):
    reports = [list(map(int, report.split(" "))) for report in input_lines]
    total_safe = 0
    unsafe_reports = []
    for report in reports:
        unsafe_levels = check_report(report)
        if unsafe_levels == 0:
            total_safe += 1
        else:
            unsafe_reports.append(report)
    # print(unsafe_reports)
    unsafe_reports_copy = unsafe_reports.copy()
    for report in unsafe_reports:
        for ii in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(ii)
            unsafe_levels = check_report(report_copy)
            if unsafe_levels == 0:
                unsafe_reports_copy.remove(report)
                total_safe += 1
                break

    # print(unsafe_reports_copy)
    print(total_safe)

if __name__ == '__main__':
    test = 0
    part = 2

    start_time = time.time()

    if test:
        inputLines = readFile("testInput.txt")
    else:
        inputLines = readFile("input.txt")

    if part == 1:
        part1(inputLines)
    elif part == 2:
        part2(inputLines)

    total_time = time.time() - start_time

    hours = int(total_time / 3600)
    minutes = int(total_time / 60)
    seconds = total_time % 60

    print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}")
