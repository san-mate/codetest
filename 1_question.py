#!/bin/python


if __name__ == '__main__':
    input1 = raw_input()
    input2 = raw_input()
    input3 = raw_input()
    input4 = raw_input()
    for input in [input1, input2, input3, input4]:
        a, b = map(int, input.split(','))
        rows = []
        row = []
        for i in xrange(1, (a*b)+1):
            row.append(i)
            if i % b == 0:
                rows.append(row)
                row = []
        print rows
