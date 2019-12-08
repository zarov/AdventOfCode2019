#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def get_addr(program, mode, index, number):
    addresses = []
    for n in range(1, number + 1):
        mode = mode / 10
        if mode % 10 == 1:
            addresses.append(index + n)
        else:
            addresses.append(program[index + n])

    return addresses

def opcode1(program, mode, index):
    addr = get_addr(program, mode, index, 2)
    program[program[index + 3]] = program[addr[0]] + program[addr[1]]

def opcode2(program, mode, index):
    addr = get_addr(program, mode, index, 2)
    program[program[index + 3]] = program[addr[0]] * program[addr[1]]

def opcode3(program, mode, index):
    addr = get_addr(program, mode, index, 1)
    #  content = input('Opcode 3 at ' + str(addr[0]) + ' : ')
    program[addr[0]] = 1

def opcode4(program, mode, index):
    #  addr = get_addr(program, mode, index, 1)
    print('Opcode 4 at', program[index + 1], ':', program[program[index + 1]])

def execute(program):
    length = len(program)
    i = 0
    while True:
        i = i % length
        opcode = program[i]

        instruction = opcode % 100
        mode = (opcode - instruction) / 10

        if instruction == 1:
            opcode1(program, mode, i)
            i += 4
        elif instruction == 2:
            opcode2(program, mode, i)
            i += 4
        elif instruction == 3:
            opcode3(program, mode, i)
            i += 2
        elif instruction == 4:
            opcode4(program, mode, i)
            i += 2
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
