low_alp = "abcdefghijklmnopqrstuvwxyz"
cap_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"

def level(input_string):
	ret = 0
    is_low = False
    is_cap = False
    is_num = False
    is_spe = False

    for char in input_string:
        if char in num:
            if not is_num: ret += 1
            is_num = True
            continue
        if char in low_alp:
            if not is_low: ret += 1
            is_low = True
            continue
        if char in cap_alp:
            if not is_cap: ret += 1
            is_cap = True
            continue
        if not is_spe:
            is_spe = True
            ret += 1
    return ret
	

user_input = input()
lev = level(user_input)
print(f'LEVEL{lev}')