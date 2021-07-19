
# s(S) - lower-cased for PEP8
class ConditionedPassword:

    @staticmethod
    def count_letter(s):
        count = 0
        for letter in s:
            if letter.isalpha():
                count += 1
        return count

    @staticmethod
    def count_digit(s):
        count = 0
        for digit in s:
            if digit.isnumeric():
                count += 1
        return count

    def solution(self, s):
        max_word_length = -1
        for password in s:
            if password.isalnum():
                if self.count_letter(password) % 2 == 0 and self.count_digit(password) % 2 != 0:
                    max_word_length = max(len(password), max_word_length)
        return max_word_length


if __name__ == '__main__':
    password_list = list(map(str, input("Please enter the password in the raw form: ").split()))
    # test 5 a0A pass007 ?xy1
    CP = ConditionedPassword()
    print(CP.solution(password_list))  # 7
