#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import Intcode

def main():
    program = Intcode.read('input/2.in')
    program[1] = 12
    program[2] = 2

    Intcode.execute(program)

    print('For 1202, first operation is', program[0])
    print("""By manually testing different input, we can see that the noun
increases a lot the final result, and the verb increases only by its
value the final result. Thus, finding the closest noun (5 tries), and
calculating the remainer, we have: 5696.""")

if __name__ == "__main__":
    main()
