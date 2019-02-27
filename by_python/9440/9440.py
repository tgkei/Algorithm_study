counter = {0:0,
           1:0,
           2:0,
           3:0,
           4:0,
           5:0,
           6:0,
           7:0,
           8:0,
           9:0
           }

def find_min(start = False):
    start_num = 0
    if start:
        start_num = 1
        
    for i in range(start_num, 10):
        if counter[i] != 0:
            min_1 = i
            counter[i] -= 1 
            if counter[i] >=1:
                min_2 = i
                counter[i] -= 1
            else:
                for j in range(i+1,10):
                    if counter[j] != 0:
                        min_2 = j
                        counter[j]-=1
                        break
            break
    return min_1, min_2

while(1):
    input_list = input()

    inputs = input_list.split(' ')
    inputs_len = int(inputs[0])

    if(inputs_len == 0):
        break
    
    num_1 = 0
    num_2 = 0

    for key,value in enumerate(inputs):
        if key != 0:
            value = int(value)
            counter[value] += 1
    
    for i in range(inputs_len //2):
        if i == 0:
            min_1, min_2 = find_min(True)
        else:
            min_1, min_2 = find_min()
            
        num_1 += (min_1 * 10**(inputs_len//2-i-1))
        num_2 += (min_2 * 10**(inputs_len//2-i-1))

    if inputs_len % 2 == 1:
        for key, value in counter.items():
            if value != 0:
                num_1 = num_1 * 10 + key
                counter[key] -= 1
    
    print(num_1+num_2)

    
    num_1 = 0
    num_2 = 0