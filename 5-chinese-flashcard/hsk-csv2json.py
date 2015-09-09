#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import csv
import json

pinyinToneMarks = {
    u'a': u'āáǎà', u'e': u'ēéěè', u'i': u'īíǐì',
    u'o': u'ōóǒò', u'u': u'ūúǔù', u'ü': u'ǖǘǚǜ',
    u'A': u'ĀÁǍÀ', u'E': u'ĒÉĚÈ', u'I': u'ĪÍǏÌ',
    u'O': u'ŌÓǑÒ', u'U': u'ŪÚǓÙ', u'Ü': u'ǕǗǙǛ'
}

def convertPinyinCallback(m):
    tone=int(m.group(3))%5
    r=m.group(1).replace(u'v', u'ü').replace(u'V', u'Ü')
    # for multple vowels, use first one if it is a/e/o, otherwise use second one
    pos=0
    if len(r)>1 and not r[0] in 'aeoAEO':
        pos=1
    if tone != 0:
        r=r[0:pos]+pinyinToneMarks[r[pos]][tone-1]+r[pos+1:]
    return r+m.group(2)

def convertPinyin(s):
    return re.sub(ur'([aeiouüvÜ]{1,3})(n?g?r?)([012345])', convertPinyinCallback, s, flags=re.IGNORECASE)

# print convertPinyin(u'Ni3 hao3 ma0?')

data = []
with open('../csv/HSK_Level_1_(New_HSK).csv') as csvfile:
	wordlist = csv.reader(csvfile, delimiter=',', quotechar='"')
	next(wordlist)
	for word in wordlist:
		order = word[0]
		hskLevelOrder = word[1]
		chinese = word[2]
		pinyin = convertPinyin(word[3])
		english = word[4]
		data.append({'order':order,'hsk':hskLevelOrder, 'cn':chinese, 'en':english, 'pinyin':pinyin})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
