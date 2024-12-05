    
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
            else:
                found = False
                for i, num in enumerate(numbers):
                    if (found == False):
                        strip = []
                        for nb in numbers:
                            strip.append(int(nb))
                        strip.pop(i)
                        safe = True
                        for j, number in enumerate(strip):
                            if (j > 0):
                                if (strip[0] < strip[1]):
                                    if ((strip[j - 1]) >= int(number) or (number) - int(strip[j - 1]) > 3):
                                        safe = False
                                else:
                                    if ((strip[j - 1]) <= int(number) or (strip[j - 1]) - int(number) > 3):
                                        safe = False
                        if (safe == True):
                            found = True
                if (found == True):
                    total += 1
            line = file.readline()
        print(total)

if (__name__ == "__main__"):
    main()