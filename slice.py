
class Slice:

    @staticmethod
    def discreteness(arr):
        discreteness_array = [arr[0]]
        len_array = len(arr)

        for i in range(1, len_array):
            discreteness_array.append(discreteness_array[-1] + arr[i])
        return discreteness_array

    @staticmethod
    def solution(arr):
        d = {}
        for i, value in enumerate(arr):
            d[value] = i

        max_len = 0
        for i, value in enumerate(arr):
            max_len = max(max_len, d[value] - i)
        return max_len


if __name__ == '__main__':
    s = Slice()
    A = list(map(int, input("Please enter array: ").split()))
    print(s.solution(s.discreteness(A)))
    # input: -1 -1 1 -1 1 0 1 -1 -1 | output: 7
    # input: 1 1 -1 -1 -1 -1 -1 -1 1 1 | output: 4
