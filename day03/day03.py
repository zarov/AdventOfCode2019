#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import math

def trace_wire(wire):
    x = 0
    y = 0
    trace = []
    for w in wire:
        m = w[0]
        a = int(w[1:])

        if m == 'R':
            for i in range(0, a):
                x += 1
                trace.append((x, y))
        elif m == 'L':
            for i in range(0, a):
                x -= 1
                trace.append((x, y))
        elif m == 'U':
            for i in range(0, a):
                y += 1
                trace.append((x, y))
        elif m == 'D':
            for i in range(0, a):
                y -= 1
                trace.append((x, y))
        else:
            print('error', m)
            return

    return trace

def main():
    with open('input.txt') as f:
        wires = f.readlines()
        wire1 = trace_wire(wires[0].split(','))
        wire2 = trace_wire(wires[1].split(','))

        manhattan = math.inf
        shortest = math.inf
        for w in set(wire1) & set(wire2):
            if w[0] + w[1] < manhattan:
                manhattan = w[0] + w[1]

            d1 = wire1.index(w)
            d2 = wire2.index(w)
            if d1 + d2 < shortest:
                shortest = d1 + d2

        print('manhattan distance is', manhattan)
        print('shortest distance is', shortest + 2)

if __name__ == "__main__":
    main()
