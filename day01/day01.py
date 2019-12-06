#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import math

def get_fuel_for(m):
    return math.floor(m / 3) - 2

def get_fuel_fuel_for(f):
    total = 0
    fuel = get_fuel_for(f)
    while fuel > 0:
        total += fuel
        fuel = get_fuel_for(fuel)

    return total

def main():
    partial_fuel = 0
    total_fuel = 0
    with open('input.txt') as f:
        masses = f.readlines()
        for mass in masses:
            module_fuel = get_fuel_for(int(mass))
            fuel_fuel = get_fuel_fuel_for(module_fuel)
            partial_fuel += module_fuel
            total_fuel += module_fuel + fuel_fuel

    print("fuel necessary for the modules:", partial_fuel)
    print("total fuel necessary:", total_fuel)

if __name__ == "__main__":
    main()
