#!/usr/bin/env python

with open("bioactivity-18_1_47_13.txt") as f:
    with open("smiles.txt", "w") as ws:
        with open("act.txt", "w") as wa:
            f.readline()
            for l in f:
                ls = l.split("\t")
                ws.write("{} {}\n".format(ls[10],ls[0]))
                wa.write("{} {}\n".format(ls[0],ls[16]))