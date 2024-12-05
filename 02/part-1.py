    
def main():
    with open("input.txt", 'r') as file:
        line = file.readline()
        total = 0
        while (line):
            numbers = line.split(" ")
            safe = True
            for i, num in enumerate(numbers):
                if (i > 0):
                    if (int(numbers[0]) < int(numbers[1])):
                        if ((int(numbers[i - 1]) >= int(num)) or (int(num) - int(numbers[i - 1]) > 3)):
                            safe = False
                    else:
                        if ((int(numbers[i - 1]) <= int(num)) or (int(numbers[i - 1]) - int(num) > 3)):
                            safe = False
            if (safe):
                total += 1
            line = file.readline()
        print(total)

if (__name__ == "__main__"):
    main()