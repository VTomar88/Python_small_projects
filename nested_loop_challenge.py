"""
This is nested loop challenge. Using nested loop print in the following format
xxxx
xx
xxxx
xx
xx
"""
for x_count in range(2):
    print('xxxx')
    for _ in range(x_count+1):
        print('xx')
        