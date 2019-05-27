# author:- Bhavana Saraswat M.Tech Banasthali University 2016-2017
import sqlite3
import re
import sys
import os
conn = sqlite3.connect("Treebank.db")
print ('Opened database successfully');
s=""
s1=''
list1=[]
i=0
files=sys.argv[1]
for name in os.listdir(files):
	path=os.path.realpath(files)
	path=path+"/"+name
	with open(path) as f:
		for line in f:
			if '<Sentence id=' in  line:
				a=re.findall('\d+',line)
				print("\n")
				print(a)
				sid=[int(x) for x in a];
			if 'af' in line: 
				line = line.strip()
				if line!="":
					line=line.split("\t")
					colnum=len(line)
				if colnum>1:
					s+=str(line[1]+" ")
			if '</Sentence' in line:
				print(name)
				i=i+1
				list1.extend((sid,s,name,i))
				print(list1)
				conn.execute('INSERT INTO Tsentence(SNo,sid,sentence,filename) VALUES(?,?,?,?)',(list1[3],list1[0][0],list1[1],list1[2]))
				conn.commit()
				s=""
				list1=[ ]
conn.close()
f.close()
