# current version without MD files and creating subdirectories
import os
from datetime import datetime, timedelta
import csv
from typing import List


#csv file from now on
def mac():
 try:
     with open(os.path.expanduser(f'~/Downloads/replay {str(datetime.today().year)}.txt'), 'r', encoding='utf-16') as file:
         raw = file.read().split('\n')[:101]

     #extract the necessary data
         raw[0] = raw[0].split('\t')[:2] + raw[0].split('\t')[3:4] + raw[0].split('\t')[16:17] + raw[0].split('\t')[9:10] + raw[0].split('\t')[11:12] + raw[0].split('\t')[25:26]
         raw[0].insert(0, 'Position')
         for i in range(1, len(raw)):
             raw[i] = raw[i].split('\t')[:2]+raw[i].split('\t')[3:4] + raw[i].split('\t')[16:17] + raw[i].split('\t')[9:10] + time(raw[i].split('\t')[11:12]) + raw[i].split('\t')[25:26]
             raw[i].insert(0, i)

     # os.remove(os.path.expanduser(f'~/Downloads/replay {str(datetime.today().year)}.txt'))
     os.chdir('/Users/minhphan/Documents/apple-music-replay/replay/replay23/')
     d = date()
     csvfile(raw, d)
 except Exception as e:
     print(e)


def csvfile(arr: List[str], date):
    if not os.path.isfile(f"{date}.csv"):
        with open(f"{date}.csv","w",newline='', encoding='utf-8') as file:
            obj = csv.writer(file)
            for i in range(len(arr)):
                obj.writerow([n for n in arr[i]])


def time(l:List)-> List:
 return [str(timedelta(seconds=int(l[0])))]


def date():
    day = datetime.today()
    dofw = day.isoweekday()
    if dofw != 7:
        day = day - datetime.timedelta(dofw)
    return day.strftime('%m-%d-%y')
