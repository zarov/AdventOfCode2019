#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def main():
    with open('input.txt') as f:
        instructions = f.readlines()[0].split(',')

        instructions = [int(i) for i in instructions]

        # 1202 code
        instructions[1] = 12
        instructions[2] = 2

        length = len(instructions)
        i = 0
        while True:
            c = instructions[i % length]
            in0 = instructions[i + 1]
            in1 = instructions[i + 2]
            out = instructions[i + 3]
            if c == 1:
                instructions[out] = instructions[in0] + instructions[in1]
            elif c == 2:
                instructions[out] = instructions[in0] * instructions[in1]
            elif c == 99:
                break
            else:
                print("error", i, c)
                break

            i += 4

        print('For 1202, first operation is', instructions[0])
        print("""By manually testing different input, we can see that the noun
increases a lot the final result, and the verb increases only by its
value the final result. Thus, finding the closest noun (5 tries), and
calculating the remainer, we have: 5696.""")

if __name__ == "__main__":
    main()
