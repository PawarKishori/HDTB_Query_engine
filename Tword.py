# author:- Bhavana Saraswat M.Tech Banasthali University 2016-2017
import re
import sqlite3
import sys
import os
s2=''
sid1=0
i=443303                                                             
list1=[ ]
list2=[0,0 ]
list3=[0,0 ]
list4=[ ]
sid2=0
rchunkid=0
connection=0
index=0
n=[]
conn = sqlite3.connect('Treebank.db')
print ('Opened database successfully');
files = sys.argv[1]
path1=sys.argv[2]
s=os.path.realpath(path1)
for name in os.listdir(files):
    path=os.path.realpath(files)
    path=path+"/"+name
    print (name)
    with open(path) as f:
         for line in f:
             if '<Sentence id=' in  line:    
                 a=re.findall('\d+',line)
                 print("\n")
                 sid=[int(x) for x in a];
                 #print(sid)   
             elif not '<Sentence id='  in line:
                 if not '</Sentence' in line:
                    line=line.strip()
                    if line!="":
                       line=line.split("\t")
                       colnum=len(line)
                       w=line[1]
                       #print(w)
                       t=line[2]
                       #print(t)
                       if 'af' in line[3]:
                          m=re.search("af=\'(.*?)\'",line[3])
                          list2=m.group(1)
                          list2=list2.split(",")
                          for index in range(len(list2)):
                              if list2[index]=='':
                                 list2[index]='NULL'
                                 #print(list2)
                       if 'name' in line[3]:
                          m1=re.search("name=\'(.*?)\'",line[3])
                          M1=m1.group(1)
                          #print(M1)
                       else:
                          M1='NULL'
                          #print(M1)
                       if 'drel' in line[3]:
                          m2=re.search("drel=\'(.*?)\'",line[3])
                          list3=m2.group(1)
                          #print(list3)
                          list3=list3.split(":")
                          #print(list3)
                          if list3[0]=='k1' or list3[0]=='k2'or list3[0]=='k3' or list3[0]=='k4'or list3[0]=='k5' or list3[0]=='k7' or list3[0]=='k7t' or list3[0]=='k7p' or list3[0]=='k1u' or list3[0]=='k1s' or list3[0]=='k2u' or list3[0]=='k2s' or list3[0]=='k2p'or list2[0]=='k2g' or list3[0]=='k2a' or list3[0]=='k7a' or list3[0]=='k7u'or list3[0]=='k4a':
                             karak=list3[0]
                             #print(karak)
                          else:
                             karak='NULL'
                             #print(karak)
                          if list3[0]=='jjmod' or list3[0]=='nmod' or list3[0]=='vmod' or list3[0]=='rbmod' or list3[0]=='mod':
                             modifier=list3[0]
                             #print(modifier)
                          else:
                             modifier='NULL'
                             #print(modifier)
                          if list3[0]=='fragof' or list3[0]=='pof' or list3[0]=='ccof':
                             fragment=list3[0]
                             #print(fragment) 
                          else:
                             fragment='NULL'
                             #print(fragment)
                          if list3[0]=='rsym':
                             symbol=list3[0]
                             #print(symbol)
                          else:
                             symbol='NULL'
                             #print(synbol)
                          if list3[0]=='ras-k1' or list3[0]=='ras-k2' or list3[0]=='ras-r6-k2'or list3[0]=='ras-pof' or list3[0]=='ras-k4a' or list3[0]=='ras-k4' or list3[0]=='ras-k7'or list3[0]=='ras-NEG' or list3[0]=='ras-rt':
                             saha=list3[0]
                             #print(saha)
                          else:
                             saha='NULL'
                             #print(saha)
                          if list3[0]=='r6' or list3[0]=='r6-k1'or list3[0]=='r6-k2':
                             shashthi=list3[0]
                             #print(shashthi)
                          else:
                             shashthi='NULL'
                             #print(shashthi)
                          if list3[0]=='adv'or  list3[0]=='sent-adv':
                             adverbs=list3[0]
                             #print(adverbs)
                          else:
                             adverbs='NULL'
                             #print(adverbs)
                          if list3[0]=='jk1' or list3[0]=='pk1':
                             cause=list3[0]
                             #print(cause) 
                          else:
                             cause='NULL'
                             #print(cause)
                          if list3[0]=='rh' or list3[0]=='rsp' or list3[0]=='rd' or list3[0]=='rt' or list3[0]=='rs' or list3[0]=='rad' or list3[0]=='main' or list3[0]=='undef':
                             relation=list3[0]
                             #print(relation)
                          else:
                             relation='NULL'
                             #print(relation)
                          if list3[0]=='lwg__vaux_cont' or list3[0]=='lwg__neg' or list3[0]=='pof__redup' or list3[0]=='nmod__adj' or list3[0]=='pof__cn' or list3[0]=='lwg__psp' or list3[0]=='lwg__vaux' or list3[0]=='lwg__vaux__cont' or list3[0]=='lwg__rp' or list3[0]=='pof__inv' or list3[0]=='nmod__pofinv' or list3[0]=='rbmod__relc' or list3[0]=='nmod__emph' or  list3[0]=='spr' or list3[0]=='nmod__relc' or list3[0]=='spn' or list3[0]=='nmod__k2inv' or list3[0]=='nmod__k1inv':
                             other=list3[0]
                             #print(other)
                          else:
                             other='NULL'
                             #print(other)				
                          with open('karak.dat','r') as f1:
                               for line1 in f1:
                                   if re.match("^"+re.escape(list3[0])+"\t" ,line1):
                                      line1=line1.split("\t")
                                      rname=line1[1]
                                      #print(list3[0]+" "+rname)                              
                                      #print(rname)
                          wrelation=list3[1]
                       else:
                          karak='NULL'
                          modifier='NULL'
                          fragment='NULL'
                          symbol='NULL'
                          shashthi='NULL'
                          saha='NULL'
                          adverbs='NULL'
                          cause='NULL'
                          relation='NULL'
                          other='NULL'
                          rname='NULL'
                          wrelation='NULL'
                          rchunkid='NULL'
                          connection='main'
                          #print(karak+","+modifier+","+fragment+","+symbol+","+shashthi+","+saha+","+adverbs+","+cause+","+relation+","+other+","+rname+","+wrelation+","+rchunkid+","+connection)
                       if 'chunkType' in line[3]:
                          m4=re.search("chunkType=\'(.*?)\'",line[3])
                          list4=m4.group(1)                         
                          #print(list4)
                          list4=list4.split(":")
                          #print(list4)
                          s2=str(s+"/"+name)
                          #print(s2)
                          with open(s2,'r') as f2: 
                               for line2 in f2:	
                                   if '<Sentence id=' in line2:
                                      b=re.findall('\d+',line2)
                                      sid1=[int(x1) for x1 in b];
                                      #print(sid1)
                                      if sid==sid1:
                                         n.extend((sid,name))
                                         cursor=conn.execute("select chunkid,chunkname from Tchunk where sid=? and filename=?;",(n[0][0],n[1]))
                                         n=[] 
                                         for row in cursor:
                                             if row[1]==list4[1]:
                                                chunkid=row[0]
                                                #print(chunkid)
                                   if 'af' in line2:
                                      line2 = line2.strip()
                                      if line2!="":
                                         line2=line2.split("\t")
                                         if sid==sid1:
                                            if 'name' in line2[3]:
                                               n1=re.search("name=\'(.*?)\'",line2[3])
                                               N1=n1.group(1)
                                               if M1==N1:
                                                  if line2[1]==w:
                                                     wordid=line2[0]
                                                     #print(wordid)
                                               if N1==wrelation:
                                                  connection=line2[0] 
                                                  rw=line2[0].split(".")
                                                  rchunkid=rw[0]
                                                  #print(connection)
                                                  #print(rchunkid)
                       else:
                          list4[0]='NULL'
                          list4[1]='NULL'
                          #print(list4,end=" ")
                       if 'vpos' in line[3]:
                          m3=re.search("vpos=\'(.*?)\'",line[3])
                          M3=m3.group(1)
                          #print(M3,end=" ")
                       else:
                          M3='NULL'
                       if 'posn' in line[3]:
                          m5=re.search("posn=\'(.*?)\'",line[3])
                          M5=m5.group(1)
                          #print(M5)
                       else:
                          M5='NULL' 
                          #print(M5)                                       
                       i=i+1
                       list1.extend((i,sid,chunkid,wordid,w,t,list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,wrelation,rchunkid,M3,M1,list4[0],list4[1],M5,connection,name))
                       print(list1)
                       conn.execute('INSERT INTO Tword(SNo,sid,chunkid,wordid,word,postag,root,category,gender,number,person,wcase,vibhakti,tam,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,wrelation,rchunkid,vpos, name,treeposition,chunkname,position,connection,filename) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(list1[0],list1[1][0],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10],list1[11],list1[12],list1[13],list1[14],list1[15],list1[16],list1[17],list1[18],list1[19],list1[20],list1[21],list1[22],list1[23],list1[24],list1[25],list1[26],list1[27],list1[28],list1[29],list1[30],list1[31],list1[32],list1[33]))
                       conn.commit()
                       list3=[ ]
                       list1=[ ]
                       list4=[ ]
                       list2=[ ]
                       a=0
                       b=0
                       e=0		
                       s2=''		
conn.close()
#f2.close()
#f.close()
