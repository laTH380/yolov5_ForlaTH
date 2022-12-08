#データセットのラベルミスを一括で治したい人生だった

import glob
import re
import os

dir = "/data/train/labels"
#ファイルを順に読み込み
path_list = glob.glob( dir + "/*.txt")
#一行ずつ読み込み,書き込み
for i in path_list:
    contents = []
    with open("yolov5_ForTamaki/data/train/labels/egg_45_jpg.rf.fcf108e3f89512e9bcb0798fe728b83f.txt") as f:
        for line in f:
            print(line)#????行ごとになぜか開かない！！！！
            line = "8" + line
            print(line)
            contents.append(line)
    # with open(i, mode = "w") as f:
    #     for content in contents:
    #         f.write(content)