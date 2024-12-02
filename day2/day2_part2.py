"""
Advent of Code 2024

--- Day 2: Red-Nosed Reports ---
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

# reports = [[7, 6, 4, 2, 1],
#            [1, 2, 7, 8, 9],
#            [9, 7, 6, 2, 1],
#            [1, 3, 2, 4, 5],
#            [8, 6, 4, 4, 1],
#            [1, 3, 6, 7, 9]]


def main():
    reports = load_input("input.txt")
    safe_report_count = 0
    for report in reports:
        if is_report_safe_with_dampener(report):
            safe_report_count += 1
    print(safe_report_count)


def load_input(filename):
    rows = []
    with open(filename, 'r') as file_in:
        for line in file_in.readlines():
            chars = line.split(' ')
            numbers = [int(char) for char in chars]
            rows.append(numbers)
    return rows


def is_report_safe(report):
    if not is_increasing(report) and not is_decreasing(report):
        return False

    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
            return False
    return True


def is_report_safe_with_dampener(report):
    if is_report_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_report_safe(modified_report):
            return True
    else:
        return False


def is_increasing(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return False
    return True


def is_decreasing(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


if __name__ == '__main__':
    main()
