import os
from collections import Counter

def part1(input_array1, input_array2):
    sum = 0
    for i in range(len(input_array1)):
        sum += abs(input_array1[i] - input_array2[i])


    return sum

def part2(input_array1, input_array2):
    similarity = 0
    countered_list1, countered_list2 = Counter(input_array1), Counter(input_array2)
    dict_list1, dict_list2 = dict(countered_list1), dict(countered_list2)

    for key in dict_list1:
        if key in dict_list2:
            similarity += dict_list1[key] * key * dict_list2[key]

    return similarity

def main():
    current_path = os.path.dirname(__file__)
    input_path = "day1-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array1, input_array2 = [], []

    for line in input:
        split_line = line.split()
        input_array1.append(int(split_line[0]))
        input_array2.append(int(split_line[1]))

    input_array1.sort()
    input_array2.sort()

    part1_answer = part1(input_array1, input_array2)
    part2_answer = part2(input_array1, input_array2)
    
    print('\n' + str(part1_answer))
    print('\n' + str(part2_answer))

if __name__ == '__main__':
    main()