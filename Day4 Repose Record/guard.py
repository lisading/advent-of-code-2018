def sort_entry(list):
    return sorted(list, key=lambda x: x[0])


def get_asleep_time(sorted_list):
    period_dict = {}
    length_dict = {}
    guard_id = 0
    start_time = 0
    end_time = 0
    for entry in sorted_list:
        action = entry[1].strip()
        if action.split(" ")[1][0] == "#":
            guard_id = action.split(" ")[1][1:]
        if action == 'falls asleep':
            start_time = int(entry[0].split(" ")[1].strip()[-2:])
        if action == 'wakes up':
            end_time = int(entry[0].split(" ")[1].strip()[-2:])
            length = end_time - start_time

            if guard_id != 0 and guard_id in period_dict:
                new_length = length_dict[guard_id] + length
                length_dict[guard_id] = new_length

                new_period_list = period_dict[guard_id]
                for i in range(start_time, end_time):
                    new_period_list[i] += 1
                period_dict[guard_id] = new_period_list

            else:
                length_dict[guard_id] = length

                period_list = [0 for i in range(60)]
                for i in range(start_time, end_time):
                    period_list[i] = 1
                period_dict[guard_id] = period_list

    return period_dict, length_dict


def find_guard_asleep_most(period_dict, length_dict):
    guard_id = max(length_dict, key=length_dict.get)
    period_list = period_dict[guard_id]
    max_freq = -1
    max_time = -1
    for i in range(len(period_list)):
        freq = period_list[i]
        if freq > max_freq:
            max_freq = freq
            max_time = i

    return guard_id, max_time


def find_guard_asleep_most_frequently(period_dict):
    max_frequency = -1
    guard_id = 0
    max_minute = -1
    for cur_guard_id, cur_period in period_dict.items():
        for i in range(len(cur_period)):
            if cur_period[i] > max_frequency:
                max_frequency = cur_period[i]
                max_minute = i
                guard_id = cur_guard_id

    print(max_frequency)
    return guard_id, max_minute


if __name__ == '__main__':

    with open("input.txt") as file:
        entry_list = []
        for line in file:
            date = line.split("]")[0][1:]
            action = line.split("]")[1][1:]
            entry_list.append([date, action])

        sorted_entry_list = sort_entry(entry_list)

        period_dict, length_dict = get_asleep_time(sorted_entry_list)
        print("period dict: ", period_dict)
        print("length dict: ", length_dict)
        guard_id, max_time = find_guard_asleep_most(period_dict, length_dict)
        print("guard id: ", guard_id)
        print("max time: ", max_time)
        print("answer 1: ", int(guard_id) * int(max_time))
        guard_id, max_minute = find_guard_asleep_most_frequently(period_dict)
        print("guard id: ", guard_id)
        print("max minute: ", max_minute)
        print("answer 2: ", int(guard_id) * int(max_minute))