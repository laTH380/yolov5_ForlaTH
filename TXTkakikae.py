import glob
import re
import os

dir = "/data/train/labels"
#ファイルを順に読み込み
path_list = glob.glob( dir + "/*.txt")
#一行ずつ読み込み,書き込み
for i in path_list:
    contents = []
    with open("/data/train/labels\egg_32_jpg.rf.339a0a7c21df0b18f8182922f9395efd.txt") as f:
        for line in f:
            print(line)
            line = "8" + line
            print(line)
            contents.append(line)
    # with open(i, mode = "w") as f:
    #     for content in contents:
    #         f.write(content)