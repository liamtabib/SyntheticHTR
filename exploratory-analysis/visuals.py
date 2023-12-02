import numpy as np
import pandas as pd
import torch
import json

#our_model = torch.load("/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/model/OurModel_model/models/ckpt.pt")

t = open("/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/job_scripts/writers_dict_train.json")
styles = json.load(t)
styles["135"]
a = list(styles.keys())
a.sort()
print(a)
len(a)
#!pip install matplotlib
import os
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as img

from PIL import Image

iam_cl_path = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/datasets/IAM_cleaned"

iam_gen_path = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/synthetic_datasets/IAM_full/images"

filelist = os.listdir(iam_cl_path)

clean_endings=[]
for f in filelist:
    if f.endswith(".png"):
        clean_endings.append(f)

clean_endings.sort()
print(clean_endings[0:3])


filelist2 = os.listdir(iam_gen_path)

gen_endings=[]
for f in filelist2:
    if f.endswith(".png"):
        gen_endings.append(f)

gen_endings.sort()
print(gen_endings[0:3])

clean = []; gen = []

# clean=np.empty((256,64,3, len(clean_endings)))
# clean[clean!="a"]=0
#print(clean.shape, clean.sum())


for end in clean_endings:
    im = np.array( Image.open(iam_cl_path+"/"+end) )
    clean.append(im)

for end in gen_endings:
    im = np.array( Image.open(iam_gen_path+"/"+end) )
    gen.append(im)
for i in range(10):
    cl_ind = clean_endings.index( gen_endings[i] )
    plt.subplot(1, 2, 1)
    plt.imshow(clean[cl_ind][:,:,0], cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(gen[i], cmap="gray")
    plt.show()
clean_endings.index(clean_endings[100])
clean[100].shape, gen[100].shape
i=1000
(clean[i][:,:,0] == clean[i][:,:,1]).all(), (clean[i][:,:,0] == clean[i][:,:,2]).all()
i=100
cl_ind = clean_endings.index( gen_endings[i] )
a = clean[cl_ind][:,:,0].astype("float"); b = gen[i].astype("float")
plt.imshow(a, cmap="gray")
plt.show()
plt.imshow(b, cmap="gray")
plt.show()

c = a-b
plt.imshow(c, cmap="gray")
plt.show()
c[0,0], a[0,0], b[0,0]
np.sum(np.abs(c))/c.size, np.sqrt(np.sum(c**2))/c.size
errs = []
for i in range(len(gen_endings)):
    cl_ind = clean_endings.index( gen_endings[i] )
    a = clean[cl_ind][:,:,0].astype("float"); b = gen[i].astype("float")
    c = a-b
    errs.append(np.sum(np.abs(c))/c.size)
plt.hist(errs, bins=50)
plt.xlim([0,255])
plt.show()
good=[]; bad=[]
i=0
while len(good)<5:
    cl_ind = clean_endings.index( gen_endings[i] )
    a = clean[cl_ind][:,:,0].astype("float"); b = gen[i].astype("float")
    c = a-b
    if np.sum(np.abs(c))/c.size < 10:
        good.append(i)
    
    i += 1

i=0
while len(bad)<4:
    cl_ind = clean_endings.index( gen_endings[i] )
    a = clean[cl_ind][:,:,0].astype("float"); b = gen[i].astype("float")
    c = a-b
    if np.sum(np.abs(c))/c.size > 60:
        bad.append(i)
    i += 1
good, bad, good+bad
print("GOOD:")
c=0
for i in good+bad:
    if c==5:
        print("BAD:")
    cl_ind = clean_endings.index( gen_endings[i] )
    plt.subplot(1, 2, 1)
    plt.imshow(clean[cl_ind][:,:,0], cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(gen[i], cmap="gray")
    plt.show()
    print( np.sum(np.abs(clean[cl_ind][:,:,0].astype("float")-gen[i].astype("float")))/gen[i].size )
    c+=1

voc_path = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/datasets/IAM_vocabulary.txt"

with open(voc_path, "r") as vf:
    words = [ line[0:len(line)-1] for line in vf ]
words[0:3], words[-3:], len(words)
voc = list(set(words))
len(words), len(voc)
words.count("Olimpia")
### in-Vocabulary: frequency-L1 score
file_path = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/datasets/IAM_gt/batch_0.filter27"
with open(file_path, "r") as file:
    s = file.readlines()
    print(s)
iam_gt = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/datasets/IAM_cleaned/"
iam_gn = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/synthetic_datasets/IAM_full/images/"

freq=[]; score=[]

for e in s:
    e = e.replace("\n", "")
    e = e.split(",")[1]
    e = e.split()
    
    a = np.array( Image.open(iam_gt + e[0] + ".png") )[:,:,0].astype("float")
    b = np.array( Image.open(iam_gn + e[0] + ".png") ).astype("float")
    freq.append( words.count(e[1]) )
    score.append( np.sum(np.abs(a-b))/a.size )

sc = []
for f in freq:
    temp=[]
    for i in range(len(freq)):
        if freq[i]==f:
            temp.append(score[i])
    sc.append( np.mean(temp) )

plt.figure(figsize=(15,10))
plt.scatter(freq, score)
plt.scatter(freq, sc, c="red")
plt.xlabel("frequency")
plt.ylabel("L1-score")
plt.xlim([0,500])
plt.show()
plt.hist(score, bins=50)
plt.show()
### Out-of-Vovabulary
others = pd.read_csv("https://raw.githubusercontent.com/filiph/english_words/master/data/word-freq-top5000.csv")
others = others["Word"]
others.head()
word_dict={}

for i in range(others.shape[0]):
    w = others[i]
    if w not in word_dict:
        word_dict[w] = words.count(w)
word_dict
import json

json.dump( word_dict, open( "word_dict.json", 'w' ) )
wd = json.load( open( "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/word_dict.json" ) )
type(wd)
wd["stars"]
for e in wd.keys():
    print(e, wd[e])
    break

from string import punctuation as punc
oov = []
for e in wd.keys():
    if wd[e] == 0:
        if (e not in oov) and not any(p in e for p in punc):
            oov.append(e)
from string import punctuation as punc

print(punc)

punc 
len(oov), oov[0:5]
l3 = []

for i in range(len(oov)):
    if len(oov[i]) == 3:
        l3.append(oov[i])
len(l3), l3
"labor" in oov
wd["labor"]
v = list(word_dict.values())
v.count(0)
lengths = [ len(e) for e in oov ]
lengths.count(8)

