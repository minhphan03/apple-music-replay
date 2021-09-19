# using offline itunes to generate and update Apple Music Replay playlists
# data, then upload files to GitHub
import os
import datetime
import csv
from mdutils.mdutils import MdUtils
from git import Repo
import git
#csv and markdown files
def main():
    try:
        with open('C:\\Users\\User\\Downloads\\Replay 2021.txt', 'r', encoding='utf-16') as file:
            raw = file.read().split('\n')[:101]

        raw[0] = raw[0].split('\t')[:2] + raw[0].split('\t')[3:4]
        raw[0].insert(0, 'Position')
        for i in range(1, len(raw)):
            raw[i] = raw[i].split('\t')[:2]+raw[i].split('\t')[3:4]
            raw[i].insert(0, i)

        # for i in raw:
        #     print(i[0], i[1], i[2], i[3])
        #os.remove('C:\\Users\\User\\Downloads\\Replay 2021.txt')
        [path, date] = check()
        os.chdir(path)
        #print(*raw, sep='\n')
        csvfile(raw, date)
        markdown(raw, date)
        push(date)
    except Exception as e:
        print(e)

def csvfile(arr: list[str], date):
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
    mdFile.new_table(columns=4, rows=101, text=temp, text_align='center')
    mdFile.create_md_file()

def check()->list[str, str]:
    dir = str(input("what is the date of that Sunday?"))
    parent_dir = r"C:/Users/User/PycharmProjects/AppleMusicReplay/replay/replay21"
    path = os.path.join(parent_dir,dir)
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Already has directory")
    finally:
        return [path, dir]

if __name__ == "__main__":
    main()