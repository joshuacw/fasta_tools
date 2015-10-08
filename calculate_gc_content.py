#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys
import argparse
from decimal import *
getcontext().prec = 2

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
args = parser.parse_args()
print args.fasta

a_count = 0
c_count = 0
g_count = 0
t_count = 0

a_pct = 0
c_pct = 0
g_pct = 0
t_pct = 0

total_bases = 0

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        a_count = a_count + line.count("A")  
        c_count = c_count + line.count("C")
        g_count = g_count + line.count("G")
        t_count = t_count + line.count("T")

total_bases = a_count + c_count + g_count + t_count

a_pct = (Decimal(a_count) / Decimal(total_bases)) * 100
c_pct = (Decimal(c_count) / Decimal(total_bases)) * 100
g_pct = (Decimal(g_count) / Decimal(total_bases)) * 100
t_pct = (Decimal(t_count) / Decimal(total_bases)) * 100

gc_content = ((Decimal(g_count) + Decimal(c_count)) / Decimal(total_bases)) * 100

print("Base counts for file %s:" % sys.argv[1])
print("A: %d" % a_count)
print("C: %d" % c_count)
print("G: %d" % g_count)
print("T: %d" % t_count)
print ""
print "Base percentages:"
print "A: %d%%" % a_pct
print "C: %d%%" % c_pct
print "G: %d%%" % g_pct
print "T: %d%%" % t_pct
print ""
print "GC Content:"
print "%d%%" % gc_content
