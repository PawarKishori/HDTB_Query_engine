# author:- Bhavana Saraswat M.Tech Banastahli University 2016-2017
import sqlite3
conn = sqlite3.connect('bhavana.db')
print ('Opened database successfully');
conn.execute('CREATE TABLE Tsentence (SNo INTEGER AUTO INCREMENT, sid INT (10), sentence text, filename VARCHAR (100),PRIMARY KEY (SNo,sid, filename));')
print ('Tsentence created successfuly')
conn.execute('CREATE TABLE Tchunk(SNo int(10),sid int(10),chunkid int (10),chunktype text, chunkname varchar(100),chunkrel text,relwith text,stype text,voicetype text,mtype text,dmrel text, dmrelwith text, troot text,coref text, filename varchar(100), words text, primary key(SNo,sid,chunkid,chunkname), foreign key(filename) references Tsentence(filename));')
print ('Tchunk created successfuly')
conn.execute('CREATE TABLE Tword(SNo int(10),sid int(10),chunkid int (10), wordid decimal(3,1),word varchar(100), postag text,root text, category text, gender text, number text,person text, wcase text,tam text,vibhakti text,karak text, modifier text, fragment text,symbol text,saha text,shashthi text, adverbs text,cause text,relation text,other text,rname text, wrelation text, rchunkid int(10),vpos text, name text,treeposition text,chunkname varchar(100),position text,connection text, filename varchar(100), primary key(SNo,sid,chunkid,wordid),foreign key(chunkid,chunkname) references Tchunk(chunkid,chunkname), foreign key(sid,filename) references Tsentence(sid,filename));')
print ('Tword created successfuly')
conn.execute('CREATE TABLE Tverb(SNo int(10),sid int(10), chunkid int(10),wordid decimal(3,2),verb text,wverb text, pof text, category text,rchunkid int(10),filename text,primary key(SNo,sid,wordid,chunkid,filename),foreign key(chunkid) references Tword(chunkid),foreign key(chunkid) references Tchunk(chunkid),foreign key(sid) references Tsentence(chunkid));')
print ('Tverb created successfuly')
conn.close()
