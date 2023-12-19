# AOC 2023
# --- Day 19: Aplenty ---

import networkx as nx
import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
import numpy as np
import functools
import json


def solve():
    part_1 = 0
    part_2 = 0

    s = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".split(
        "\n\n"
    )

    parts = []
    for x in [y for y in s[1].split("\n") if y]:
        parts.append(
            {z[0]: int(z[1]) for z in [y.split("=") for y in x[1:-1].split(",")]}
        )

    rules = {}

    for x in s[0].split("\n"):
        name, rest = x.split("{")

        r = rest[:-1].split(",")

        tmp = []
        for k in r[:-1]:
            rule, move = k.split(":")
            if "<" in rule:
                opr = "<"
                var, val = rule.split("<")
            else:
                opr = ">"
                var, val = rule.split(">")

            tmp.append([var, opr, int(val), move])

        rules[name] = tmp

    print(rules)
    print(parts)

    accepted = []

    for part in parts:
        cur_rule_name = "in"
        while True:
            cur_rule = rules[cur_rule_name]
            for rule in cur_rule:
                if len(rule) == 1:
                    cur_rule

                pos, opr, value, move = rule
                if eval(f"{part[pos]} {opr} {value}"):
                    # Rule "OK"
                    cur_rule_name = move
                    break
                else:
                    continue

        pass

    return part_1, part_2


part_1, part_2 = solve()
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
# assert part_1 ==
# assert part_2 ==
