def main():
    with open("input.txt", 'r') as file:
        left = []
        right = []
        line = file.readline()
        while (line):
            numbers = line.split("   ")
            left.append(numbers[0])
            right.append(numbers[1])
            line = file.readline()
        left.sort()
        right.sort()
        total = 0
        for i, num in enumerate(left):
            total += abs(int(left[i]) - int(right[i]))
        print(total)

if (__name__ == "__main__"):
    main()