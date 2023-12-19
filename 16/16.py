import init
import re
import numpy as np

data = init.read_data(isTest=True, )

global energised_tiles
global maxi, maxj
energised_tiles = []

# make the individual matrix
matrix = []
maxi = -1
for line in data:
    maxi += 1
    split = re.split('', line)
    split = split[1:len(split) - 1]
    matrix.append(split)
    # print(split)
maxj = len(matrix[0]) - 1


# matrix[i][j] i = row index, j = col index

def where_next(current_location, direction, symbol):
    if symbol == '.':
        return 1, np.concatenate((current_location + direction, direction), axis=None)

    # results in left
    elif (np.array_equal(direction, [-1, 0]) and symbol == '\\') or (
            np.array_equal(direction, [1, 0]) and symbol == '/'):
        return 1,  np.concatenate((current_location + [0, -1], [0, -1]), axis=None)

    elif np.array_equal(direction, [0, -1]) and symbol == '-':
        return 1, np.concatenate((current_location + [0, -1], [0, -1]), axis=None)

    # results in right
    elif (np.array_equal(direction, [1, 0]) and symbol == '\\') or (
            np.array_equal(direction, [-1, 0]) and symbol == '/'):
        return 1, np.concatenate((current_location + [0, 1], [0, 1]), axis=None)

    elif np.array_equal(direction, [0, 1]) and symbol == '-':
        return 1, np.concatenate((current_location + [0, 1], [0, 1]), axis=None)

    # results in up
    elif (np.array_equal(direction, [0, -1]) and symbol == '\\') or (
            np.array_equal(direction, [0, 1]) and symbol == '/'):
        return 1, np.concatenate((current_location + [-1, 0], [-1, 0]), axis=None)

    elif np.array_equal(direction, [-1, 0]) and symbol == '|':
        return 1, np.concatenate((current_location + [-1, 0], [-1, 0]), axis=None)

    # results in down
    elif (np.array_equal(direction, [0, 1]) and symbol == '\\') or (
            np.array_equal(direction, [0, -1]) and symbol == '/'):
        return 1, np.concatenate((current_location + [1, 0], [1, 0]), axis=None)

    elif np.array_equal(direction, [1, 0]) and symbol == '|':
        return 1, np.concatenate((current_location + [1, 0], [1, 0]), axis=None)

    # results in two (up & down)
    elif (np.array_equal(direction, [0, 1]) or np.array_equal(direction, [0, -1])) and symbol == '|':
        return 2, np.concatenate((current_location + [1, 0], [1, 0]), axis=None), np.concatenate((current_location + [-1, 0], [-1, 0]), axis=None)

    # results in two (left & right)
    elif (np.array_equal(direction, [1, 0]) or np.array_equal(direction, [-1, 0])) and symbol == '-':
        return 2, np.concatenate((current_location + [0, 1], [0, 1]), axis=None), np.concatenate((current_location + [0, -1], [0, -1]), axis=None)


def part1():
    tiles_to_check = [[0, 0, 0, 1]]
    # format of entries [i, j, i_direction, j_direction]

    while tiles_to_check:

        for tile in tiles_to_check:
            print('still to check', tiles_to_check, '\n')
            print('checking tile', tile)
            current_location = np.array([tile[0], tile[1]])
            direction = np.array([tile[2], tile[3]])

            # check if out of range:
            i, j = tile[0], tile[1]
            if i < 0 or j < 0 or i > maxi or j > maxj:
                # out of range of the matrix, so can discard
                tiles_to_check.remove(tile)
                print('out of range so removed.')
                break

            symbol = matrix[tile[0]][tile[1]]
            print('found symbol of', symbol, 'at', [tile[0], tile[1]])

            if [[tile[0], tile[1]]] not in energised_tiles:
                energised_tiles.append([tile[0], tile[1]])

            result = where_next(current_location, direction, symbol)

            tiles_to_check.remove(tile)
            print(result)

            tiles_to_check.append(result[1].tolist())
            if result[0] == 2:
                tiles_to_check.append(result[2].tolist())



            print('energised:', sorted(energised_tiles))
            print('energised count', len(energised_tiles))

    return len(energised_tiles)


def part2():
    return False


print(f'Part 1: {part1()}, Part 2: {part2()}')
