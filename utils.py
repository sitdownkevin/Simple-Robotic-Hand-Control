'''
@author: sitdownkevin
@data:   2023.4.12
'''

def decimal_to_ternary(num):
    if num == 0:
        return '00000'
    ternary = ''
    while num != 0:
        remainder = num % 3
        ternary = str(remainder) + ternary
        num //= 3
    ternary = ternary.rjust(5, '0')
    return ternary

def string_to_binary(ternaryStr):
    binary_dict = {
        '0': '00',
        '1': '01',
        '2': '10'
    }
    binary = ''
    for num in ternaryStr:
        assert int(num) < 3
        binary += binary_dict[num]
    
    return binary

def encode(num) -> str:
    return string_to_binary(decimal_to_ternary(num))

def translate(command):
    assert len(command) == 10
    motion_dict = {
        '00': '静止',
        '01': '正转',
        '10': '反转'
    }
    print(f'A: {motion_dict[command[0:2]]}\n' + \
          f'B: {motion_dict[command[2:4]]}\n' + \
          f'C: {motion_dict[command[4:6]]}\n' + \
          f'D: {motion_dict[command[6:8]]}\n' + \
          f'E: {motion_dict[command[8:10]]}\n'
        )


if __name__ == "__main__":
    for cmd in range(243):
        cmd_ = encode(cmd)
        print(f'{cmd} -> {cmd_}')
        translate(cmd_)
    
        