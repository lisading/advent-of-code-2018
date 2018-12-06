def get_freq_sum(l):
    freq = 0
    for cur_freq in l:
        freq += int(cur_freq)
    return freq


def find_freq(l):
    cur_freq_sum = 0
    freq_set = set()

    while True:
        for cur_freq in l:
            cur_freq_sum += cur_freq
            if cur_freq_sum in freq_set:
                return cur_freq_sum
            else:
                freq_set.add(cur_freq_sum)


if __name__ == '__main__':
    with open("input") as file:
        freq_list = []
        for line in file:
            freq_list.append(int(line))

        freq_sum = get_freq_sum(freq_list)
        print(freq_sum)

        freq_twice = find_freq(freq_list)
        print(freq_twice)

