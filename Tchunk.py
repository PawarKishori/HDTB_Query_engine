#author:- Bhavana Saraswat M.Tech Banasthali University 2016-2017
import sqlite3
import re
import sys
import os
conn = sqlite3.connect('Treebank.db')
print ('Opened database successfully');
s=""
s1=''
list1=[]
list2=[0,0 ]
list3=[0,0 ]
i=0   
files =sys.argv[1]                                                                
for name in os.listdir(files):
    path=os.path.realpath(files)
    path=path+"/"+name 
    with open(path) as f:
         for line in f:
                if '<Sentence id=' in  line:
                        a=re.findall('\d+',line)
                        print("\n")
                if '((' in line:
                        line = line.strip()
                        if line!="":
                                line=line.split("\t")
                                colnum=len(line)
                                print(a, end=" ")
                                print(line[0], end=" ")
                                chid=line[0]
                                print(line[1], end=" ")
                                print(line[2], end=" ")
                                ctype=line[2]
                                print(line[3], end=" ")
                                if 'name' in line[3]:
                                        m=re.search("name=\'(.*?)\'",line[3])
                                        #print(m.group(1))
                                        M=m.group(1)
                                else:
                                        M='NULL'
                                if 'drel' in line[3]:
                                        m1=re.search("drel=\'(.*?)\'",line[3])
                                        list2=m1.group(1)
                                        list2=list2.split(":")
                                        #print(list2)
                                else:
                                        list2[0]='NULL'
                                        list2[1]='NULL'
                                if 'stype' in line[3]:
                                        m2=re.search("stype=\'(.*?)\'",line[3])
                                        #print(m2.group(1))
                                        M2=m2.group(1)
                                else:
                                        M2='NULL'
                                if 'voicetype' in line[3]:
                                        m3=re.search("voicetype=\'(.*?)\'",line[3])
                                        #print(m3.group(1))
                                        M3=m3.group(1)
                                else:
                                        M3='NULL'
                                if 'mtype' in line[3]:
                                        m4=re.search("mtype=\'(.*?)\'",line[3])
                                        #print(m4.group(1))
                                        M4=m4.group(1)
                                else:
                                        M4='NULL'
                                if 'dmrel' in line[3]:
                                        m5=re.search("dmrel=\'(.*?)\'",line[3])
                                        list3=m5.group(1)
                                        list3=list3.split(":")
                                        #print(list3)
                                else:
                                        list3[0]='NULL'
                                        list3[1]='NULL'
                                if 'troot' in line[3]:
                                        m6=re.search("troot=\'(.*?)\'",line[3])
                                        #print(m6.group(1))
                                        M6=m6.group(1)
                                else:
                                        M6='NULL'
                                if 'coref' in line[3]:
                                        m7=re.search("coref=\'(.*?)\'",line[3])
                                        #print(m7.group(1))
                                        M7=m7.group(1)
                                else:
                                        M7='NULL'
                                if 'comment' in line[3]:
                                        m8=re.search("comment=\'(.*?)\'",line[3])
                                        #print(m7.group(1))
                                        M8=m8.group(1)
                                else:
                                        M8='NULL'
                if 'af=' in line:
                        line = line.strip()
                        if line!="":
                                line=line.split("\t")
                                colnum=len(line)
                                print(line[1], end=" ")
                                s+=str(line[1]+" ")
                if '))' in line:
                        #print("\n")
                        print(name)
                        i=i+1
                        print(i)
                        list1.extend((i,a,chid,ctype,M,list2[0],list2[1],M2,M3,M4,list3[0],list3[1],M6,M7,M8,name,s))
                        conn.execute('INSERT INTO Tchunk(SNo,sid,chunkid,chunktype,chunkname,chunkrel,relwith,stype,voicetype,mtype,dmrel,dmrelwith,troot,coref,comment,filename,words) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(list1[0],list1[1][0],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10],list1[11],list1[12],list1[13],list1[14],list1[15],list1[16]))
                        conn.commit()
                        s=""
                        list1=[ ]
                        list2=[0,0]
                        list3=[0,0]
conn.close()
f.close()
