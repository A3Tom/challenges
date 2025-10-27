# Number Letter Counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

numeric_word_map = {
    1: 'one',   10: 'ten',     11: 'eleven',
    2: 'two',   20: 'twenty',  12: 'twelve', 
    3: 'three', 30: 'thirty',  13: 'thirteen', 
    4: 'four',  40: 'forty',   14: 'fourteen',
    5: 'five',  50: 'fifty',   15: 'fifteen',
    6: 'six',   60: 'sixty',   16: 'sixteen',
    7: 'seven', 70: 'seventy', 17: 'seventeen',
    8: 'eight', 80: 'eighty',  18: 'eighteen',
    9: 'nine',  90: 'ninety',  19: 'nineteen',
}

def solve(n):
    i = 1
    r_total = 0

    while i <= n:
        word = get_numeric_word(i)
        l_count = len(word.replace(' ', ''))
        r_total += l_count
        i += 1

    return r_total


def get_numeric_word(n):
    n_string = str(n)
    remaining_chars = len(n_string)
    numeric_word = ''

    while remaining_chars > 0:
        idx = len(n_string) - remaining_chars
        char = int(n_string[idx])

        if char == 0:
            remaining_chars -= 1
            continue

        match remaining_chars:
            case 4: 
                has_following_chars = number_has_following_chars(n_string, idx)
                numeric_word += f'{numeric_word_map[char]} thousand{' ' if has_following_chars else ''}'
            case 3: 
                has_following_chars = number_has_following_chars(n_string, idx)
                numeric_word += f'{numeric_word_map[char]} hundred{' and ' if has_following_chars else ''}'
            case 2: 
                char *= 10

                if char < 20:
                    char += int(n_string[idx + 1])
                    remaining_chars -= 1

                numeric_word += numeric_word_map[char]
            case _:
                numeric_word += numeric_word_map[char]
        
        remaining_chars -= 1
    return numeric_word

def number_has_following_chars(n_string, idx):
    return int(n_string[idx + 1:len(n_string)]) > 0


n_test_case_1 = 5
n_test_case_2 = 342
n_test_case_3 = 115
n_test_case_4 = 203

n_question = 1000

actual = solve(n_question)

print(actual)