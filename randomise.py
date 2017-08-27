#run with command argument test to run without launching video program

import os;
import sys;
import re;
import random;

class vidArray:
    def __init__(self):
        self.vids=set();
        self.files=set();

    def add(self,vid,filename):
        if (vid=="randomisepy"):
            return;
        if vid not in self.vids:
            self.vids.add(vid);
            self.files.add(filename);

    def write(self):
        outfile=open("vidlist.txt","w");
        for x in self.vids:
            outfile.write(x);

    def printVids(self):
        for x in self.vids:
            print(x);

    def pick(self):
        return random.choice(list(self.files));

def main():
    files=os.scandir();
    v=vidArray();

    for x in files:
        if x.is_dir() or x.name=="randomise.py":
            continue;
        name=x.name;
        # cleanName=(re.sub("(\[([^\]]*)\])|(.mkv)|([^a-zA-z])|(.mp4)","",name)).lower();
        cleanName=(re.sub("(\..*$)|((\[|\().*?(\]|\)))|([^a-zA-Z])","",name)).lower();
        v.add(cleanName,name);

    v.printVids();

    pick=v.pick();
    print(">{}".format(pick));

    if len(sys.argv)>1 and sys.argv[1]=="test":
        return;

    os.system('start "" "{}" & pause'.format(pick));

def chanceWord(s):
    if len(s)==0:
        return 0;

    s=s.lower();
    letters=re.findall("[a-z ]",s);
    return len(letters)/len(s);

main();

