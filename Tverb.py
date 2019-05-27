#author:- Bhavana Saraswat M.tech Banasthali University 2016-2017
import sqlite3
i=0
list1=[]
s=''
s1=''
conn = sqlite3.connect('Treebank.db')
print ('Opened database successfully');
cursor=conn.execute("select sid,fragment,wrelation,filename,rchunkid,category,chunkid,wordid,root,word from Tword")
for row in cursor:
	if row[1]=='pof':
		pof='True'
		s1=str(row[9]+" "+row[2])
		cursor1=conn.execute("select sid,chunkid,wordid,root,category,filename from Tword where sid=? and filename=? and name=?",(row[0],row[3],row[2]))
		for row1 in cursor1:
			s=str(row[9]+" "+row1[3])
			if row1[4]=='v':
				i=i+1
				list1.extend((i,row1[0],row1[1],row1[2],row1[3],s,s1,pof,row1[4],row1[1],row1[5]))
				print(list1)
				conn.execute('INSERT INTO temp(SNo,sid,chunkid,wordid,verb,wverb,word_verb,pof,category,rchunkid,filename) values(?,?,?,?,?,?,?,?,?,?,?)',(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10]))
				conn.commit()
				list1=[]
				s=""
conn.close()
