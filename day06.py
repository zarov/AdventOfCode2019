#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Node:
    def __init__(self, name, parent, level):
        self.name = name
        self.parent = parent
        self.level = level
        self.children = []

    def add(self, node):
        node.parent = self
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def count(self):
        total = self.level
        for child in self.children:
            total += child.count()
        return total

    def find(self, name):
        if self.name == name:
            return self

        for child in self.children:
            c = child.find(name)
            if c:
                return c

    def distance(self, node):
        if self.level <= node.level:
            a = node
            b = self
        else:
            a = self
            b = node

        for _ in range(0, a.level - b.level):
            a = a.parent

        for _ in range(0, a.level):
            if a == b:
                return (self.level - a.level) + (node.level - a.level)
            a = a.parent
            b = b.parent

def insert_node(key, parent, level, odict):
    node = Node(key, parent, level)
    if key in odict:
        for child in odict[key]:
            node.add(insert_node(child, node, level + 1, odict))

    return node


def main():
    with open('input/6.in') as f:
        orbits = f.readlines()

        odict = {}
        for orbit in orbits:
            o = orbit.replace('\n', '').split(')')
            if o[0] not in odict:
                odict[o[0]] = []
            odict[o[0]].append(o[1])

        COM = insert_node('COM', None, 0, odict)
        print('total of orbits is ' + str(COM.count()))

        YOU = COM.find('YOU')
        SAN = COM.find('SAN')
        print('distance between YOU and SAN is ' + str(YOU.distance(SAN) - 2))

if __name__ == "__main__":
    main()
