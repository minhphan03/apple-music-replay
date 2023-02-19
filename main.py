# using offline itunes to generate and update Apple Music Replay playlists
# data, then upload files to GitHub
import os
import datetime
import csv
from typing import List

from mdutils.mdutils import MdUtils
#csv and markdown files
def main():
    try:
        with open(os.path.expanduser('~/Downloads/replay 2021.txt'), 'r', encoding='utf-16') as file:
            raw = file.read().split('\n')[:101]

        #extract the necessary data
            raw[0] = raw[0].split('\t')[:2] + raw[0].split('\t')[3:4] + raw[0].split('\t')[9:10] + raw[0].split('\t')[11:12] + raw[0].split('\t')[25:26]
            raw[0].insert(0, 'Position')
            for i in range(1, len(raw)):
                raw[i] = raw[i].split('\t')[:2]+raw[i].split('\t')[3:4] + raw[i].split('\t')[9:10] + time(raw[i].split('\t')[11:12]) + raw[i].split('\t')[25:26]
                raw[i].insert(0, i)

        # for i in raw:
        #     print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        os.remove(os.path.expanduser('~/Downloads/replay 2021.txt'))
        [path, date] = check()
        os.chdir(path)
        print(*raw, sep='\n')
        csvfile(raw, date)
        markdown(raw, date)
    except Exception as e:
        print(e)

def csvfile(arr: List[str], date):
    if not os.path.isfile(f"{date}.csv"):
        with open(f"{date}.csv","w",newline='', encoding='utf-8') as file:
            obj = csv.writer(file)
            for i in range(len(arr)):
                obj.writerow([n for n in arr[i]])

def markdown(arr: list, date):
    mdFile = MdUtils(file_name=date, title=date)
    temp = []
    for line in arr:
        for n in line:
            temp.append(n)
    mdFile.new_table(columns=7, rows=101, text=temp, text_align='center')
    mdFile.create_md_file()


def check() -> List[str]:
    d = str(input("what is the date of that Sunday?"))
    parent_dir = os.path.expanduser('~/Documents/apple-music-replay/replay/replay21')
    path = os.path.join(parent_dir, d)
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Already has directory")
    finally:
        return [path, d]

def time(l:List)-> List:
    return [str(datetime.timedelta(seconds=int(l[0])))]
