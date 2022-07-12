#!/usr/bin/env python3

import sys
import os 

domain = sys.argv[1]

os.system('cat ~/Wordlists/wordlist > wordlist')
wordlist = open('wordlist', 'r')
wordlist = wordlist.readlines()

wordlist_temp = open("wordlist_temp", 'w')

for line in wordlist:
	wordlist_temp.write(line.rstrip()+'.'+domain.rstrip()+'\n')

wordlist_temp.close()

os.system('massdns -r ~/Downloads/massdns/lists/resolvers.txt -t AAAA wordlist_temp -o S > resolve_results.txt')

os.system('rm -rf wordlist_temp')

results = open('resolve_results.txt', 'r')
results = results.readlines()
final_results = open(sys.argv[2], 'w')

for line in results:
	if ". CNAME " in line:
		final_results.writelines(line.split(". CNAME ")[0]+'\n')
	if ". AAAA " in line:
		final_results.writelines(line.split(". AAAA ")[0]+'\n')




