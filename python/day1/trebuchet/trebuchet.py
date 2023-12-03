def main():
    print(calibrationData())

def calibrationData():
    """
    Calibration Data Count:
    Function read the file calibrations.txt and get the count
    """
    with open('input.txt', 'r') as file:
        data = file.readlines()
    
    count = 0

    for d in data:
        record = []
        
        for i in d.strip('\n'):
            if i.isnumeric():
                record.append(i)
        if len(record) > 1:
            count += int(f"{record[0]}{record[-1]}")
        elif len(record) == 1:
            count += int(f"{record[0]}{record[0]}")
    return count

        

if __name__ == '__main__':
    main()