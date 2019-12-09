#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import math

def get_addr(program, mode, index, number):
    addresses = []
    for n in range(1, number + 1):
        mode = math.floor(mode / 10)
        if mode % 10 == 1:
            addresses.append(index + n)
        else:
            addresses.append(program[index + n])

    return addresses

def execute(program):
    length = len(program)
    p = 0
    while True:
        p = p % length
        opcode = program[p]

        instruction = opcode % 100
        mode = (opcode - instruction) / 10

        if instruction == 1:
            addr = get_addr(program, mode, p, 2)
            program[program[p + 3]] = program[addr[0]] + program[addr[1]]
            p += 4
        elif instruction == 2:
            addr = get_addr(program, mode, p, 2)
            program[program[p + 3]] = program[addr[0]] * program[addr[1]]
            p += 4
        elif instruction == 3:
            addr = get_addr(program, mode, p, 1)
            content = input('Opcode 3 at ' + str(addr[0]) + ' : ')
            program[addr[0]] = int(content)
            p += 2
        elif instruction == 4:
            print('Opcode 4 at', program[p + 1], ':', program[program[p + 1]])
            p += 2
        elif instruction == 5:
            addr = get_addr(program, mode, p, 2)
            if program[addr[0]] != 0: p = program[addr[1]]
            else: p += 3
        elif instruction == 6:
            addr = get_addr(program, mode, p, 2)
            if program[addr[0]] == 0: p = program[addr[1]]
            else: p += 3
        elif instruction == 7:
            addr = get_addr(program, mode, p, 2)
            program[program[p + 3]] = 1 if program[addr[0]] < program[addr[1]] else 0
            p += 4
        elif instruction == 8:
            addr = get_addr(program, mode, p, 2)
            program[program[p + 3]] = 1 if program[addr[0]] == program[addr[1]] else 0
            p += 4
        elif instruction == 99:
            break
        else:
            print('unknown opcode', instruction)
            break

def read(path):
    program = ''
    with open(path) as f:
        program = f.readlines()[0].split(',')
        program = [int(x) for x in program]
    return program
