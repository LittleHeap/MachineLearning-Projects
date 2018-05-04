import operator

import jieba.posseg

read = open('140000.TRAIN', 'r', encoding='gbk', errors='ignore')

data = read.read()

rows = data.split('\n')

alldic = set()

allwords = ''

for row in rows:
    segs = jieba.posseg.cut(row)
    for seg in segs:
        alldic.add(seg.word)

print(len(alldic))  # >>>78444

# 写入文件
write = open("140000_words.TRAIN", "w")

for word in alldic:
    allwords = allwords + '\n' + word

write.write(allwords)

read.close()

write.close()
