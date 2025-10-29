def read_file_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

names = read_file_to_string('project_euler/problem/022/names.txt')

def solve():
    names_arr = names.replace("\"", "").split(',')
    names_arr.sort()
    r_total = 0
    
    for i in range(len(names_arr)):
        name = names_arr[i]
        value = 0
        for alpha in name:
            value += get_alpha_value(alpha)
        r_total += (value * (i + 1))
    
    return r_total

def get_alpha_value(a: str):
    match a.lower():
        case 'a': return 1
        case 'b': return 2
        case 'c': return 3
        case 'd': return 4
        case 'e': return 5
        case 'f': return 6
        case 'g': return 7
        case 'h': return 8
        case 'i': return 9
        case 'j': return 10
        case 'k': return 11
        case 'l': return 12
        case 'm': return 13
        case 'n': return 14
        case 'o': return 15
        case 'p': return 16
        case 'q': return 17
        case 'r': return 18
        case 's': return 19
        case 't': return 20
        case 'u': return 21
        case 'v': return 22
        case 'w': return 23
        case 'x': return 24
        case 'y': return 25
        case 'z': return 26

actual = solve()
print(actual)