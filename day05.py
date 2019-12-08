#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import Intcode

def main():
    program = Intcode.read('input/5.in')
    Intcode.execute(program)

if __name__ == "__main__":
    main()
