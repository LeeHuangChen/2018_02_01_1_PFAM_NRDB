import Configurations as conf
from cPickle import load
from src import util
import os


def nrbd_pfam():
    fastaSeqDict = load(open(conf.fastaSeqDictPath))

    util.generateDirectories(conf.outputFolder)
    nrbdFile = os.path.join(conf.outputFolder, conf.nrbdPFamOutputFile)
    open(nrbdFile, "w")

    with open(conf.nrbdFile, "r") as f:
        for i, line in enumerate(f):
            if len(line) > 0:
                pid = line.split(":")[0].strip()
                # print pid
                if len(pid) > 0:
                    seq = fastaSeqDict[pid]
                    # print seq
                    fastaOut = util.toFASTA(pid, seq)
                    # print type(fastaOut)
                    with open(nrbdFile, "a") as ff:
                        ff.write(fastaOut)



def main():
    nrbd_pfam()


if __name__ == '__main__':
    main()
