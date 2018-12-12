def check_overlap_claim(claim_list, overlap_claim):
    for claim in claim_list:
        coord = claim.split(" ")[2]
        area = claim.split(" ")[3]
        left_edge = int(coord.split(",")[0])
        top_edge = int(coord.split(",")[1][:-1])
        wide = int(area.split("x")[0])
        tall = int(area.split("x")[1])

        for x in range(left_edge, left_edge + wide):
            for y in range(top_edge, top_edge + tall):
                if overlap_claim[x][y] == 0:
                    overlap_claim[x][y] = 1
                else:
                    overlap_claim[x][y] += overlap_claim[x][y]
    return overlap_claim


def check_overlap_size(overlap_claim):
    size = 0
    for i in range(len(overlap_claim)):
        for j in range(len(overlap_claim[0])):
            if overlap_claim[i][j] >= 2:
                size += 1
    return size


def check_non_overlap_size(overlap_claim):

    id = 0
    for claim in claim_list:
        coord = claim.split(" ")[2]
        area = claim.split(" ")[3]
        left_edge = int(coord.split(",")[0])
        top_edge = int(coord.split(",")[1][:-1])
        wide = int(area.split("x")[0])
        tall = int(area.split("x")[1])
        intact_claim = True

        for x in range(left_edge, left_edge + wide):
            for y in range(top_edge, top_edge + tall):
                if overlap_claim[x][y] != 1:
                    intact_claim = False
                    break

        if intact_claim:
            id = claim.split(" ")[0][1:]

    return id


if __name__ == '__main__':

    with open("input.txt") as file:
        claim_list = []
        for line in file:
            claim_list.append(line)

        overlap_claim = [[0 for x in range(1000)] for u in range(1000)]

        overlap_claim = check_overlap_claim(claim_list, overlap_claim)
        overlap_size = check_overlap_size(overlap_claim)
        print(overlap_size)

        non_overlap_size = check_non_overlap_size(overlap_claim)
        print(non_overlap_size)

