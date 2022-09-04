# print the map
def print_map(map):
    n = len(map)
    m = len(map[0])
    for j in range(m):
        for i in range(n):
            print(map[i][j], end=' ')
        print()


def check_up(map, i, j):
    if i <= 0:
        return False
    if map[i-1][j] != 0:
        return True
    return False


def check_left(map, i, j):
    if j <= 0:
        return False
    if map[i][j-1] != 0:
        return True
    return False

# upperleft 부터 탐색
# map값이 1일때,
#   왼쪽과 위가 모두 0이면, 새로운 그룹이라 판정하고 id를 부여 (이후 id를 1 증가시킨다)
#   한쪽이라도 0이 아니면, 0이 아닌 그룹 id를 가져옴

T = int(input())

M = [0 for _ in range(T)]
N = [0 for _ in range(T)]
K = [0 for _ in range(T)]
cabbage_locations = []

for t in range(T):
    M[t], N[t], K[t] = [int(x) for x in input().split()]
    for i in range(K[t]):
        cabbage_locations.append([int(x) for x in input().split()])

for t in range(T):
    map = [[0 for _ in range(N[t])] for _ in range(M[t])]
    for i in range(K[t]):
        x, y = cabbage_locations[i]
        map[x][y] = -1

    id = 1
    id_map = [[0 for _ in range(M[t]*N[t]//2)] for _ in range(M[t]*N[t]//2)]
    for i in range(M[t]):
        for j in range(N[t]):
            # if current location is cabbage
            if map[i][j] == -1:
                if check_up(map, i, j) and check_left(map, i, j):
                    map[i][j] = map[i-1][j]
                    # if left and up is in the different group
                    if map[i][j-1] != map[i-1][j]:
                        low_id = min(map[i][j-1], map[i-1][j])
                        high_id = max(map[i][j-1], map[i-1][j])
                        id_map[low_id][high_id] = 1
                        #id_map[map[i-1][j]][map[i][j-1]] = 1
                elif check_up(map, i, j):
                    map[i][j] = map[i-1][j]
                elif check_left(map, i, j):
                    map[i][j] = map[i][j-1]
                else:
                    map[i][j] = id
                    id += 1
    # print_map(id_map)
    # print("="*10 + "map" + "="*10)
    # print_map(map)
    # print()
    # print()
    # print("="*10 + "id_map" + "="*10)
    # print_map(id_map)
    num_of_groups = 0
    for row in id_map:
        for col in row:
            if col == 1:
                num_of_groups += 1
                break
    answer = (id-1) - num_of_groups
    print(answer)