from itertools import combinations


def get_cur_check_sum(box_id, twice_appearance, three_times_appearance):
    letter_list = list(box_id)
    letter_dict = {}
    for letter in letter_list:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    twice_appearance_flag = False
    three_times_appearance_flag = False

    for letter in letter_dict:
        if letter_dict[letter] == 2 and not twice_appearance_flag:
            twice_appearance += 1
            twice_appearance_flag = True
        elif letter_dict[letter] == 3 and not three_times_appearance_flag:
            three_times_appearance += 1
            three_times_appearance_flag = True

    return twice_appearance, three_times_appearance


def get_check_sum(id_list):
    twice_appearance = 0
    three_times_appearance = 0
    for box_id in id_list:
        twice_appearance, three_times_appearance \
            = get_cur_check_sum(box_id, twice_appearance, three_times_appearance)
    return twice_appearance * three_times_appearance


def get_correct_box(box_id_1, box_id_2):
    box_id_list_1 = list(box_id_1)
    box_id_list_2 = list(box_id_2)
    total_diff = 0
    correct_box = []

    for inx, val in enumerate(box_id_list_1):
        if box_id_list_1[inx] != box_id_list_2[inx]:
            total_diff += 1
            if total_diff == 2:
                return False, ""
        else:
            correct_box.append(val)

    return True, "".join(correct_box)


def get_common_letters(id_list):
    for box_id_1, box_id_2 in combinations(id_list, 2):
        correct_box_flag, correct_box = get_correct_box(box_id_1, box_id_2)
        if correct_box_flag:
            return correct_box


if __name__ == '__main__':
    with open("input.txt") as file:
        box_id_list = []
        for line in file:
            box_id_list.append(line)

        check_sum = get_check_sum(box_id_list)
        print(check_sum)

        common_letters = get_common_letters(box_id_list)
        print(common_letters)
