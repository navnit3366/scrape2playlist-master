#!/usr/bin/python3
# TODO: remove old file? re-write to same file?

from cfg import *

infile = 'song_list.txt'
outfile = 'drug_music_no_dupe.txt'

def new_file_no_dupe(infile, outfile):
    lines_seen = set()
    outfile = open(outfile, 'w')
    for line in open(infile, 'r'):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

print('de-dupe these lists')
new_file_no_dupe(INFILE, OUTFILE)
print('complete, now find me some adderall...')
