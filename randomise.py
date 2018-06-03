#run with command argument "--test" to run without launching video program

import os;
import sys;
import re;
import random;
import datetime;

# -- settable variables --
#there's no error checking!!! make sure directories exist
_log=1; #1 to make log file, 0 to not
_loadDir="./vids"; #directory to launch vids from (make sure theres no slash at the end)

_promptMove=1; #whether to prompt to move the chosen video
_moveDir="./completed"; #folder to move to

class vidArray:
    def __init__(self):
        self.vids=set();
        self.files=set();

    def add(self,vid,filename):
        if vid not in self.vids:
            self.vids.add(vid);
            self.files.add(filename);

    #print filenames of loaded vids
    def printVids(self):
        for x in self.vids:
            print(x);

    def pick(self):
        return random.choice(list(self.files));

def main():
    files=os.scandir(_loadDir);
    v=vidArray();
    thisFile=os.path.basename(__file__); #this files filename with extension
    logFile=os.path.splitext(thisFile)[0]+".log"; #log file name

    dircount=0;
    for x in files:
        if x.is_dir() or x.name==thisFile or x.name==logFile:
            continue;
        name=x.name;
        # cleanName=(re.sub("(\[([^\]]*)\])|(.mkv)|([^a-zA-z])|(.mp4)","",name)).lower();
        cleanName=(re.sub("(\..*$)|((\[|\().*?(\]|\)))|([^a-zA-Z])","",name)).lower();
        v.add(cleanName,name);
        dircount+=1;

    if dircount==0:
        print("folder was empty");
        os.system("pause");
        return;

    v.printVids();

    pick=v.pick();
    print(">{}".format(pick));

    if _log:
        logVid(pick,logFile);

    if len(sys.argv)>1 and sys.argv[1]=="--test":
        return;

    os.system('start "" "{}/{}"'.format(_loadDir,pick));

    if _promptMove:
        print("enter y to move video to {}, enter to cancel: ".format(_moveDir),end="");
        choice=input();

        if choice=="y":
            os.rename("{}/{}".format(_loadDir,pick),"{}/{}".format(_moveDir,pick));

    else:
        os.system("pause");

def logVid(filename,logFile):
    with open(logFile,"a+",encoding="utf8") as logfile:
        line="";
        logfile.seek(0);
        for x in logfile:
            line=x;

        newline="";
        if len(line)>0 and line[-1]!="\n":
            newline="\n";

        logfile.write("{}{} {}\n".format(newline,datetime.datetime.now().replace(microsecond=0),filename));

#supposed to be function that compares strings
#and gives some percent on their similarities,
#but not really useful and doesnt really work
def chanceWord(s):
    if len(s)==0:
        return 0;

    s=s.lower();
    letters=re.findall("[a-z ]",s);
    return len(letters)/len(s);

main();

