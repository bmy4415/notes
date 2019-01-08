'''
Check whether equation is valid in human level
- exclude double consecutive operator
'''


import re

double_op = re.compile(r'[+*/-]{2,}')
paren = re.compile(r'\((?P<inner>[^()]*)\)') # inner most parenthesis
num = re.compile(r'^[+-]?(0|[1-9][0-9]*)([.][0-9]+)?$')
ops = re.compile(r'[+*/-]')

def is_valid_exp(exp):
    exp = ''.join(exp.split(' '))
    if len(exp) == 0:
        return False

    if double_op.search(exp):
        return False

    if num.search(exp):
        return True

    if paren.search(exp):
        if is_valid_exp(paren.search(exp).group('inner')): # if inside of parenthesis is valid, remove paren
            return is_valid_exp(paren.sub('0', exp))

        else:
            return False

    for op in ops.finditer(exp):
        if op.start()==0 and op.group() in ['+', '-']: # unary operator
            continue

        left = exp[:op.start()]
        right = exp[op.start()+1:]
        if is_valid_exp(left) and is_valid_exp(right):
            return True
        else:
            return False

    # wrong number, wrong parenthesis, etc.
    return False

tests = [
    ['(3)', True],
    [')3', False],
    ['-(-3)', True],
    ['--2', False],
    ['1 + -1', False],
    ['-3 + 3', True],
    ['1 * -3', False],
    ['0003 + 2', False],
    ['0.12', True],
    ['((3))', True],
    ['1-(-1)', True],
    ['123.', False],
    ['00.123', False],
    ['01', False],
    ['1..1', False]
]


for test in tests:
    eq, ans = test
    print(eq.rjust(20), 'ans:', str(ans).rjust(5), 'my:', str(is_valid_exp(eq)).rjust(5))