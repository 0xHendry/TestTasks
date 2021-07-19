
class HammingDistance:

    @staticmethod
    def hammingDist(str1, str2):
        i = 0
        count = 0

        while i < len(str1):
            if str1[i] != str2[i]:
                count += 1
            i += 1
        return count


if __name__ == '__main__':
    first_DNA = "GAGCCTACTAACGGGAT"
    second_DNA = "CATCGTAATGACGGCCT"
    HD = HammingDistance()
    print(HD.hammingDist(first_DNA, second_DNA))
