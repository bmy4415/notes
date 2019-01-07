import re

items = [
    'park 010-9999-9988',
    'kim 010-9909-7789',
    'lee 010-8789-7768',
]

pattern = re.compile(r'(?P<name>\w)\s(?P<n1>\d+)[-](?P<n2>\d+)[-](?P<n3>\d+)')
for item in items:
    print(pattern.sub('\g<name> \g<n1>-\g<n2>-####', item))

items = [
    'park@naver.com',
    'kim@daum.net',
    'lee@myhome.co.kr'
]

pattern = re.compile(r'.*[@].*[.](?=com$|net$)')
for item in items:
    if pattern.match(item):
        print(item, 'yes')
    else:
        print(item, 'no')