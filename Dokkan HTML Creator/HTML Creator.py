import os

try:
    os.mkdir('results')
    print("Created results folder")
except:
    ''

region = raw_input("What region is the account for? ")
stones = raw_input("How many dragon stones does the account have? ")
lrs = raw_input("How many LRs does the account have? ")
cards = raw_input("What card IDs does the account have? ")

data = '<!DOCTYPE html><html lang = "en"><head><meta charset="utf-8" /><title>Dokkan Battle Account</title><link rel="stylesheet" href="main.css"></head><body><b>Region: '+region+'<br>Stones: '+stones+'<br>LRs: '+lrs+'<br><img src="C:/Dokkan HTML Creator/Cards/'+cards+'.png" style="width:150px;height:150px;"></body></html>'

f = open(os.path.join('results', cards+'.html'), 'w')
f.write(data)
f.close()