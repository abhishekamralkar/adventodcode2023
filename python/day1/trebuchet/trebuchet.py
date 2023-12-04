def main():
    print(calibrationData())

def calibrationData():
    """
    Calibration Data Count:
    Function read the file calibrations.txt and get the count
    """
    with open('input.txt', 'r') as file:
        data = file.read().strip()
    
    count = 0
    count2 = 0

    for d in data.split("\n"):
        record = []
        record2 = []
        for i, v in enumerate(d):
            if v.isdigit():
                record.append(v)
                record2.append(v)
            for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if d[i:].startswith(val):
                    record2.append(str(j+1))
        count += int(record[0]+record[-1])
        count2 += int(record2[0]+record2[-1])
    return count, count2


if __name__ == '__main__':
    main()