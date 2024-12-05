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
        # left.sort()
        # right.sort()
        total = 0
        for num_left in left:
            # print(f"num_left: {num_left}")
            count = 0
            for num_right in right:
                # print(f"----- num_right: {num_right} : {count}")
                if (int(num_left) == int(num_right)):
                    count += 1
            if (count != 0):
                # print(f"{num_left} * {count} = {num_left * count}")
                total += int(num_left) * count
        print(total)

if (__name__ == "__main__"):
    main()