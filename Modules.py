import sqlite3
import re
import sys
import os
import getpass
#conn=sqlite3.connect('/home/raudra/Treebank/Treebank.db')
conn=sqlite3.connect('/mnt/PhD/Treebank_query_engine/Treebank.db')
print ('Opened database successfully')
def vibh(vibhakti):
	flag=0
	flag1=0
	total=0
	p=0 
	d=0 
	i=0
	k=''
	l=[]
	l1=[]
	name=input('Enter name of output file: ')
	#name='Vibhakti_'
	#name+=str(vibhakti)
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	c="SNo\t\tKarak\t\tOccurance\tPercentage\tCumalative\tName\n"
	f.write(c)
	c=''
	s='0_'
	s+=vibhakti
	#cho=input('Do you want to see output for '+ vibhakti+' and '+s+' both or for single '+vibhakti+' only?(Press "b" for both and "s" for single) ')
	#if cho=='b':
	cursor=conn.execute('select karak,rname,count(*) from Tword where vibhakti=? or vibhakti=? and karak!="NULL" and rname!="NULL" group by karak',(vibhakti,c))
	cu=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and karak!="NULL" and rname!="NULL" group by karak)',(vibhakti,c))
	cursor1=conn.execute('select saha,rname,count(*) from Tword where vibhakti=? or vibhakti=? and saha!="NULL" and rname!="NULL" group by saha',(vibhakti,c))
	cu1=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and saha!="NULL" and rname!="NULL" group by saha)',(vibhakti,c))
	cursor2=conn.execute('select cause,rname,count(*) from Tword where vibhakti=?  or vibhakti=? and cause!="NULL" and rname!="NULL" group by cause',(vibhakti,c))
	cu2=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and cause!="NULL" and rname!="NULL" group by cause)',(vibhakti,c))
	cursor3=conn.execute('select modifier,rname,count(*) from Tword where vibhakti=? or vibhakti=? and modifier!="NULL" and rname!="NULL" group by modifier',(vibhakti,c))
	cu3=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and modifier!="NULL" and rname!="NULL" group by modifier)',(vibhakti,c))
	cursor4=conn.execute('select shashthi,rname,count(*) from Tword where vibhakti=? or vibhakti=? and shashthi!="NULL" and rname!="NULL" group by shashthi',(vibhakti,c))
	cu4=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and shashthi!="NULL" and rname!="NULL" group by shashthi)',(vibhakti,c))
	cursor5=conn.execute('select adverbs,rname,count(*) from Tword where vibhakti=? or vibhakti=? and adverbs!="NULL" and rname!="NULL" group by adverbs',(vibhakti,c))
	cu5=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and adverbs!="NULL" and rname!="NULL" group by adverbs)',(vibhakti,c))
	cursor6=conn.execute('select relation,rname,count(*) from Tword where vibhakti=? or vibhakti=? and relation!="NULL" and rname!="NULL" group by relation',(vibhakti,c))
	cu6=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=?  or vibhakti=? and relation!="NULL" and rname!="NULL" group by relation)',(vibhakti,c))
	cursor7=conn.execute('select other,rname,count(*) from Tword where vibhakti=? or vibhakti=? and other!="NULL" and rname!="NULL" group by other',(vibhakti,c))
	cu7=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=?  and other!="NULL" and rname!="NULL" group by other)',(vibhakti,c))
	cursor17=conn.execute('select other,rname,count(*) from Tword where vibhakti=? or vibhakti=? and fragment!="NULL" and rname!="NULL" group by fragment',(vibhakti,c))
	cu17=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? or vibhakti=? and fragment!="NULL" and rname!="NULL" group by fragment)',(vibhakti,c))
	for row3 in cu:
		c1=row3[0]
	for row4 in cu1:
		c2=row4[0]
	for row5 in cu2:
		c3=row5[0]
	for row6 in cu3:
		c4=row6[0]
	for row7 in cu4:
		c5=row7[0]
	for row8 in cu5:
		c6=row8[0]
	for row9 in cu6:
		c7=row9[0]
	for row10 in cu7:
		c8=row10[0]
	for row11 in cu17:
		c9=row11[0]
	total=c1+c2+c3+c4+c5+c6+c7+c8+c9		
		#print(total)
	print("SNo\t\tKarak\t\tOccurance\tPercentage\tCumalative\tName")
	for row in cursor:
		flag=1
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row[0]+"\t\t",end="")
			#a=ro[2]+r11[2]
		print(row[2],end="")
		print("\t\t",end="")
		p=((row[2]/total)*100)
		d=d+p	
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row[1])
		c=str(i)
		c+=str("\t\t"+row[0]+"\t\t")
		c+=str(row[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row[1]+"\n")
		f.write(c)
		c=''
	for row1 in cursor1:
		flag=2
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row1[0]+"\t\t",end="")
		print(row1[2],end="")
		print("\t\t",end="")
		p=((row1[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row1[1])
		c=str(i)
		c+=str("\t\t"+row1[0]+"\t\t")
		c+=str(row1[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row1[1]+"\n")
		f.write(c)
		c=''
	for row2 in cursor2:
		flag=3
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row2[0]+"\t\t",end="")
		print(row2[2],end="")
		print("\t\t",end="")
		p=((row2[2]/total)*100)
		d=d+p
		print(round(p,2),end="")	
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row2[1])
		c=str(i)
		c+=str("\t\t"+row2[0]+"\t\t")
		c+=str(row2[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row2[1]+"\n")
		f.write(c)
		c=''
	for row11 in cursor3:
		flag=4
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row11[0]+"\t\t",end="")
		print(row11[2],end="")
		print("\t\t",end="")
		p=((row11[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row11[1])
		c=str(i)
		c+=str("\t\t"+row11[0]+"\t\t")
		c+=str(row11[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row11[1]+"\n")
		f.write(c)
		c=''
	for row12 in cursor4:
		flag=5
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row12[0]+"\t\t",end="")
		print(row12[2],end="")
		print("\t\t",end="")
		p=((row12[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row12[1])
		c=str(i)
		c+=str("\t\t"+row12[0]+"\t\t")
		c+=str(row12[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row12[1]+"\n")
		f.write(c)
		c=''
	for row13 in cursor5:
		flag=6
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row13[0]+"\t\t",end="")
		print(row13[2],end="")
		print("\t\t",end="")
		p=((row13[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row13[1])
		c=str(i)
		c+=str("\t\t"+row13[0]+"\t\t")
		c+=str(row13[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row13[1]+"\n")
		f.write(c)
		c=''
	for row14 in cursor6:
		flag=7
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row14[0]+"\t\t",end="")
		print(row14[2],end="")
		print("\t\t",end="")
		p=((row14[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row14[1])
		c=str(i)
		c+=str("\t\t"+row14[0]+"\t\t")
		c+=str(row14[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row14[1]+"\n")
		f.write(c)
		c=''
	for row15 in cursor7:
		flag=8
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row15[0]+"\t\t",end="")
		print(row15[2],end="")
		print("\t\t",end="")
		p=((row15[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row15[1])
		c=str(i)
		c+=str("\t\t"+row15[0]+"\t\t")
		c+=str(row15[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row15[1]+"\n")
		f.write(c)
		c=''
	for row16 in cursor17:
		flag=9
		i=i+1
		print(i,end="")
		print("\t\t",end="")
		print(row16[0]+"\t\t",end="")
		print(row16[2],end="")
		print("\t\t",end="")
		p=((row16[2]/total)*100)
		d=d+p
		print(round(p,2),end="")
		print("\t\t",end="")
		print(round(d,2),end="")
		print("\t\t"+row16[1])
		c=str(i)
		c+=str("\t\t"+row16[0]+"\t\t")
		c+=str(row16[2])
		c+=str("\t")
		c+=str(round(p,2))
		c+=("\t\t")
		c+=str(round(d,2))
		c+=str("\t\t"+row16[1]+"\n")
		f.write(c)
		c=''
	'''elif cho=='s':
		cursor18=conn.execute('select karak,rname,count(*) from Tword where vibhakti=? and karak!="NULL" group by karak',(vibhakti,))
		cu18=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and karak!="NULL" group by karak)',(vibhakti,))
		cursor19=conn.execute('select saha,rname,count(*) from Tword where vibhakti=? and saha!="NULL" group by saha',(vibhakti,))
		cu19=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and saha!="NULL" group by saha)',(vibhakti,))
		cursor20=conn.execute('select cause,rname,count(*) from Tword where vibhakti=? and cause!="NULL"group by cause',(vibhakti,))
		cu20=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and cause!="NULL" group by cause)',(vibhakti,))
		cursor21=conn.execute('select modifier,rname,count(*) from Tword where vibhakti=? and modifier!="NULL" group by modifier',(vibhakti,))
		cu21=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and modifier!="NULL" group by modifier)',(vibhakti,))
		cursor22=conn.execute('select shashthi,rname,count(*) from Tword where vibhakti=? and shashthi!="NULL" group by shashthi',(vibhakti,))
		cu22=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and shashthi!="NULL" group by shashthi)',(vibhakti,))
		cursor23=conn.execute('select adverbs,rname,count(*) from Tword where vibhakti=? and adverbs!="NULL" group by adverbs',(vibhakti,))
		cu23=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and adverbs!="NULL" group by adverbs)',(vibhakti,))
		cursor24=conn.execute('select relation,rname,count(*) from Tword where vibhakti=? and relation!="NULL" group by relation',(vibhakti,))
		cu24=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and relation!="NULL" group by relation)',(vibhakti,))
		cursor25=conn.execute('select other,rname,count(*) from Tword where vibhakti=? and other!="NULL" group by other',(vibhakti,))
		cu25=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=?  and other!="NULL" group by other)',(vibhakti,))
		cursor26=conn.execute('select other,rname,count(*) from Tword where vibhakti=? and fragment!="NULL" group by fragment',(vibhakti,))
		cu26=conn.execute('select total(occurance) from(select count(*) as occurance from Tword where vibhakti=? and fragment!="NULL" group by fragment)',(vibhakti,))
		for row3 in cu18:
			c1=row3[0]
		for row4 in cu19:
			c2=row4[0]
		for row5 in cu20:
			c3=row5[0]
		for row6 in cu21:
			c4=row6[0]
		for row7 in cu22:
			c5=row7[0]
		for row8 in cu23:
			c6=row8[0]
		for row9 in cu24:
			c7=row9[0]
		for row10 in cu25:
			c8=row10[0]
		for row11 in cu26:
			c9=row11[0]
		total=c1+c2+c3+c4+c5+c6+c7+c8+c9
		#print(total)
		print("SNo\t\tKarak\t\tOccurance\tPercentage\tCumalative\t\tName")
		for row in cursor18:
			flag1=1
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row[0]+"\t\t",end="")
			#a=ro[2]+r11[2]
			print(row[2],end="")
			print("\t\t",end="")
			p=((row[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row[1])
			c=str(i)
			c+=str("\t\t"+row[0]+"\t\t")
			c+=str(row[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row[1]+"\n")
			f.write(c)
			c=''
		for row1 in cursor19:
			flag1=2
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row1[0]+"\t\t",end="")
			print(row1[2],end="")
			print("\t\t",end="")
			p=((row1[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row1[1])
			c=str(i)
			c+=str("\t\t"+row1[0]+"\t\t")
			c+=str(row1[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row1[1]+"\n")
			f.write(c)
			c=''
		for row2 in cursor20:
			flag1=3
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row2[0]+"\t\t",end="")
			print(row2[2],end="")
			print("\t\t",end="")
			p=((row2[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row2[1])
			c=str(i)
			c+=str("\t\t"+row2[0]+"\t\t")
			c+=str(row2[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row2[1]+"\n")
			f.write(c)
			c=''
		for row11 in cursor21:
			flag1=4
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row11[0]+"\t\t",end="")
			print(row11[2],end="")
			print("\t\t",end="")
			p=((row11[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row11[1])
			c=str(i)
			c+=str("\t\t"+row11[0]+"\t\t")
			c+=str(row11[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row11[1]+"\n")
			f.write(c)
			c=''
		for row12 in cursor22:
			flag1=5
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row12[0]+"\t\t",end="")
			print(row12[2],end="")
			print("\t\t",end="")
			p=((row12[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row12[1])
			c=str(i)
			c+=str("\t\t"+row12[0]+"\t\t")
			c+=str(row12[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row12[1]+"\n")
			f.write(c)
			c=''
		for row13 in cursor23:
			flag1=6
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row13[0]+"\t\t",end="")
			print(row13[2],end="")
			print("\t\t",end="")
			p=((row13[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row13[1])
			c=str(i)
			c+=str("\t\t"+row13[0]+"\t\t")
			c+=str(row13[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row13[1]+"\n")
			f.write(c)
			c=''
		for row14 in cursor24:
			flag1=7
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row14[0]+"\t\t",end="")
			print(row14[2],end="")
			print("\t\t",end="")
			p=((row14[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row14[1])
			c=str(i)
			c+=str("\t\t"+row14[0]+"\t\t")
			c+=str(row14[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row14[1]+"\n")
			f.write(c)
			c=''
		for row15 in cursor25:
			flag1=8
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row15[0]+"\t\t",end="")
			print(row15[2],end="")
			print("\t\t",end="")
			p=((row15[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row15[1])
			c=str(i)
			c+=str("\t\t"+row15[0]+"\t\t")
			c+=str(row15[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row15[1]+"\n")
			f.write(c)
			c=''
		for row16 in cursor26:
			flag1=9
			i=i+1
			print(i,end="")
			print("\t\t",end="")
			print(row16[0]+"\t\t",end="")
			print(row16[2],end="")
			print("\t\t",end="")
			p=((row16[2]/total)*100)
			d=d+p
			print(round(p,2),end="")
			print("\t\t",end="")
			print(round(d,2),end="")
			print("\t\t"+row16[1])
			c=str(i)
			c+=str("\t\t"+row16[0]+"\t\t")
			c+=str(row16[2])
			c+=str("\t")
			c+=str(round(p,2))
			c+=("\t\t")
			c+=str(round(d,2))
			c+=str("\t\t"+row16[1]+"\n")
			f.write(c)
			c='''''
	if flag>0:
		choice=input("Do you want to see the sentences?(press 'y' for yes and 'n' for no) ")
		if choice=='y':
			k=input('Enter karak: ') 
			sentence(vibhakti,k);
	'''elif flag1>0:
		choice=input("Do you want to see the sentences?(press 'y' for yes and 'n' for no) ")
		if choice=='y':
			k=input('Enter karak: ')
			sentence1(vibhakti,k);'''
	if flag==0:
		print('No result found')
'''def sentence1(vibhakti,karak):
	flag=0
	i=0
	j=[]
	l=[]
	name=input('Enter name of output file: ')
	#name='Sentence_vibhakti'
	#name+=str(vibhakti+karak)
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	c="Sid\tOccurance\tFilename\t\t\t\tSentence\n"
	f.write(c)
	c=''
	cursor8=conn.execute('select vibhakti,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword')
	z=input("Do you want to see all sentences?(press 'y' for yes and 'n' for no) ")
	for row in cursor8:
		if vibhakti==row[0]:
			if karak==row[1]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.karak=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.karak=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]    
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[2]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.modifier=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.modifier=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[3]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.fragment=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.fragment=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[4]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.symbol=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.symbol=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[5]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.saha=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.saha=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[6]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.shashthi=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.shashthi=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[7]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.adverbs=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.adverbs=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
			elif karak==row[8]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.cause=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.cause=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)	
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)	
				break
			elif karak==row[9]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.relation=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.relation=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)		
				break
			elif karak==row[10]:
				if z=='n':
					m=input('How many sentences you want to see?(Enter number of sentences) ')
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.other=? and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,m))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				elif z=='y':
					print("SNo\tSid\t\tfilename\t\t\t\tSentence")
					cursor9=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.other=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
					for row1 in cursor9:
						flag=1
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row1[0],end="")
						print("\t\t",end="")
						print(row1[2],end="")
						print("\t\t"+row1[1]+"\n")
						c=str(i)
						c+=str("\t")
						c+=str(row1[0])
						c+=str("\t"+row1[2]+"\t\t"+row1[1]+"\n")
						f.write(c)
						c=''
						j=[]
						j.append(row1[0])
						j.append(row1[2])
						l.append(j)
				break
	if flag==0:
		print("No result found")
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			#na='Relation_Sentence_vibhakti_'
			#na+=str(vibhakti+karak)
			na=input('Enter name of output file: ')
			cho=input('Do you want to see relation between words of single sentence?(press y for yes and  n for no) ')
			if cho=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ') 
				relation1(na,si,fi)
			elif cho=='n':
				relation(na,j,l)
		ch=input("Do you want to see other karak also?(Press 'y' for yes and 'n' for no) ")
		if ch=='y':
			vibh(vibhakti)'''
def sentence(vibhakti,karak):
	flag=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	#name1=name
	name=input('Enter name of output file: ')
	#name='Sentence_vibhakti_and_0_vibhakti'
	#name+=str(vibhakti+karak)
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	c="Sid\tOccurance\tFilename\t\t\t\t\tSentence\n"
	f.write(c)
	c=''
	s='0_'
	s+=str(vibhakti)
	cursor8=conn.execute('select vibhakti,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword')
	z=input("Do you want to see all sentences?(press 'y' for yes and 'n' for no) ")
	for row in cursor8:
		if karak==row[1]:
			cursor19=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.karak=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			curso19=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.karak=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			for row1 in curso19:
				flag=1
				l3=[]
				l3.append(row1[0])
				l3.append(row1[1])
				l3.append(row1[2])
				l4.append(l3)
			for row11 in cursor19:
				flag=1
				l1=[]
				l1.append(row11[0])
				l1.append(row11[1])
				l1.append(row11[2])
				l2.append(l1)
			for l1 in l2:
				l4.append(l1) 
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l4[k][0],end="")
					print("\t\t",end="")
					print(l4[k][2],end="")
					print("\t\t"+str(l4[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l4[k][0])
					c+=str("\t"+l4[k][2]+"\t\t"+l4[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l4[k][0])
					j.append(l4[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l3 in l4:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l3[0],end="")
					print("\t\t",end="")
					print(l3[2],end="")
					print("\t\t"+l3[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l3[0])
					c+=str("\t"+l3[2]+"\t\t"+l3[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l3[0])
					j.append(l3[2])
					l.append(j)			
			break
		elif karak==row[2]:
			cursor20=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.modifier=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			curso20=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.modifier=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			for row2 in curso20:
				flag=1
				l1=[]
				l1.append(row2[0])
				l1.append(row2[1])
				l1.append(row2[2])
				l2.append(l1)
			for row12 in cursor20:
				flag=1
				l3=[]
				l3.append(row12[0])
				l3.append(row12[1])
				l3.append(row12[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[3]:
			cursor21=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.fragment=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso21=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.fragment=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row13 in cursor21:
				flag=1
				l1=[]
				l1.append(row13[0])
				l1.append(row13[1])
				l1.append(row13[2])
				l2.append(l1)
			for row3 in curso21:
				flag=1
				l3=[]
				l3.append(row3[0])
				l3.append(row3[1])
				l3.append(row3[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[4]:
			cursor22=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.symbol=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso22=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.symbol=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row14 in cursor22:
				flag=1
				l1=[]
				l1.append(row14[0])
				l1.append(row14[1])
				l1.append(row14[2])
				l2.append(l1)
			for row4 in curso22:
				flag=1
				l3=[]
				l3.append(row4[0])
				l3.append(row4[1])
				l3.append(row4[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)	
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[5]:
			cursor23=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.saha=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso23=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.saha=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row15 in cursor23:
				flag=1
				l1=[]
				l1.append(row15[0])
				l1.append(row15[1])
				l1.append(row15[2])
				l2.append(l1)
			for row5 in curso23:
				flag=1
				l3=[]
				l3.append(row5[0])
				l3.append(row5[1])
				l3.append(row5[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[6]:
			cursor24=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.shashthi=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso24=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.shashthi=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row16 in cursor24:
				flag=1
				l1=[]
				l1.append(row16[0])
				l1.append(row16[1])
				l1.append(row16[2])
				l2.append(l1)
			for row6 in curso24:
				flag=1
				l3=[]
				l3.append(row6[0])
				l3.append(row6[1])
				l3.append(row6[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[7]:
			cursor25=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.adverbs=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso25=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.adverbs=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row17 in cursor25:
				flag=1
				l1=[]
				l1.append(row17[0])
				l1.append(row17[1])
				l1.append(row17[2])
				l2.append(l1)
			for row7 in curso25:
				flag=1
				l3=[]
				l3.append(row7[0])
				l3.append(row7[1])
				l3.append(row7[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[8]:
			cursor26=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.cause=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso26=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.cause=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row18 in cursor26:
				flag=1
				l1=[]
				l1.append(row18[0])
				l1.append(row18[1])
				l1.append(row18[2])
				l2.append(l1)
			for row8 in curso26:
				flag=1
				l3=[]
				l3.append(row8[0])
				l3.append(row8[1])
				l3.append(row8[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		elif karak==row[9]:
			cursor27=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.relation=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso27=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.relation=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row19 in cursor27:
				flag=1
				l1=[]
				l1.append(row19[0])
				l1.append(row19[1])
				l1.append(row19[2])
				l2.append(l1)
			for row9 in curso27:
				flag=1
				l3=[]
				l3.append(row9[0])
				l3.append(row9[1])
				l3.append(row9[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
		if karak==row[10]:
			cursor28=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.other=? and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak))
			curso28=conn.execute('select distinct t1.sid,t1.sentence,t2.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.other=? and t1.sid==t2.sid and t1.filename==t2.filename',(s,karak))
			for row20 in cursor28:
				flag=1
				l1=[]
				l1.append(row20[0])
				l1.append(row20[1])
				l1.append(row20[2])
				l2.append(l1)
			for row10 in curso28:
				flag=1
				l3=[]
				l3.append(row10[0])
				l3.append(row10[1])
				l3.append(row10[2])
				l4.append(l3)
			for l3 in l4:
				l2.append(l3)
			k=0
			if z=='n':
				m=input('How many sentences you want to see?(Enter number of sentences) ')
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				while k<int(m):
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l2[k][0],end="")
					print("\t\t",end="")
					print(l2[k][2],end="")
					print("\t\t"+str(l2[k][1])+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l2[k][0])
					c+=str("\t"+l2[k][2]+"\t\t"+l2[k][1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l2[k][0])
					j.append(l2[k][2])
					l.append(j)
					k=k+1
			elif z=='y':
				print("SNo\tSid\t\tfilename\t\t\t\t\tSentence")
				i=0
				for l1 in l2:
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(l1[0],end="")
					print("\t\t",end="")
					print(l1[2],end="")
					print("\t\t"+l1[1]+"\n")
					c=str(i)
					c+=str("\t")
					c+=str(l1[0])
					c+=str("\t"+l1[2]+"\t\t"+l1[1]+"\n")
					f.write(c)
					c=''
					j=[]
					j.append(l1[0])
					j.append(l1[2])
					l.append(j)
			break
	if flag==0:
		print("No result found")
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			#na='Relation_Sentence_vibhakti_and_0_vibhakti'
			#na+=str(vibhakti+karak)
			na=input('Enter name of output file: ')
			cho=input('Do you want to see relation between words of single sentence?(press y for yes and  n for no) ')
			if cho=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif cho=='n':
				relation(na,j,l)
		ch=input("Do you want to see other karak also?(Press 'y' for yes and 'n' for no) ")
		if ch=='y':
			vibh(vibhakti)
def category(pos):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l4=[]
	l5=[]
	l6=[]
	l7=[]
	#name='category_'
	name=input('Enter name of output file: ')
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,count(*) from Tword where postag=? or category=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(pos,pos))
	for row41 in cursor91:
		l1=[]
		if row41[9]!='NULL':
			l1.append(row41[9])
		elif row41[8]!='NULL':
			l1.append(row41[8])
		elif row41[7]!='NULL':
			l1.append(row41[7])
		elif row41[6]!='NULL':
			l1.append(row41[6])
		elif row41[5]!='NULL':
			l1.append(row41[5])
		elif row41[4]!='NULL':
			l1.append(row41[4])
		elif row41[5]!='NULL':
			l1.append(row41[3])
		elif row41[2]!='NULL':
			l1.append(row41[2])
		elif row41[1]!='NULL':
			l1.append(row41[1])
		elif row41[0]!='NULL':
			l1.append(row41[0])
		l1.append(row41[10])
		l1.append(row41[11])
		l2.append(l1)
	for l1 in l2:
		print(l1,end="")
		print('\t',end="")
	karak=input('\n Enter karak you want: ')
	#name+=str(pos+karak)
	f=open(os.path.join(path,name),'w')
	c="SNo\tWord\tRelated_Word\tVerb Relation\tsid\tfilename\t\t\t\t\tSentence\n"
	f.write(c)
	c=''
	print("SNo\tWord\tRelated_Word\tVerb Relation\tsid\tfilename\t\t\t\t\tSentence")
	cursor=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,postag,category from Tword where postag=? or category=?',(pos,pos))
	for row in cursor:
		if row[10]==pos:
			if row[0]==karak:
				cursor1=conn.execute('select distinct word,sid,filename,wrelation from Tword  where postag=? and karak=?',(pos,karak))                 
				for row1 in cursor1:
					l4=[]
					l4.append(row1[0])
					l4.append(row1[1])
					l4.append(row1[2])
					l4.append(row1[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break	
			elif karak==row[1]:
				cursor3=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and modifier=?',(pos,karak))
				for row3 in cursor3:
					l4=[]
					l4.append(row3[0])
					l4.append(row3[1])
					l4.append(row3[2])
					l4.append(row3[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[2]:
				cursor5=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and fragment=?',(pos,karak))
				for row5 in cursor5:
					l4=[]
					l4.append(row5[0])
					l4.append(row5[1])
					l4.append(row5[2])
					l4.append(row5[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[3]:
				cursor7=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and symbol=? ',(pos,karak))
				for row7 in cursor7:
					l4=[]
					l4.append(row7[0])
					l4.append(row7[1])
					l4.append(row7[2])
					l4.append(row7[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[4]:
				cursor9=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and saha=?',(pos,karak))
				for row9 in cursor9:
					l4=[]
					l4.append(row9[0])
					l4.append(row9[1])
					l4.append(row9[2])
					l4.append(row9[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[5]:
				cursor11=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and shashthi=?',(pos,karak))
				for row11 in cursor11:
					l4=[]
					l4.append(row11[0])
					l4.append(row11[1])
					l4.append(row11[2])
					l4.append(row11[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[6]:
				cursor13=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and adverbs=?',(pos,karak))
				for row13 in cursor13:
					l4=[]
					l4.append(row13[0])
					l4.append(row13[1])
					l4.append(row13[2])
					l4.append(row13[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[7]:
				cursor15=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and cause=?',(pos,karak))
				for row15 in cursor15:
					l4=[]
					l4.append(row15[0])
					l4.append(row15[1])
					l4.append(row15[2])
					l4.append(row15[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[8]:
				cursor17=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and relation=?',(pos,karak))
				for row17 in cursor17:
					l4=[]
					l4.append(row17[0])
					l4.append(row17[1])
					l4.append(row17[2])
					l4.append(row17[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[9]:
				cursor19=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and other=?',(pos,karak))
				for row19 in cursor19:
					l4=[]
					l4.append(row19[0])
					l4.append(row19[1])
					l4.append(row19[2])
					l4.append(row19[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
		elif row[11]==pos:
			if row[0]==karak:
				cursor1=conn.execute('select distinct word,sid,filename,wrelation from Tword  where category=? and karak=?', (pos,karak))
				for row1 in cursor1:
					l4=[]
					l4.append(row1[0])
					l4.append(row1[1])
					l4.append(row1[2])
					l4.append(row1[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[1]:
				cursor3=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and modifier=?',(pos,karak))
				for row3 in cursor3:
					l4=[]
					l4.append(row3[0])
					l4.append(row3[1])
					l4.append(row3[2])
					l4.append(row3[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[2]:
				cursor5=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and fragment=?',(pos,karak))
				for row5 in cursor5:
					l4=[]
					l4.append(row5[0])
					l4.append(row5[1])
					l4.append(row5[2])
					l4.append(row5[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[3]:
				cursor7=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and symbol=?',(pos,karak))
				for row7 in cursor7:
					l4=[]
					l4.append(row7[0])
					l4.append(row7[1])
					l4.append(row7[2])
					l4.append(row7[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[4]:
				cursor9=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and saha=?',(pos,karak))
				for row9 in cursor9:
					l4=[]
					l4.append(row9[0])
					l4.append(row9[1])
					l4.append(row9[2])
					l4.append(row9[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[5]:
				cursor11=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and shashthi=?',(pos,karak))
				for row11 in cursor11:
					l4=[]
					l4.append(row11[0])
					l4.append(row11[1])
					l4.append(row11[2])
					l4.append(row11[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[6]:
				cursor13=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and adverbs=?',(pos,karak))
				for row13 in cursor13:
					l4=[]
					l4.append(row13[0])
					l4.append(row13[1])
					l4.append(row13[2])
					l4.append(row13[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[7]:
				cursor15=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and cause=?',(pos,karak))
				for row15 in cursor15:
					l4=[]
					l4.append(row15[0])
					l4.append(row15[1])
					l4.append(row15[2])
					l4.append(row15[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[8]:
				cursor17=conn.execute('select distinct word,sid,filename,wrelation from Tword where category=? and relation=?',(pos,karak))
				for row17 in cursor17:
					l4=[]
					l4.append(row17[0])
					l4.append(row17[1])
					l4.append(row17[2])
					l4.append(row17[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
			elif karak==row[9]:
				cursor19=conn.execute('select distinct word,sid,filename,wrelation from Tword where postag=? and other=?',(pos,karak))
				for row19 in cursor19:
					l4=[]
					l4.append(row19[0])
					l4.append(row19[1])
					l4.append(row19[2])
					l4.append(row19[3])
					l5.append(l4)
				for l4 in l5:
					cursor21=conn.execute('select distinct t1.name,t1.sid,t1.filename,t2.words,t3.sentence from Tword t1 join Tchunk t2 join Tsentence t3 where t1.category="v" and t1.sid=? and t1.filename=? and t1.name=? and t1.sid==t2.sid and t1.filename==t2.filename and t1.chunkid==t2.chunkid and t1.filename==t3.filename and t1.sid==t3.sid',(l4[1],l4[2],l4[3]))
					for row21 in cursor21:
						flag=1
						j=[]
						i=i+1
						print(i, end="")
						print("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+row21[4]+"\n\n")
						c=str(i)
						c+=str("\t"+l4[0]+"\t"+row21[0]+"\t\t"+row21[3]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+row21[4]+"\n")
						f.write(c)
						c=''    
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
				break
	if flag==0:
		print("No result found")
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
		'''ch=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		i=0
		if ch=='y':
			#st='Sentence_category_'
			#st+=str(pos+karak)
			st=input('Enter name of output file: ')
			print("SNo\tSid\tFilename\t\t\t\tSentence")
			sent(st,j,l)'''
def sent(name,list1=[],list2=[]):
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	z=input('Do you want to see all sentences or some sentences?(press "a" for all and "s" for some) ') 
	l1=[]
	l2=[] 
	l3=[]
	l4=[]
	m=0
	f=open(os.path.join(path,name),'w')
	if z=='s':
		m=int(input('Hom many sentences you want to see? '))
		s="SNo\tSid\tFilename\t\t\t\t\t\tSentence\n"
		print(s)
		f.write(s)
		s=''
		k=0
		i=0
		while k<m:
			cursor=conn.execute('select distinct sid,filename,sentence from Tsentence where sid=? and filename=?',(list2[k][0],list2[k][1]))
			for row in cursor:
				i=i+1
				print(i,end="")
				print('\t',end="")
				print(row[0],end="")
				print("\t",end="")
				print(row[1]+"\t\t"+row[2]+"\n")
				s=str(i)
				s+=str('\t')
				s+=str(row[0])
				s+=str("\t"+row[1]+"\t\t"+row[2]+"\n")
				f.write(s)
				s=''
				l3=[]
				l3.append(row[0])
				l3.append(row[1])
				l4.append(l3)
			k=k+1
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			#na='Relation_vibhakti_'
			#na+=str(category)
			na=input('Enter name of output file: ')
			#na=name
			choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,l3,l4)
	elif z=='a':
		s="SNo\tSid\tFilename\t\t\t\t\t\tSentence\n"
		print(s)
		f.write(s)
		s=''
		i=0
		for list1 in list2:
			curso=conn.execute('select distinct sid,filename,sentence from Tsentence where sid=? and filename=?',(list1[0],list1[1]))
			#for l1 in l2:
			for row in curso:
				i=i+1
				print(i,end="")
				print('\t',end="")
				print(row[0],end="")
				print("\t",end="")
				print(row[1]+"\t\t"+row[2]+"\n")
				s=str(i)
				s+=str('\t')
				s+=str(row[0])
				s+=str("\t"+row[1]+"\t\t"+row[2]+"\n")
				f.write(s)
				l3=[]
				l3.append(row[0])
				l3.append(row[1])
				l4.append(l3)
				s=''
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			#na='Relation_vibhakti_'
			#na+=str(category)
			#na=name
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,l3,l4)
def vibhakti(category):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	#name='Vibhakti_category_'
	#name+=str(category)
	name=input('Enter name of output file: ')
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	c="SNo\tword\tVibhakti\tsid\tfilename\t\t\t\t\t\tsentence\n"
	f.write(c)
	c=''
	print("SNo\tword\tVibhakti\tsid\tfilename\t\t\t\t\t\tsentence")
	#cursor=conn.execute('select distinct count(*),vibhakti from Tword where category=? or postag=? group by vibhakti',(category,category))
	cursor=conn.execute('select distinct word,vibhakti,sid,filename from Tword  where category=? or postag=? and vibhakti!="NULL" group by vibhakti',(category,category))
	for row in cursor:
		cursor3=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row[2],row[3]))
		for row3 in cursor3:
			flag=1
			i=i+1
			print(i,end="")
			print("\t"+row[0]+"\t"+row[1]+"\t",end="")
			print(row[2],end="")
			print("\t"+row[3]+"\t"+row3[0]+"\n\n")
			c=str(i)
			c+=str("\t"+row[0]+"\t"+row[1]+"\t")
			c+=str(row[2])
			c+=str("\t"+row[3]+"\t"+row3[0]+"\n")
			f.write(c)
			c=''
			j=[]
			j.append(row[2])
			j.append(row[3])
			l.append(j)
	'''cursor3=conn.execute('select distinct vibhakti,sid,filename from Tword where category=? or postag=? and vibhakti!="NULL"',(category,category))
	for row3 in cursor3:
		j=[]
		j.append(row3[1])
		j.append(row3[2])
		l.append(j)'''
	if flag==0:
		print("No result found")
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
		'''choi=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		if choi=='y':
			#st=name
			#st='Sentence_vibhakti_'
			st=input('Enter name of output file: ')
			ch=input("Do you want to see sentences for single vibhakti or for all vibhakti?(Press 's' for single and 'a' for all) ")
			if ch=='s':
				cho=input('Enter vibhakti: ')
				#st+=str(category+cho)
				cursor1=conn.execute('select distinct sid,filename from Tword where category=? or postag=? and vibhakti=? and vibhakti!="NULL"',(category,category,cho))
				for row1 in cursor1:
					l1=[]
					l1.append(row1[0])
					l1.append(row1[1])
					l2.append(l1)
				sent(st,l1,l2)
			elif ch=='a':
				#st+=str(category)
				sent(st,j,l)'''
def verb(vibhakti):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	l5=[]
	l6=[]
	l7=[]
	#name='Verb_'
	name=input('Enter name of output file: ')
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	s='0_'
	s+=str(vibhakti)
	'''cho=input('Do you want to see result for '+vibhakti+' and '+s+' both form or for '+vibhakti+' single form?(Press "s" for single and "b" for both) ')
	if cho=='s':
		cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,))
		for row41 in cursor91:
			if row41[9]!='NULL':
				l1.append(row41[9])
			elif row41[8]!='NULL':
				l1.append(row41[8])
			elif row41[7]!='NULL':
				l1.append(row41[7])
			elif row41[6]!='NULL':
				l1.append(row41[6])
			elif row41[5]!='NULL':
				l1.append(row41[5])
			elif row41[4]!='NULL':
				l1.append(row41[4])
			elif row41[5]!='NULL':
				l1.append(row41[3])
			elif row41[2]!='NULL':
				l1.append(row41[2])
			elif row41[1]!='NULL':
				l1.append(row41[1])
			elif row41[0]!='NULL':
				l1.append(row41[0])
		print(l1)
		karak=input('Enter karak: ') 
		#name+=str(vibhakti+karak)
		f=open(os.path.join(path,name),'w')
		c="SNo\tVerb\t\tWord\t\tChunk Words\n"
		f.write(c)
		c=''
		print("SNo\tVerb\t\tWord\t\tChunk Words")
		cursor=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,))
		for row in cursor:
			if karak==row[0]:
				cursor1=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.karak=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak)) 
				for row1 in cursor1:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row1[0]+"\t"+row1[1]+"\t"+row1[2])
					c=str(i)
					c+=str("\t")
					c+=str(row1[0]+"\t"+row1[1]+"\t\t"+row1[2]+"\n")
					f.write(c)
					c=''
					j.append(row1[3])
					j.append(row1[4])
					l.append(j)
				break
			if karak==row[1]:
				cursor2=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.modifier=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row2 in cursor2:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row2[0]+"\t"+row2[1]+"\t"+row2[2])
					c=str(i)
					c+=str("\t")
					c+=str(row2[0]+"\t"+row2[1]+"\t\t"+row2[2]+"\n")
					f.write(c)
					c=''
					j.append(row2[3])
					j.append(row2[4])
					l.append(j)
				break
			if karak==row[2]:
				cursor3=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.fragment=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row3 in cursor3:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row3[0]+"\t"+row3[1]+"\t"+row3[2])
					c=str(i)
					c+=str("\t")
					c+=str(row3[0]+"\t"+row3[1]+"\t\t"+row3[2]+"\n")
					f.write(c)
					c=''
					j.append(row3[3])
					j.append(row3[4])
					l.append(j)
				break
			if karak==row[3]:
				cursor4=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.symbol=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row4 in cursor4:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row4[0]+"\t"+row4[1]+"\t"+row4[2])
					c=str(i)
					c+=str("\t")
					c+=str(row4[0]+"\t"+row4[1]+"\t\t"+row4[2]+"\n")
					f.write(c)
					c=''
					j.append(row4[3])
					j.append(row4[4])
					l.append(j)
				break
			if karak==row[4]:
				cursor5=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.saha=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row5 in cursor5:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row5[0]+"\t"+row5[1]+"\t"+row5[2])
					c=str(i)
					c+=str("\t")
					c+=str(row5[0]+"\t"+row5[1]+"\t\t"+row5[2]+"\n")
					f.write(c)
					c=''
					j.append(row5[3])
					j.append(row5[4])
					l.append(j)
				break
			if karak==row[5]:
				cursor6=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.shashthi=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row6 in cursor6:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row6[0]+"\t"+row6[1]+"\t"+row6[2])
					c=str(i)
					c+=str("\t")
					c+=str(row6[0]+"\t"+row6[1]+"\t\t"+row6[2]+"\n")
					f.write(c)
					c=''
					j.append(row6[3])
					j.append(row6[4])
					l.append(j)
				break
			if karak==row[6]:
				cursor7=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.adverbs=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row7 in cursor7:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row7[0]+"\t"+row7[1]+"\t"+row7[2])
					c=str(i)
					c+=str("\t")
					c+=str(row7[0]+"\t"+row7[1]+"\t\t"+row7[2]+"\n")
					f.write(c)
					c=''
					j.append(row7[3])
					j.append(row7[4])
					l.append(j)
				break
			if karak==row[7]:
				cursor8=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.cause=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row8 in cursor8:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row8[0]+"\t"+row8[1]+"\t"+row8[2])
					c=str(i)
					c+=str("\t")
					c+=str(row8[0]+"\t"+row8[1]+"\t\t"+row8[2]+"\n")
					f.write(c)
					c=''
					j.append(row8[3])
					j.append(row8[4])
					l.append(j)
				break
			if karak==row[8]:
				cursor9=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.relation=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row9 in cursor9:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row9[0]+"\t"+row9[1]+"\t"+row9[2])
					c=str(i)
					c+=str("\t")
					c+=str(row9[0]+"\t"+row9[1]+"\t\t"+row9[2]+"\n")
					f.write(c)
					c=''
					j.append(row9[3])
					j.append(row9[4])
					l.append(j)
				break
			if karak==row[9]:
				cursor10=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,count(*) from Tword t1 join Tchunk t2 where t1.vibhakti=? and t1.other=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename group by t1.root',(vibhakti,karak))
				for row10 in cursor10:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row10[0]+"\t"+row10[1]+"\t"+row10[2])
					c=str(i)
					c+=str("\t")
					c+=str(row10[0]+"\t"+row10[1]+"\t\t"+row10[2]+"\n")
					f.write(c)
					c=''
					j.append(row10[3])
					j.append(row10[4])
					l.append(j)
				break
	elif cho=='b':'''
	a=[]
	cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,count(*) from Tword where vibhakti=? or vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,s))
	for row41 in cursor91:
		l1=[]
		if row41[9]!='NULL':
			l1.append(row41[9])
		elif row41[8]!='NULL':
			l1.append(row41[8])
		elif row41[7]!='NULL':
			l1.append(row41[7])
		elif row41[6]!='NULL':
			l1.append(row41[6])
		elif row41[5]!='NULL':
			l1.append(row41[5])
		elif row41[4]!='NULL':
			l1.append(row41[4])
		elif row41[5]!='NULL':
			l1.append(row41[3])
		elif row41[2]!='NULL':
			l1.append(row41[2])
		elif row41[1]!='NULL':
			l1.append(row41[1])
		elif row41[0]!='NULL':
			l1.append(row41[0])
		l1.append(row41[10])
		l1.append(row41[11])
		a.append(l1)
	for l1 in a:
		print(l1,end="")
	karak=input('\n Enter karak: ')
		#name+=str(vibhakti+s+karak)
	f=open(os.path.join(path,name),'w')
	c="SNo\tVerb\tWord\t\tChunk Words\tsid\tfilename\t\t\t\t\t\tsentence\n"
	f.write(c)
	c=''
	print("SNo\tVerb\tWord\t\tChunk Words\tsid\tfilename\t\t\t\t\t\tsentence")
	cursor=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? or vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,s))
	for row in cursor:
		if karak==row[0]:
			cursor11=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.karak=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename  and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso11=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.karak=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row11 in cursor11:
				l4=[]
				flag=1
				l4.append(row11[0])
				l4.append(row11[1])
				l4.append(row11[2])
				l4.append(row11[3])
				l4.append(row11[4])
				l4.append(row11[5])
				l5.append(l4)
			for row1 in curso11:
				l6=[]
				flag=1
				l6.append(row1[0])
				l6.append(row1[1])
				l6.append(row1[2])
				l6.append(row1[3])
				l6.append(row1[4])
				l6.append(row1[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[1]:
			cursor12=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.modifier=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso12=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.modifier=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row12 in cursor12:
				l4=[]
				flag=1
				l4.append(row12[0])
				l4.append(row12[1])
				l4.append(row12[2])
				l4.append(row12[3])
				l4.append(row12[4])
				l4.append(row12[5])
				l5.append(l4)
			for row2 in curso12:
				l6=[]
				flag=1
				l6.append(row2[0])
				l6.append(row2[1])
				l6.append(row2[2])
				l6.append(row2[3])
				l6.append(row2[4])
				l6.append(row2[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[2]:
			cursor13=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.fragment=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso13=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.fragment=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row13 in cursor13:
				#print(row13)
				l4=[]
				flag=1
				l4.append(row13[0])
				l4.append(row13[1])
				l4.append(row13[2])
				l4.append(row13[3])
				l4.append(row13[4])
				l4.append(row13[5])
				l5.append(l4)
			for row3 in curso13:
				l6=[]
				flag=1
				l6.append(row3[0])
				l6.append(row3[1])
				l6.append(row3[2])
				l6.append(row3[3])
				l6.append(row3[4])
				l6.append(row3[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[3]:
			cursor14=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.symbol=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso14=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.symbol=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row14 in cursor14:
				l4=[]
				flag=1
				l4.append(row14[0])
				l4.append(row14[1])
				l4.append(row14[2])
				l4.append(row14[3])
				l4.append(row14[4])
				l4.append(row14[5])
				l5.append(l4)
			for row4 in curso14:
				l6=[]
				flag=1
				l6.append(row4[0])
				l6.append(row4[1])
				l6.append(row4[2])
				l6.append(row4[3])
				l6.append(row4[4])
				l6.append(row4[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[4]:
			cursor15=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.saha=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso15=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.saha=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row15 in cursor15:
				l4=[]
				flag=1
				l4.append(row15[0])
				l4.append(row15[1])
				l4.append(row15[2])
				l4.append(row15[3])
				l4.append(row15[4])
				l4.append(row15[5])
				l5.append(l4)
			for row5 in curso15:
				l6=[]   
				flag=1
				l6.append(row5[0])
				l6.append(row5[1])
				l6.append(row5[2])
				l6.append(row5[3])
				l6.append(row5[4])
				l6.append(row5[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[5]:
			cursor16=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.shashthi=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso16=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.shashthi=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row16 in cursor16:
				l4=[]
				flag=1
				l4.append(row16[0])
				l4.append(row16[1])
				l4.append(row16[2])
				l4.append(row16[3])
				l4.append(row16[4])
				l4.append(row16[5])
				l5.append(l4)
			for row6 in curso16:
				l6=[]
				flag=1
				l6.append(row6[0])
				l6.append(row6[1])
				l6.append(row6[2])
				l6.append(row6[3])
				l6.append(row6[4])
				l6.append(row6[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[6]:
			cursor17=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.adverbs=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso17=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.adverbs=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row17 in cursor17:
				l4=[]
				flag=1
				l4.append(row17[0])
				l4.append(row17[1])
				l4.append(row17[2])
				l4.append(row17[3])
				l4.append(row17[4])
				l4.append(row17[5])
				l5.append(l4)
			for row7 in curso17:
				l6=[]
				flag=1
				l6.append(row7[0])
				l6.append(row7[1])
				l6.append(row7[2])
				l6.append(row7[3])
				l6.append(row7[4])
				l6.append(row7[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[7]:
			cursor18=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.cause=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso18=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.cause=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row18 in cursor18:
				l4=[]
				flag=1
				l4.append(row18[0])
				l4.append(row18[1])
				l4.append(row18[2])
				l4.append(row18[3])
				l4.append(row18[4])
				l4.append(row18[5])
				l5.append(l4)
			for row8 in curso18:
				l6=[]
				flag=1
				l6.append(row8[0])
				l6.append(row8[1])
				l6.append(row8[2])
				l6.append(row8[3])
				l6.append(row8[4])
				l6.append(row8[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[8]:
			cursor19=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.relation=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso19=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.relation=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row19 in cursor19:
				l4=[]
				flag=1
				l4.append(row19[0])
				l4.append(row19[1])
				l4.append(row19[2])
				l4.append(row19[3])
				l4.append(row19[4])
				l4.append(row19[5])
				l5.append(l4)
			for row9 in curso19:
				l6=[]
				flag=1
				l6.append(row9[0])
				l6.append(row9[1])
				l6.append(row9[2])
				l6.append(row9[3])
				l6.append(row9[4])
				l6.append(row9[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
		elif karak==row[9]:
			cursor20=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.other=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(vibhakti,karak))
			curso20=conn.execute('select distinct t1.root, t1.word,t2.words,t1.sid,t1.filename,t3.sentence,count(*) from Tword t1 join Tchunk t2 join Tsentence t3 where t1.vibhakti=? and t1.other=? and t1.category="v" and t1.sid==t2.sid and t1.chunkid==t2.chunkid and t1.fragment!="pof" and t1.filename==t2.filename and t1.sid==t3.sid and t1.filename==t3.filename group by t3.sentence',(s,karak))
			for row20 in cursor20:
				l4=[]
				flag=1
				l4.append(row20[0])
				l4.append(row20[1])
				l4.append(row20[2])
				l4.append(row20[3])
				l4.append(row20[4])
				l4.append(row20[5])
				l5.append(l4)
			for row10 in curso20:
				l6=[]
				flag=1
				l6.append(row10[0])
				l6.append(row10[1])
				l6.append(row10[2])
				l6.append(row10[3])
				l6.append(row10[4])
				l6.append(row10[5])
				l7.append(l6)
			for l6 in l7:
				l5.append(l6)
	for l4 in l5:
		j=[]
		i=i+1
		print(i,end="")
		print("\t",end="")
		print(l4[0]+"\t"+l4[1]+"\t"+l4[2]+"\t\t",end="")
		print(l4[3],end="")
		print("\t"+l4[4]+"\t\t"+l4[5]+"\n\n")
		c=str(i)
		c+=str("\t")
		c+=str(l4[0]+"\t"+l4[1]+"\t"+l4[2]+"\t\t")
		c+=str(l4[3])
		c+=str("\t"+l4[4]+"\t\t"+l4[5]+"\n")
		f.write(c)
		c=''
		j.append(l4[3])
		j.append(l4[4])
		l.append(j)	
	if flag==0:
		print("No result found.")
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
		'''ch=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		if ch=='y':
			#st='Sentence_verb_'
			st=input('Enter name of output file: ')
			#st=name
			choi=input('Do you want to see sentence of all verbs or single verb?(Press "s" for single and "a" for all) ')
			if choi=='s':
				z=input('Enter root verb or verb: ')
				if cho=='b':
					#st+=str(vibhakti+s+karak)
					for j in l:
						cursor22=conn.execute('select distinct sid,filename from Tword where root=? or word=? and vibhakti=? and sid=? and filename=?',(z,z,vibhakti,j[0],j[1]))
						curso22=conn.execute('select distinct sid,filename from Tword where root=? or word=? and vibhakti=? and sid=? and filename=?',(z,z,s,j[0],j[1]))
						for row22 in cursor22:
							l2=[]
							l2.append(row22[0])
							l2.append(row22[1])
							l3.append(l2)
						l8=[]
						l9=[]
						for ro22 in curso22:
							l8=[]
							l8.append(ro22[0])
							l8.append(ro22[1])
							l9.append(l8)
						for l8 in l9:
							l2.append(l8)
					sent(st,l2,l3)
				elif cho=='s':
					#st+=str(vibhakti+karak)
					for j in l:
						cursor23=conn.execute('select distinct sid,filename from Tword where root=? or word=? and vibhakti=? and sid=? and filename=?',(z,z,vibhakti,j[0],j[1]))
						for row23 in cursor23:
							l2=[]
							l2.append(row23[0])
							l2.append(row23[1])
							l3.append(l2)
					sent(st,l2,l3)
			elif choi=='a':
				if cho=='b':
					#st+=str(vibhakti+s+karak)
					sent(st,j,l)
				elif cho=='s':
					#st+=str(vibhakti+karak)
					sent(st,j,l)'''
def modify(Modifier):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	#name='Modifier_'
	#name+=str(Modifier)
	name=input('Enter name of output file: ')
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	z=input("Do you want to see all chunks or some?(Press 'a' for all and 's' for some) ")
	if z=='s':
		m=int(input("How many you want to see? "))
		print("SNo\tword\trelated_word\tsid\tfilename\t\t\t\t\t\tsentence")
		c="SNo\tword\trelated_word\tsid\tfilename\t\t\t\t\t\tsentence\n"
		f.write(c)
		c=''
		cursor1=conn.execute('select distinct t2.sentence,t3.sid,t3.filename,t3.word,t3.wrelation from Tsentence t2 join Tword t3 where t2.sid==t3.sid and t2.filename==t3.filename and t3.modifier=? limit ?',(Modifier,m))
		for row1 in cursor1:
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row1[3]+"\t"+row1[4]+"\t",end="")
			print(row1[1],end="")
			print("\t\t"+row1[2]+"\t\t"+row1[0]+"\n\n")
			c=str(i)
			c+=str("\t")
			c+=str(row1[3]+"\t"+row1[4]+"\t")
			c+=str(row1[1])
			c+=str("\t\t"+row1[2]+"\t\t"+row1[0]+"\n")
			f.write(c)
			c=''
			j.append(row1[1])
			j.append(row1[2])
			l.append(j)
	if z=='a':
		print("SNo\tword\trelated_word\tsid\tfilename\t\t\t\t\t\tsentence")
		c="SNo\tword\trelated_word\tsid\tfilename\t\t\t\t\t\tsentence\n"
		f.write(c)
		c=''
		cursor1=conn.execute('select distinct t2.sentence,t3.sid,t3.filename,t3.word,t3.wrelation from Tsentence t2 join Tword t3 where t2.sid==t3.sid and t2.filename==t3.filename and t3.modifier=?',(Modifier,))
		for row1 in cursor1:
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row1[3]+"\t"+row1[4]+"\t",end="")
			print(row1[1],end="")
			print("\t\t"+row1[2]+"\t\t"+row1[0]+"\n\n")
			c=str(i)
			c+=str("\t")
			c+=str(row1[3]+"\t"+row1[4]+"\t")
			c+=str(row1[1])
			c+=str("\t\t"+row1[2]+"\t\t"+row1[0]+"\n")
			f.write(c)
			c=''
			j.append(row1[1])
			j.append(row1[2])
			l.append(j)
	if flag==0:
		print('No result found')
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
		'''ch=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		i=0
		if ch=='y':
			#st='Sentence_modifier_'
			#st+=str(Modifier)
			st=input('Enter name of output file: ')
			#st=name
			sent(st,j,l)'''
def Word(word):
	flag=0
	i=0
	j=[]
	l=[]
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	#name='Sentence_word_'
	#name+=str(word)
	name=input('Enter name of output file: ')
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	s="SNo\tSid\tFilename\t\t\t\t\t\tSentence\n"
	f.write(s)
	s=''
	z=input('Do you want to see some sentences or all sentences?(press "a" for all and "s" for some) ')
	cursor=conn.execute('select root,word from Tword')
	for row in cursor:
		if word==row[0]:
			if z=='a':
				cursor1=conn.execute('Select t1.sid,t1.filename,t1.sentence from Tsentence t1 join Tword t2 where t1.sid==t2.sid and t1.filename==t2.filename and t2.root=?',(word,))
				print("SNo.\tSid\tFilename\t\t\t\t\tSentence")
				for row1 in cursor1:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row1[0],end="")
					print("\t",end="")
					print(row1[1]+"\t\t"+row1[2]+"\n\n")
					s=str(i)
					s+=str("\t")
					s+=str(row1[0])
					s+=str("\t"+row1[1]+"\t\t"+row1[2]+"\n")
					f.write(s)
					s=''
					j.append(row1[0])
					j.append(row1[1])
					l.append(j)
				break
		if word==row[1]:
			if z=='a':
				cursor1=conn.execute('Select t1.sid,t1.filename,t1.sentence from Tsentence t1 join Tword t2 where t1.sid==t2.sid and t1.filename==t2.filename and t2.word=?',(word,))
				print("SNo.\tSid\tFilename\t\t\t\t\tSentence")
				for row1 in cursor1:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row1[0],end="")
					print("\t",end="")
					print(row1[1]+"\t\t"+row1[2]+"\n\n")
					s=str(i)
					s+=str("\t")
					s+=str(row1[0])
					s+=str("\t"+row1[1]+"\t\t"+row1[2]+"\n")
					f.write(s)
					s=''
					j.append(row1[0])
					j.append(row1[1])
					l.append(j)
				break
		if word==row[0]:
			if z=='s':
				m=int(input('How many sentences you want to see? '))
				cursor2=conn.execute('Select t1.sid,t1.filename,t1.sentence from Tsentence t1 join Tword t2 where t1.sid==t2.sid and t1.filename==t2.filename and t2.root=? limit ?',(word,m))
				print("SNo.\tSid\tFilename\t\t\t\t\tSentence")
				for row2 in cursor2:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row2[0],end="")
					print("\t",end="")
					print(row2[1]+"\t\t"+row2[2]+"\n\n")
					s=str(i)
					s+=str("\t")
					s+=str(row2[0])
					s+=str("\t"+row2[1]+"\t\t"+row2[2]+"\n")
					f.write(s)
					s=''
					j.append(row2[0])
					j.append(row2[1])
					l.append(j)
				break
		if word==row[1]: 
			if z=='s':
				m=int(input('How many sentences you want to see? '))
				cursor2=conn.execute('Select t1.sid,t1.filename,t1.sentence from Tsentence t1 join Tword t2 where t1.sid==t2.sid and t1.filename==t2.filename and t2.word=? limit ?',(word,m))
				print("SNo.\tSid\tFilename\t\t\t\t\tSentence")
				for row2 in cursor2:
					flag=1
					j=[]
					i=i+1
					print(i,end="")
					print("\t",end="")
					print(row2[0],end="")
					print("\t",end="")
					print(row2[1]+"\t\t"+row2[2]+"\n\n")
					s=str(i)
					s+=str("\t")
					s+=str(row2[0])
					s+=str("\t"+row2[1]+"\t\t"+row2[2]+"\n")
					f.write(s)
					s=''
					j.append(row2[0])
					j.append(row2[1])
					l.append(j)
				break
	if flag==0:
		print('No result found')
	elif flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			#na='Relation_word_'
			#na+=str(word)
			na=input('Enter name of output file: ')
			#na=name
			choic=input('Do you want to see relation between words of single sentence?(press y for yes and  n for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				#fi=input('Enter filename: ')
				fi=name
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
def pofverb(vibhakti):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	#name='pofverb_'
	name=input('Enter name of output file: ')
	if not os.path.exists(path):
		os.makedirs(path)
	s='0_'
	s+=str(vibhakti)
	'''cho=input('Do you want to search for '+vibhakti+' and '+s+' both forms or single '+vibhakti+' form?(Press "s" for single and "b" for both) ')
	if cho=='s': 
		cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,))
		for row41 in cursor91:
			if row41[9]!='NULL':
				l1.append(row41[9])
			elif row41[8]!='NULL':
				l1.append(row41[8])
			elif row41[7]!='NULL':
				l1.append(row41[7])
			elif row41[6]!='NULL':
				l1.append(row41[6])
			elif row41[5]!='NULL':
				l1.append(row41[5])
			elif row41[4]!='NULL':
				l1.append(row41[4])
			elif row41[5]!='NULL':
				l1.append(row41[3])
			elif row41[2]!='NULL':
				l1.append(row41[2])
			elif row41[1]!='NULL':
				l1.append(row41[1])
			elif row41[0]!='NULL':
				l1.append(row41[0])
		print(l1)
		karak=input('Enter karak: ')
		#name+=str(vibhakti+karak)
		f=open(os.path.join(path,name),'w')
		c="SNo\tVerb\n"
		f.write(c)
		c=''
		cursor=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=?',(vibhakti,))
		for row in cursor:
			if karak==row[0]:
				cursor1=conn.execute('select sid,filename,wrelation from Tword where vibhakti=? and karak=?',(vibhakti,karak))
				for row1 in cursor1:
					cursor2=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=? group by filename',(row1[0],row1[2],row1[1]))	
					for row2 in cursor2:
						cursor3=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row2[0],row2[1],row2[2],row2[3],row2[4]))
						for row3 in cursor3:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row3[3])
							c=str(i)
							c+=str("\t"+row3[3]+"\n")
							f.write(c)
							c=''
							j.append(row3[0])
							j.append(row3[4])
							l.append(j)
				break
			if karak==row[1]:
				cursor4=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and modifier=?',(vibhakti,karak))
				for row4 in cursor4:
					cursor5=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row4[0],row4[4],row4[3]))
					for row5 in cursor5:
						cursor6=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row5[0],row5[1],row5[2],row5[3],row5[4]))
						for row6 in cursor6:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row6[3])
							c=str(i)
							c+=str("\t"+row6[3]+"\n")
							f.write(c)
							c=''
							j.append(row6[0])
							j.append(row6[4])
							l.append(j)
				break
			if karak==row[2]:
				cursor7=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and fragment=?',(vibhakti,karak))
				for row7 in cursor7:
					cursor8=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row7[0],row7[4],row7[3]))
					for row8 in cursor8:
						cursor9=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row8[0],row8[1],row8[2],row8[3],row8[4]))
						for row9 in cursor9:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row9[3])
							c=str(i)
							c+=str("\t"+row9[3]+"\n")
							f.write(c)
							c=''
							j.append(row9[0])
							j.append(row9[4])
							l.append(j)
				break
			if karak==row[3]:
				cursor10=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and symbol=?',(vibhakti,karak))
				for row10 in cursor10:
					cursor11=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row10[0],row10[4],row10[3]))
					for row11 in cursor11:
						cursor12=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row11[0],row11[1],row11[2],row11[3],row11[4]))
						for row12 in cursor12:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row12[3])
							c=str(i)
							c+=str("\t"+row12[3]+"\n")
							f.write(c)
							c=''
							j.append(row12[0])
							j.append(row12[4])
							l.append(j)
				break
			if karak==row[4]:
				cursor13=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and saha=?',(vibhakti,karak))				
				for row13 in cursor13:
					cursor14=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row13[0],row13[4],row13[3]))
					for row14 in cursor14:
						cursor15=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row14[0],row14[1],row14[2],row14[3],row14[4]))
						for row15 in cursor15:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row15[3])
							c=str(i)
							c+=str("\t"+row15[3]+"\n")
							f.write(c)
							c=''
							j.append(row15[0])
							j.append(row15[4])
							l.append(j)
				break
			if karak==row[5]:
				cursor16=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and shashthi=?',(vibhakti,karak))
				for row16 in cursor16:
					cursor17=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row16[0],row16[4],row16[3]))
					for row17 in cursor17:
						cursor18=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row17[0],row17[1],row17[2],row17[3],row17[4]))
						for row18 in cursor18:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row18[3])
							c=str(i)
							c+=str("\t"+row18[3]+"\n")
							f.write(c)
							c=''
							j.append(row18[0])
							j.append(row18[4])
							l.append(j)
				break
			if karak==row[6]:
				cursor19=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and adverbs=?',(vibhakti,karak))
				for row19 in cursor19:
					cursor20=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row19[0],row19[4],row19[3]))
					for row20 in cursor20:
						cursor21=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row20[0],row20[1],row20[2],row20[3],row20[4]))
						for row21 in cursor21:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row21[3])
							c=str(i)
							c+=str("\t"+row21[3]+"\n")
							f.write(c)
							c=''
							j.append(row21[0])
							j.append(row21[4])
							l.append(j)
				break
			if karak==row[7]:
				cursor22=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and cause=?',(vibhakti,karak))
				for row22 in cursor22:
					cursor23=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row22[0],row22[4],row22[3]))
					for row23 in cursor23:
						cursor24=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row23[0],row23[1],row23[2],row23[3],row23[4]))	
						for row24 in cursor24:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row24[3])
							c=str(i)
							c+=str("\t"+row24[3]+"\n")
							f.write(c)
							c=''
							j.append(row24[0])
							j.append(row24[4])
							l.append(j)
				break
			if karak==row[8]:
				cursor25=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and relation=?',(vibhakti,karak))		
				for row25 in cursor25:
					cursor26=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row25[0],row25[4],row25[3]))
					for row26 in cursor26:
						cursor27=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row26[0],row26[1],row26[2],row26[3],row26[4]))
						for row27 in cursor27:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row27[3])
							c=str(i)
							c+=str("\t"+row27[3]+"\n")
							f.write(c)
							c=''
							j.append(row27[0])
							j.append(row27[4])
							l.append(j)
				break
			if karak==row[9]:
				cursor28=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? and other=?',(vibhakti,karak))
				for row28 in cursor28:
					cursor29=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row28[0],row28[4],row28[3]))
					for row29 in cursor29:
						cursor30=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row29[0],row29[1],row29[2],row29[3],row29[4]))
						for row30 in cursor30:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row30[3])
							c=str(i)
							c+=str("\t"+row30[3]+"\n")
							f.write(c)
							c=''
							j.append(row30[0])
							j.append(row30[4])
							l.append(j)
				break
	elif cho=='b':'''
	cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,count(*) from Tword where vibhakti=? or vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,s))
	for row41 in cursor91:
		if row41[9]!='NULL':
			l1.append(row41[9])
		elif row41[8]!='NULL':
			l1.append(row41[8])
		elif row41[7]!='NULL':
			l1.append(row41[7])
		elif row41[6]!='NULL':
			l1.append(row41[6])
		elif row41[5]!='NULL':
			l1.append(row41[5])
		elif row41[4]!='NULL':
			l1.append(row41[4])
		elif row41[5]!='NULL':
			l1.append(row41[3])
		elif row41[2]!='NULL':
			l1.append(row41[2])
		elif row41[1]!='NULL':
			l1.append(row41[1])
		elif row41[0]!='NULL':
			l1.append(row41[0])
		l1.append(row41[10])
		l1.append(row41[11])
		l4.append(l1)
	for l1 in l4:
		print(l1,end="")
	karak=input('\nEnter karak: ')
	#name+=str(vibhakti+s+karak)
	f=open(os.path.join(path,name),'w')
	c="SNo\tVerb\n"
	f.write(c)
	c=''
	cursor=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? or vibhakti=?',(vibhakti,s))
	for row in cursor:
		if karak==row[0]:
			cursor31=conn.execute('select sid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and karak=?',(s,vibhakti,karak))
			for row31 in cursor31:
				cursor32=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=? group by filename',(row31[0],row31[2],row31[1]))
				for row32 in cursor32:
					cursor33=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row32[0],row32[1],row32[2],row32[3],row32[4]))
					for row33 in cursor33:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row33[3])
						c=str(i)
						c+=str("\t"+row33[3]+"\n")
						f.write(c)
						c=''
						j.append(row33[0])
						j.append(row33[4])
						l.append(j)
			break
		if karak==row[1]:
			cursor34=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and modifier=?',(s,vibhakti,karak))
			for row34 in cursor34:
				cursor35=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row34[0],row34[4],row34[3]))
				for row35 in cursor35:
					cursor36=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row35[0],row35[1],row35[2],row35[3],row35[4]))
					for row36 in cursor36:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row36[3])
						c=str(i)
						c+=str("\t"+row36[3]+"\n")
						f.write(c)
						c=''
						j.append(row36[0])
						j.append(row36[4])
						l.append(j)
			break
		if karak==row[2]:
			cursor37=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and fragment=?',(s,vibhakti,karak))
			for row37 in cursor37:
				cursor38=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row37[0],row37[4],row37[3]))
				for row38 in cursor38:
					cursor39=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row38[0],row38[1],row38[2],row38[3],row38[4]))
					for row39 in cursor39:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row39[3])
						c=str(i)
						c+=str("\t"+row39[3]+"\n")
						f.write(c)
						c=''
						j.append(row39[0])
						j.append(row39[4])
						l.append(j)
			break
		if karak==row[3]:
			cursor40=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and symbol=?',(s,vibhakti,karak))
			for row40 in cursor40:
				cursor41=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row40[0],row40[4],row40[3]))
				for row41 in cursor41:
					cursor42=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row41[0],row41[1],row41[2],row41[3],row41[4]))
					for row42 in cursor42:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row42[3])
						c=str(i)
						c+=str("\t"+row42[3]+"\n")
						f.write(c)
						c=''
						j.append(row42[0])
						j.append(row42[4])
						l.append(j)
			break
		if karak==row[4]:
			cursor43=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and saha=?',(s,vibhakti,karak))
			for row43 in cursor43:
				cursor44=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row43[0],row43[4],row43[3]))
				for row44 in cursor44:
					cursor45=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row44[0],row44[1],row44[2],row44[3],row44[4]))
					for row45 in cursor45:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row45[3])
						c=str(i)
						c+=str("\t"+row45[3]+"\n")
						f.write(c)
						c=''
						j.append(row45[0])
						j.append(row45[4])
						l.append(j)
			break
		if karak==row[5]:
			cursor46=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and shashthi=?',(s,vibhakti,karak))
			for row46 in cursor46:
				cursor47=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row46[0],row46[4],row46[3]))
				for row47 in cursor47:
					cursor48=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row47[0],row47[1],row47[2],row47[3],row47[4]))
					for row48 in cursor48:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row48[3])
						c=str(i)
						c+=str("\t"+row48[3]+"\n")
						f.write(c)
						c=''
						j.append(row48[0])
						j.append(row48[4])
						l.append(j)
			break
		if karak==row[6]:
			cursor49=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and adverbs=?',(s,vibhakti,karak))
			for row49 in cursor49:
				cursor50=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row49[0],row49[4],row49[3]))
				for row50 in cursor50:
					cursor51=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row50[0],row50[1],row50[2],row50[3],row50[4]))
					for row51 in cursor51:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row51[3])
						c=str(i)
						c+=str("\t"+row51[3]+"\n")
						f.write(c)
						c=''
						j.append(row51[0])
						j.append(row51[4])
						l.append(j)
			break
		if karak==row[7]:
			cursor52=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and cause=?',(s,vibhakti,karak))
			for row52 in cursor52:
				cursor53=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row52[0],row52[4],row52[3]))
				for row53 in cursor53:
					cursor54=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row53[0],row53[1],row53[2],row53[3],row53[4]))
					for row54 in cursor54:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row54[3])
						c=str(i)
						c+=str("\t"+row54[3]+"\n")
						f.write(c)
						c=''
						j.append(row54[0])
						j.append(row54[4])
						l.append(j)
			break
		if karak==row[8]:
			cursor55=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and relation=?',(s,vibhakti,karak))
			for row55 in cursor55:
				cursor56=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row55[0],row55[4],row55[3]))
				for row56 in cursor56:
					cursor57=conn.execute('select distinct sid,chunkid,wordid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row56[0],row56[1],row56[2],row56[3],row56[4]))
					for row57 in cursor57:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row57[3])
						c=str(i)
						c+=str("\t"+row57[3]+"\n")
						f.write(c)
						c=''
						j.append(row57[0])
						j.append(row57[4])
						l.append(j)
			break
		if karak==row[9]:
			cursor58=conn.execute('select sid,chunkid,wordid,filename,wrelation from Tword where vibhakti=? or vibhakti=? and other=?',(s,vibhakti,karak))
			for row58 in cursor58:
				cursor59=conn.execute('select sid,chunkid,wordid,root,filename from Tword where sid=? and word=? and filename=?',(row58[0],row58[4],row58[3]))
				for row59 in cursor59:
					cursor60=conn.execute('select distinct sid,wordid,chunkid,wverb,filename from Tverb where sid=? and chunkid=? and wordid=? and verb=? and pof="True" and filename=? ',(row59[0],row59[1],row59[2],row59[3],row59[4]))
					for row60 in cursor60:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(row60[3])
						c=str(i)
						c+=str("\t"+row60[3]+"\n")
						f.write(c)
						c=''
						j.append(row60[0])
						j.append(row60[4])
						l.append(j)
			break
	if flag==0:
		print('No result found')
	elif flag==1:
		ch=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		if ch=='y':
			#st='Sentence_pofverb_'
			st=input('Enter name of output file: ')
			choi=input('Do you want to see sentences of all verbs or single verb?(for all verbs press "a" and for single verb press"s") ')
			if choi=='s':
				z=input('Enter root verb or verb: ')
				#if cho=='b':
					#st+=str(vibhakti+s+karak)
				for j in l:
					cursor22=conn.execute('select distinct sid,filename from Tverb  where verb=? or wverb=? or word_verb=? and sid=? and filename=?',(z,z,z,j[0],j[1]))
					for row22 in cursor22:
						l2=[]
						l2.append(row22[0])
						l2.append(row22[1])
						l3.append(l2)
					print("SNo.\tSid\tFilename\t\t\t\t\tSentence")
					sent(st,l2,l3)
				'''elif cho=='s':
					#st+=str(vibhakti+karak)
					for j in l:
						cursor23=conn.execute('select distinct sid,filename from Tverb where verb=? or wverb=? and sid=? and filename=?',(z,z,j[0],j[1]))
						for row23 in cursor23:
							l2=[]
							l2.append(row23[0])
							l2.append(row23[1])
							l3.append(l2)
					print("SNo.\tSid\tFilename\t\t\t\t\tSentence")
					sent(st,l2,l3)'''
			elif choi=='a':
				#if cho=='b':
				print("SNo.\tSid\tFilename\t\t\t\tSentence")
					#st+=str(vibhakti+s+karak)
				sent(st,j,l)
				'''elif cho=='s':
					print("SNo.\tSid\tFilename\t\t\t\tSentence")
					#st+=str(vibhakti+s+karak)
					sent(st,j,l)'''
def modifyvibhakti(vibhakti):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l3=[]
	l4=[]
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	s='0_'
	s+=str(vibhakti)
	'''cho=input('Do you want to search for '+vibhakti+' and '+s+' both forms or single '+vibhakti+' form?(Press "s" for single and "b" for both) ')
	if cho=='s':
		cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,))
		for row41 in cursor91:
			if row41[9]!='NULL':
				l1.append(row41[9])
			elif row41[8]!='NULL':
				l1.append(row41[8])
			elif row41[7]!='NULL':
				l1.append(row41[7])
			elif row41[6]!='NULL':
				l1.append(row41[6])
			elif row41[5]!='NULL':
				l1.append(row41[5])
			elif row41[4]!='NULL':
				l1.append(row41[4])
			elif row41[5]!='NULL':
				l1.append(row41[3])
			elif row41[2]!='NULL':
				l1.append(row41[2])
			elif row41[1]!='NULL':
				l1.append(row41[1])
			elif row41[0]!='NULL':
				l1.append(row41[0])
		print(l1)
		karak=input('Enter karak: ')
		#name='ModifyVibhakti_'
		#name+=str(vibhakti+karak)
		name=input('Enter name of output file: ')
		f=open(os.path.join(path,name),'w')
		c="SNo\tChunk words\n"
		f.write(c)
		c=''
		cursor=conn.execute('select vibhakti,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword')
		print("SNo\tchunk Words")
		for row in cursor:
			if row[0]==vibhakti:
				if row[1]==karak:
					cursor1=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and karak=?',(vibhakti,karak))
					for row1 in cursor1:
						cursor2=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row1[0],row1[1],row1[2]))
						for row2 in cursor2:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row2[0])
							c=str(i)
							c+=str("\t"+row2[0]+"\n")
							f.write(c)
							c=''
							j.append(row2[1])
							j.append(row2[2])
							l.append(j)
					break
				if row[2]==karak:
					cursor3=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and modifier=?',(vibhakti,karak))
					for row3 in cursor3:
						cursor4=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row3[0],row3[1],row3[2]))
						for row4 in cursor4:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row4[0])
							c=str(i)
							c+=str("\t"+row4[0]+"\n")
							f.write(c)
							c=''	
							j.append(row4[1])
							j.append(row4[2])
							l.append(j)
					break
				if row[3]==karak:
					cursor5=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and fragment=?',(vibhakti,karak))
					for row5 in cursor5:
						cursor6=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row5[0],row5[1],row5[2]))
						for row6 in cursor6:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row6[0])
							c=str(i)
							c+=str("\t"+row6[0]+"\n")
							f.write(c)
							c=''
							j.append(row6[1])
							j.append(row6[2])
							l.append(j)
					break
				if row[4]==karak:
					cursor7=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and symbol=?',(vibhakti,karak))
					for row7 in cursor7:
						cursor8=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row7[0],row7[1],row7[2]))
						for row8 in cursor8:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row8[0])
							c=str(i)
							c+=str("\t"+row8[0]+"\n")
							f.write(c)
							c=''
							j.append(row8[1])
							j.append(row8[2])
							l.append(j)
					break
				if row[5]==karak:
					cursor9=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and saha=?',(vibhakti,karak))
					for row9 in cursor9:
						cursor10=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row9[0],row9[1],row9[2]))
						for row10 in cursor10:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row10[0])
							c=str(i)
							c+=str("\t"+row10[0]+"\n")
							f.write(c)
							c=''
							j.append(row10[1])
							j.append(row10[2])
							l.append(j)
					break
				if row[6]==karak:
					cursor11=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and shashthi=?',(vibhakti,karak))
					for row11 in cursor11:
						cursor12=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row11[0],row11[1],row11[2]))
						for row12 in cursor12:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row12[0])
							c=str(i)
							c+=str("\t"+row12[0]+"\n")
							f.write(c)
							c=''	
							j.append(row12[1])
							j.append(row12[2])
							l.append(j)
					break
				if row[7]==karak:
					cursor13=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and adverbs=?',(vibhakti,karak))
					for row13 in cursor13:
						cursor14=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row13[0],row13[1],row13[2]))				
						for row14 in cursor14:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row14[0])
							c=str(i)
							c+=str("\t"+row14[0]+"\n")
							f.write(c)
							c=''	
							j.append(row14[1])
							j.append(row14[2])
							l.append(j)
					break
				if row[8]==karak:
					cursor15=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and cause=?',(vibhakti,karak))
					for row15 in cursor15:	
						cursor16=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row15[0],row15[1],row15[2]))
						for row16 in cursor16:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row16[0])
							c=str(i)
							c+=str("\t"+row16[0]+"\n")
							f.write(c)
							c=''
							j.append(row16[1])
							j.append(row16[2])
							l.append(j)
					break
				if row[9]==karak:
					cursor17=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and relation=?',(vibhakti,karak))
					for row17 in cursor17:
						cursor18=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row17[0],row17[1],row17[2]))
						for row18 in cursor18:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row18[0])
							c=str(i)
							c+=str("\t"+row18[0]+"\n")
							f.write(c)
							c=''	
							j.append(row18[1])
							j.append(row18[2])
							l.append(j)
					break
				if row[10]==karak:
					cursor19=conn.execute('select sid,chunkid,filename from Tword where vibhakti=? and other=?',(vibhakti,karak))
					for row19 in cursor19:
						cursor20=conn.execute('select words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row19[0],row19[1],row19[2]))
						for row20 in cursor20:
							flag=1
							j=[]
							i=i+1
							print(i,end="")
							print("\t",end="")
							print(row20[0])
							c=str(i)
							c+=str("\t"+row20[0]+"\n")
							f.write(c)
							c=''	
							j.append(row20[1])
							j.append(row20[2])
							l.append(j)	
					break
	if cho=='b':'''	
	cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,count(*) from Tword where vibhakti=?  or vibhakti=? group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,s))
	for row41 in cursor91:
		l1=[]
		if row41[9]!='NULL':
			l1.append(row41[9])
		elif row41[8]!='NULL':
			l1.append(row41[8])
		elif row41[7]!='NULL':
			l1.append(row41[7])
		elif row41[6]!='NULL':
			l1.append(row41[6])
		elif row41[5]!='NULL':
			l1.append(row41[5])
		elif row41[4]!='NULL':
			l1.append(row41[4])
		elif row41[5]!='NULL':
			l1.append(row41[3])
		elif row41[2]!='NULL':
			l1.append(row41[2])
		elif row41[1]!='NULL':
			l1.append(row41[1])
		elif row41[0]!='NULL':
			l1.append(row41[0])
		l1.append(row41[10])
		l1.append(row41[11])
		l2.append(l1)
	for l1 in l2:
		print(l1,end="")
	karak=input('\nEnter karak: ')
	name=input('Enter name of output file: ')
	#name='ModifyVibhakti_'
	#name+=str(vibhakti+s+karak)
	f=open(os.path.join(path,name),'w')
	c="SNo\tword\tChunk words\tsid\tfilename\t\t\t\tsentence\n"
	f.write(c)
	c=''
	cursor=conn.execute('select distinct vibhakti,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? or vibhakti=?',(vibhakti,s))
	print("SNo\tword\tChunk words\tsid\tfilename\t\t\t\tsentence")	
	for row in cursor:
		if row[1]==karak:
			cursor40=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and karak=?',(vibhakti,s,karak))
			for row40 in cursor40:
				sc=str(row40[3])
				cursor39=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row40[0],row40[1],row40[2]))
				for row39 in cursor39:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row39[1],row39[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row39[0]+"\t\t",end="")
						print(row39[1],end="")
						print("\t"+row39[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row39[0]+"\t\t")
						c+=str(row39[1])
						c+=str("\t"+row39[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row39[1])
						j.append(row39[2])
						l.append(j)
			break
		if row[2]==karak:
			cursor38=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and modifier=?',(vibhakti,s,karak))
			for row38 in cursor38:
				sc=str(row38[3])
				cursor37=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?' ,(row38[0],row38[1],row38[2]))
				for row37 in cursor37:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row37[1],row37[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row37[0]+"\t\t",end="")
						print(row37[1],end="")
						print("\t"+row37[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row37[0]+"\t\t")
						c+=str(row37[1])
						c+=str("\t"+row37[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row37[1])
						j.append(row37[2])
						l.append(j)
			break
		if row[3]==karak:
			cursor36=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=?  or vibhakti=? and fragment=?',(vibhakti,s,karak))
			for row36 in cursor36:
				sc=str(row36[3])
				cursor35=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row36[0],row36[1],row36[2]))	
				for row35 in cursor35:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row35[1],row35[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row35[0]+"\t\t",end="")
						print(row35[1],end="")
						print("\t"+row35[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row35[0]+"\t\t")
						c+=str(row35[1])
						c+=str("\t"+row35[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row35[1])
						j.append(row35[2])
						l.append(j)
			break
		if row[4]==karak:
			cursor34=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and symbol=?',(vibhakti,s,karak))
			for row34 in cursor34:
				sc=str(row34[3])
				cursor33=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row34[0],row34[1],row34[2]))
				for row33 in curso33:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row33[1],row33[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row33[0]+"\t\t",end="")
						print(row33[1],end="")
						print("\t"+row33[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row33[0]+"\t\t")
						c+=str(row33[1])
						c+=str("\t"+row33[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row33[1])
						j.append(row33[2])
						l.append(j)
			break
		if row[5]==karak:
			cursor32=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and saha=?',(vibhakti,s,karak))
			for row32 in cursor32:
				sc=str(row34[3])
				cursor31=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row32[0],row32[1],row32[2]))
				for row31 in cursor31:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row31[1],row31[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row31[0]+"\t\t",end="")
						print(row31[1],end="")
						print("\t"+row31[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row31[0]+"\t\t")
						c+=str(row31[1])
						c+=str("\t"+row31[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row31[1])
						j.append(row31[2])
						l.append(j)
			break
		if row[6]==karak:
			cursor30=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and shashthi=?',(vibhakti,s,karak))
			for row30 in cursor30:
				sc=str(row30[3])
				cursor29=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row30[0],row30[1],row30[2]))
				for row29 in cursor29:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row29[1],row29[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row29[0]+"\t\t",end="")
						print(row29[1],end="")
						print("\t"+row29[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row29[0]+"\t\t")
						c+=str(row29[1])
						c+=str("\t"+row29[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row29[1])
						j.append(row29[2])
						l.append(j)
			break
		if row[7]==karak:
			cursor28=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and adverbs=?',(vibhakti,s,karak))
			for row28 in cursor28:
				sc=str(row28[3])
				cursor27=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row28[0],row28[1],row28[2]))
				for row27 in cursor27:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row27[1],row27[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row27[0]+"\t\t",end="")
						print(row27[1],end="")
						print("\t"+row27[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row27[0]+"\t\t")
						c+=str(row27[1])
						c+=str("\t"+row27[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row27[1])
						j.append(row27[2])
						l.append(j)
			break
		if row[8]==karak:
			cursor26=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and cause=?',(vibhakti,s,karak))
			for row26 in cursor26:
				sc=str(row26[3])
				cursor25=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row26[0],row26[1],row26[2]))
				for row25 in cursor25:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row25[1],row25[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print("\n")
						print(i,end="")
						print("\t"+sc+"\t"+row25[0]+"\t\t",end="")
						print(row25[1],end="")
						print("\t"+row25[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row25[0]+"\t\t")
						c+=str(row25[1])
						c+=str("\t"+row25[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row25[1])
						j.append(row25[2])
						l.append(j)
			break
		if row[9]==karak:
			cursor24=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and relation=?',(vibhakti,s,karak))
			for row24 in cursor24:
				sc=str(row24[3])
				cursor23=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row24[0],row24[1],row24[2]))
				for row23 in cursor23:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row23[1],row23[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+sc+"\t"+row23[0]+"\t\t",end="")
						print(row23[1],end="")
						print("\t"+row23[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row23[0]+"\t\t")
						c+=str(row23[1])
						c+=str("\t"+row23[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row23[1])
						j.append(row23[2])
						l.append(j)
			break
		if row[10]==karak:
			cursor22=conn.execute('select distinct sid,chunkid,filename,word from Tword where vibhakti=? or vibhakti=? and other=?',(vibhakti,s,karak))
			for row22 in cursor22:
				sc=str(row22[3])
				cursor21=conn.execute('select distinct words,sid,filename from Tchunk where sid=? and chunkid=? and filename=?',(row22[0],row22[1],row22[2]))
				for row21 in cursor21:
					curso39=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row21[1],row21[2]))
					for ro39 in curso39:
						flag=1
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+sc+"\t"+row21[0]+"\t\t",end="")
						print(row21[1],end="")
						print("\t"+row21[2]+"\t\t"+ro39[0]+"\n")
						c=str(i)
						c+=str("\t"+sc+"\t"+row21[0]+"\t\t")
						c+=str(row21[1])
						c+=str("\t"+row21[2]+"\t\t"+ro39[0]+"\n")
						f.write(c)
						c=''
						j.append(row21[1])
						j.append(row21[2])
						l.append(j)
			break	
	if flag==0:
		print('No result found')
	if flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press y for yes and  n for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation1(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
		'''ch=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		i=0
		#st='Sentence_ModifyChunk'
		#st+=str(vibhakti+karak)
		if ch=='y':
			st=input('Enter name of output file: ')
			sent(st,j,l)'''
def karaksentence(vibhakti,verb):
	flag=0
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	l3=[]
	c='0_'
	c+=str(vibhakti)
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	#name='karaksentence_'
	name=input('Enter name of output file: ')
	'''cho=input('Do you want to search for '+vibhakti+' and '+c+' both forms or single '+vibhakti+' form?(Press "s" for single and "b" for both) ')
	if cho=='s':
		cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other from Tword where vibhakti=? and root=? or word=? and category="v" group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,verb,verb))
		for row41 in cursor91:
			if row41[9]!='NULL':
				l1.append(row41[9])
			elif row41[8]!='NULL':
				l1.append(row41[8])
			elif row41[7]!='NULL':
				l1.append(row41[7])
			elif row41[6]!='NULL':
				l1.append(row41[6])
			elif row41[5]!='NULL':
				l1.append(row41[5])
			elif row41[4]!='NULL':
				l1.append(row41[4])
			elif row41[5]!='NULL':
				l1.append(row41[3])
			elif row41[2]!='NULL':
				l1.append(row41[2])
			elif row41[1]!='NULL':
				l1.append(row41[1])
			elif row41[0]!='NULL':
				l1.append(row41[0])
		print(l1)
		karak=input('Enter karak: ')
		#name+=str(vibhakti+karak+verb)
		f=open(os.path.join(path,name),'w')
		s="Sid\tSentence\t\tFilename\n"
		f.write(s)
		s=''
		z=input('Do you want to see all sentences or some sentences?(press "a" for all and "s" for some) ')
		cursor=conn.execute('select root,vibhakti,karak,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,modifier from Tword where vibhakti=? and root=? or word=? and category="v"',(vibhakti,verb,verb))
		for row in cursor:	
			if vibhakti==row[1]:
				if karak==row[2]:
					if z=='a':
						cursor1=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.karak=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row1 in cursor1:
							flag=1
							l2=[]
							l2.append(row1[0])
							l2.append(row1[2])
							l2.append(row1[1])
							l3.append(l2)
					elif z=='s':
						print('hello')
						m=int(input('How many sentence you want to see? '))
						curso1=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 joi     n Tword t2 where t2.vibhakti=? and t2.karak=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro1 in curso1:
							flag=1
							l2=[]
							l2.append(ro1[0])
							l2.append(ro1[2])
							l2.append(ro1[1])
							l3.append(l2)
				elif karak==row[11]:
					if z=='a':
						cursor10=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.modifier=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row10 in cursor10:
							flag=1
							l2=[]
							l2.append(row10[0])
							l2.append(row10[2])
							l2.append(row10[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso10=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.modifier=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro10 in curso10:
							flag=1
							l2=[]
							l2.append(ro10[0])
							l2.append(ro10[2])
							l2.append(ro10[1])
							l3.append(l2)
				elif karak==row[3]:
					if z=='a':
						cursor2=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.fragment=? and t2.root=?  or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb)) 
						for row2 in cursor2:
							flag=1
							l2=[]
							l2.append(row2[0])
							l2.append(row2[2])
							l2.append(row2[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso2=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.fragment=? and t2.root=?  or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro2 in curso2:
							flag=1
							l2=[]   
							l2.append(ro2[0])
							l2.append(ro2[2])
							l2.append(ro2[1])
							l3.append(l2)
				elif karak==row[4]:
					if z=='a':
						cursor3=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.symbol=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row3 in cursor3:
							flag=1
							l2=[]
							l2.append(row3[0])
							l2.append(row3[2])
							l2.append(row3[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso3=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.symbol=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro3 in curso3:
							flag=1
							l2=[]
							l2.append(ro3[0])
							l2.append(ro3[2])
							l2.append(ro3[1])
							l3.append(l2)
				elif karak==row[5]:
					if z=='a':
						cursor4=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.saha=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row4 in cursor4:
							flag=1
							l2=[]
							l2.append(row4[0])
							l2.append(row4[2])
							l2.append(row4[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso4=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.saha=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro4 in curso4:
							flag=1
							l2=[]
							l2.append(ro4[0])
							l2.append(ro4[2])
							l2.append(ro4[1])
							l3.append(l2)
				elif karak==row[6]:
					if z=='a':
						cursor5=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.shashthi=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))	
						for row5 in cursor5:
							flag=1
							l2=[]
							l2.append(row5[0])
							l2.append(row5[2])
							l2.append(row5[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso5=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.shashthi=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro5 in curso5:
							flag=1
							l2=[]
							l2.append(ro5[0])
							l2.append(ro5[2])
							l2.append(ro5[1])
							l3.append(l2)
				elif karak==row[7]:
					if z=='a':
						cursor6=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.adverbs=? and t2.root=?  or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))						
						for row6 in cursor6:
							flag=1
							l2=[]
							l2.append(row6[0])
							l2.append(row6[2])
							l2.append(row6[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso6=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.adverbs=? and t2.root=?  or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro6 in curso6:
							flag=1
							l2=[]
							l2.append(ro6[0])
							l2.append(ro6[2])
							l2.append(ro6[1])
							l3.append(l2)
				elif karak==row[8]:
					if z=='a':
						cursor7=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.cause=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row7 in cursor7:
							flag=1
							l2=[]
							l2.append(row7[0])
							l2.append(row7[2])
							l2.append(row7[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso7=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.cause=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro7 in curso7:
							flag=1
							l2=[]
							l2.append(ro7[0])
							l2.append(ro7[2])
							l2.append(ro7[1])
							l3.append(l2)
				elif karak==row[9]:
					if z=='a':
						cursor8=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.relation=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row8 in cursor8:
							flag=1
							l2=[]
							l2.append(row8[0])
							l2.append(row8[2])
							l2.append(row8[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso8=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.relation=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro8 in curso8:
							flag=1
							l2=[]
							l2.append(ro8[0])
							l2.append(ro8[2])
							l2.append(ro8[1])
							l3.append(l2)
				elif karak==row[10]:
					if z=='a':
						cursor9=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.other=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename',(vibhakti,karak,verb,verb))
						for row9 in cursor9:
							flag=1
							l2=[]
							l2.append(row9[0])
							l2.append(row9[2])
							l2.append(row9[1])
							l3.append(l2)
					elif z=='s':
						m=int(input('How many sentence you want to see? '))
						curso9=conn.execute('select distinct t1.sid,t1.sentence,t1.filename from Tsentence t1 join Tword t2 where t2.vibhakti=? and t2.other=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,karak,verb,verb,m))
						for ro9 in curso9:
							flag=1
							l2=[]
							l2.append(ro9[0])
							l2.append(ro9[2])
							l2.append(ro9[1])
							l3.append(l2)
			print("SNo.\tSid\tFilename\t\t\tSentence")
			for l2 in l3:
				j=[]    
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(l2[0],end="")
				print("\t"+l2[1]+"\t"+l2[2])
				s+=str(i)
				s+=str("\t")
				s+=str(l2[0])
				s+=str("\t"+l2[1]+"\t\t"+l2[2]+"\n")
				f.write(s)
				s=''
				j.append(l2[0])
				j.append(l2[1])
				l.append(j)
			break
	elif cho=='b':'''
	l4=[]
	l5=[]
	l6=[]
	cursor91=conn.execute('select karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,count(*) from Tword where vibhakti=? or vibhakti=? and root=? or word=? and category="v" group by karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other',(vibhakti,c,verb,verb))
	for row41 in cursor91:
		l1=[]
		if row41[9]!='NULL':
			l1.append(row41[9])
		elif row41[8]!='NULL':
			l1.append(row41[8])
		elif row41[7]!='NULL':
			l1.append(row41[7])
		elif row41[6]!='NULL':
			l1.append(row41[6])
		elif row41[5]!='NULL':
			l1.append(row41[5])
		elif row41[4]!='NULL':
			l1.append(row41[4])
		elif row41[5]!='NULL':
			l1.append(row41[3])
		elif row41[2]!='NULL':
			l1.append(row41[2])
		elif row41[1]!='NULL':
			l1.append(row41[1])
		elif row41[0]!='NULL':
			l1.append(row41[0])
		l1.append(row41[10])
		l1.append(row41[11])
		l6.append(l1)
	for l1 in l6:
		print(l1,end="")
	karak=input('\nEnter karak: ')
	#name+=str(vibhakti+c+karak+verb)
	f=open(os.path.join(path,name),'w')
	s="SNo.\tword\troot_word\tSid\tFilename\tSentence\n"
	f.write(s)
	s=''
	z=input('Do you want to see all sentences or some sentences?(press "a" for all and "s" for some) ')
	print("SNo.\tword\troot_word\tSid\tFilename\t\t\tSentence")
	cursor=conn.execute('select root,vibhakti,karak,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,modifier from Tword where vibhakti=? or vibhakti=? and root=? or word=? and category="v"',(vibhakti,c,verb,verb))
	for row in cursor:
		if vibhakti==row[1]:
			if karak==row[2]:
				if z=='a':
					cursor11=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and karak=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row11 in cursor11:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row11[0],row11[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row11[2])
							l2.append(row11[3])
							l2.append(row11[0])
							l2.append(row11[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(l2[0],end="")
						print("\t"+l2[1]+"\t"+l2[2]+"\n")
						s+=str(i)
						s+=str("\t")
						s+=str(l2[0])
						s+=str("\t"+l2[1]+"\t\t"+l2[2]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs11=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.karak=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,c,karak,verb,verb,m))
					for r1 in curs11:
						flag=1
						l2=[]
						l2.append(r1[3])
						l2.append(r1[4])
						l2.append(r1[0])
						l2.append(r1[2])
						l2.append(r1[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(l2[0],end="")
						print("\t"+l2[1]+"\t"+l2[2]+"\n")
						s+=str(i)
						s+=str("\t")
						s+=str(l2[0])
						s+=str("\t"+l2[1]+"\t\t"+l2[2]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[11]:
				if z=='a':
					cursor12=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and modifier=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row12 in cursor12:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',     (row12[0],row12[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row12[2])
							l2.append(row12[3])
							l2.append(row12[0])
							l2.append(row12[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(l2[0],end="")
						print("\t"+l2[1]+"\t"+l2[2]+"\n")
						s+=str(i)
						s+=str("\t")
						s+=str(l2[0])
						s+=str("\t"+l2[1]+"\t\t"+l2[2]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs12=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.modifier=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,s,karak,verb,verb,m))
					for r12 in curs12:
						flag=1
						l2=[]
						l2.append(r12[3])
						l2.append(r12[4])
						l2.append(r12[0])
						l2.append(r12[2])
						l2.append(r12[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(l2[0],end="")
						print("\t"+l2[1]+"\t"+l2[2]+"\n")
						s+=str(i)
						s+=str("\t")
						s+=str(l2[0])
						s+=str("\t"+l2[1]+"\t\t"+l2[2]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[3]:
				if z=='a':
					cursor13=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and fragment=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,s,karak,verb,verb))
					for row13 in cursor13:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row13[0],row13[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row13[2])
							l2.append(row13[3])
							l2.append(row13[0])
							l2.append(row13[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs13=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.fragment=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,c,karak,verb,verb,m))
					for r13 in curs13:
						flag=1
						l2=[]
						l2.append(r13[3])
						l2.append(r13[4])
						l2.append(r13[0])
						l2.append(r13[2])
						l2.append(r13[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t",end="")
						print(l2[0],end="")
						print("\t"+l2[1]+"\t"+l2[2]+"\n")
						s+=str(i)
						s+=str("\t")
						s+=str(l2[0])
						s+=str("\t"+l2[1]+"\t\t"+l2[2]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[4]:
				if z=='a':
					cursor14=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and symbol=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row14 in cursor14:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row14[0],row14[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row14[2])
							l2.append(row14[3])
							l2.append(row14[0])
							l2.append(row14[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs14=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.symbol=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,c,karak,verb,verb,m))
					for r14 in curs14:
						flag=1
						l2=[]
						l2.append(r14[3])
						l2.append(r14[4])
						l2.append(r14[0])
						l2.append(r14[2])
						l2.append(r14[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break	
			elif karak==row[5]:
				if z=='a':
					cursor15=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and saha=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row15 in cursor15:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row15[0],row15[1]))
					for ro13 in curso13:
						flag=1
						l2=[]
						l2.append(row15[2])
						l2.append(row15[3])
						l2.append(row15[0])
						l2.append(row15[1])
						l2.append(ro13[0])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break	
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs15=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.saha=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,c,karak,verb,verb,m))
					for r15 in curs15:
						flag=1
						l2=[]
						l2.append(r15[3])
						l2.append(r15[4])
						l2.append(r15[0])
						l2.append(r15[2])
						l2.append(r15[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[6]:
				if z=='a':	
					cursor16=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and shashthi=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))   
					for row16 in cursor16:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row16[0],row16[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row15[2])
							l2.append(row13[3])
							l2.append(row13[0])
							l2.append(row13[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs16=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.shashthi=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,c,karak,verb,verb,m))
					for r16 in curs16:
						flag=1
						l2=[]
						l2.append(r16[3])
						l2.append(r16[4])
						l2.append(r16[0])
						l2.append(r16[2])
						l2.append(r16[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[7]:
				if z=='a':
					cursor17=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and adverbs=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))    
					for row17 in cursor17:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row17[0],row17[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row17[2])
							l2.append(row17[3])
							l2.append(row17[0])
							l2.append(row17[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs17=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.adverbs=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,c,karak,verb,verb,m))
					for r17 in curs17:
						flag=1
						l2=[]
						l2.append(r17[3])
						l2.append(r17[4])
						l2.append(r17[0])
						l2.append(r17[2])
						l2.append(r17[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[8]:
				if z=='a':	
					cursor18=conn.execute('select distinct sid,filename,word,root from Tword  where vibhakti=? or vibhakti=? and cause=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row18 in cursor18:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row18[0],row18[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row18[2])
							l2.append(row18[3])
							l2.append(row18[0])
							l2.append(row18[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs18=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.cause=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,s,karak,verb,verb,m))
					for r18 in curs18:
						flag=1
						l2=[]
						l2.append(r18[3])
						l2.append(r18[4])
						l2.append(r18[0])
						l2.append(r18[2])
						l2.append(r18[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''    
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[9]:
				if z=='a':
					cursor19=conn.execute('select distinct sid,filename,word,root from Tword  where vibhakti=? or vibhakti=? and relation=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row19 in cursor19:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row19[0],row19[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row19[2])
							l2.append(row19[3])
							l2.append(row19[0])
							l2.append(row19[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs19=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.relation=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,s,karak,verb,verb,m))
					for r19 in curs19:
						flag=1
						l2=[]
						l2.append(r19[3])
						l2.append(r19[4])
						l2.append(r19[0])
						l2.append(r19[2])
						l2.append(r19[1])
						l3.append(l2)	
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
			elif karak==row[10]:
				if z=='a':
					cursor20=conn.execute('select distinct sid,filename,word,root from Tword where vibhakti=? or vibhakti=? and other=? and root=? or word=? and category="v" group by sid,filename',(vibhakti,c,karak,verb,verb))
					for row20 in cursor20:
						curso13=conn.execute('select distinct sentence from Tsentence where sid=? and filename=?',(row20[0],row20[1]))
						for ro13 in curso13:
							flag=1
							l2=[]
							l2.append(row20[2])
							l2.append(row20[3])
							l2.append(row20[0])
							l2.append(row20[1])
							l2.append(ro13[0])
							l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")	
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
				elif z=='s':
					m=int(input('How many sentences you want to see? '))
					curs20=conn.execute('select distinct t1.sid,t1.sentence,t1.filename,t2.word,t2.root from Tsentence t1 join Tword t2 where t2.vibhakti=? or t2.vibhakti=? and t2.other=? and t2.root=? or t2.word=? and t2.category="v" and t1.sid==t2.sid and t1.filename==t2.filename limit ?',(vibhakti,s,karak,verb,verb,m))
					for r20 in curs20:
						flag=1
						l2=[]
						l2.append(r20[3])
						l2.append(r20[4])
						l2.append(r20[0])
						l2.append(r20[2])
						l2.append(r20[1])
						l3.append(l2)
					for l2 in l3:
						j=[]
						i=i+1
						print(i,end="")
						print("\t"+l2[0]+"\t"+l2[1]+"\t",end="")
						print(l2[2],end="")
						print("\t"+l2[3]+"\t"+l2[4]+"\n")
						s+=str(i)
						s+=str("\t"+l2[0]+"\t"+l2[1]+"\t")
						s+=str(l2[2])
						s+=str("\t"+l2[3]+"\t\t"+l2[4]+"\n")
						f.write(s)
						s=''
						j.append(l2[2])
						j.append(l2[3])
						l.append(j)
					break
	if flag==0:
		print('No result found')
	if flag==1:
		choice=input("Do you want to see relation between words of sentence?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			#na='Relation_KarakSentence'
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press y for yes and n for no) ')
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				relation(na,si,fi)
			elif choic=='n':
				relation(na,j,l)
def query(q):
	flag=0
	i=0
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	#name='Query'
	name=input('Enter name of output file: ')
	f=open(os.path.join(path,name),'w')
	s=''
	cursor=conn.execute(q)
	for row in cursor:
		flag=1
		i=i+1
		print(i,end="")
		print("\t",end="")
		print(row)
		s+=str(i)
		s+=str("\t")
		s+=str(row)
		s+=str("\n")
		f.write(s)
		s=''
	if flag==0:
		print('No result found')
def relation(name,list1,list2):
	flag=0
	j=[]
	l=[]
	for list1 in list2:
		cursor=conn.execute('select word,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,wrelation,sid,filename,connection from Tword where sid=? and filename=?',(list1[0],list1[1]))
		for row in cursor:
			flag=1
			if row[1]!='NULL':
				#print(row[0]+" "+row[1]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[1])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[2]!='NULL':
				#print(row[0]+" "+row[2]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[2])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[3]!='NULL':
				#print(row[0]+" "+row[3]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[3])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[4]!='NULL':
				#print(row[0]+" "+row[4]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[4])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[5]!='NULL':
				#print(row[0]+" "+row[5]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[5])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[6]!='NULL':
				#print(row[0]+" "+row[6]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[6])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[7]!='NULL':
				#print(row[0]+" "+row[7]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[7])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[8]!='NULL':
				#print(row[0]+" "+row[8]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[8])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[9]!='NULL':
				#print(row[0]+" "+row[9]+":"+row[12]+" "+row[11])
				j=[]
				j.append(row[9])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)	
			elif row[10]!='NULL':
				#print(row[0]+" "+row[10]+":"+row[12]+" "+row[11])
				j=[]	
				j.append(row[10])
				#j.append(row[13])
				j.append(row[12])
				j.append(row[11])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
			elif row[15]=='main':
				#print(row[0]+" NULL":"+row[12]+" "+row[11])
				j=[]
				a='NULL'
				b='NULL'
				j.append(a)
				j.append(b)
				#j.append(row[12])
				j.append(row[15])
				j.append(row[0])
				j.append(row[13])
				j.append(row[14])
				l.append(j)
	if flag==0:
		print('No result found')
	elif flag==1:
		o=getpass.getuser()
		path='/home/'+o+'/Treebank_Output'
		if not os.path.exists(path):
			os.makedirs(path)
		f=open(os.path.join(path,name),'w')
		s=''
		z=input('Do you want to see word relation of all sentence or some sentence?(press "a" for all and "s" for some) ')
		if z=='a':
			for list1 in list2:
				cursor1=conn.execute('select sid,sentence,filename from Tsentence where sid=? and filename=?',(list1[0],list1[1]))
				for row1 in cursor1:
					print(row1[0],end="")
					print("\t"+row1[1]+"\t"+row1[2])
					s+=str(row1[0])
					s+=str("\t"+row1[1]+"\t"+row1[2]+"\n\n")
					f.write(s)
					s=''
				for j in l:
					if j[4]==list1[0]:
						if j[5]==list1[1]:
							print("["+j[3]+"\t"+j[0],end="")
							#print(j[1],end="")
							print(":"+j[1]+"\t"+j[2]+"]",end="")
							s+=str("["+j[3]+"\t"+j[0]+":")
							s+=str(j[1])
							#s+=str(":")
							#s+=str(j[2])
							s+=str("\t"+j[2]+"]"+"\n")
							f.write(s)
							s=''
				print(" \n\n")
		elif z=='s':
			m=int(input('How many sentences you want to see? '))
			k=0
			while k<m:
				curso1=conn.execute('select sid,sentence,filename from Tsentence where sid=? and filename=? ',(list2[k][0],list2[k][1]))
				for ro1 in curso1:
					print(ro1[0],end="")
					print("\t"+ro1[1]+"\t"+ro1[2])
					s+=str(ro1[0])
					s+=str("\t"+ro1[1]+"\t"+ro1[2]+"\n")
					f.write(s)
					s=''
				for j in l:
					if j[5]==list2[k][0]:
						if j[6]==list2[k][1]:
							print("["+j[3]+"\t"+j[0],end="")
							#print(j[1],end="")
							print(":"+j[1]+"\t"+j[2]+"]",end="")
							s+=str("["+j[3]+"\t"+j[0]+":")
							s+=str(j[1])
							#s+=str(":")
							#s+=str(j[2])
							s+=str("\t"+j[2]+"]"+"\n")
							f.write(s)
							s=''
				print(" \n\n")
				k=k+1
def karak(vibhakti,verb):
	i=0
	j=[]
	l=[]
	l1=[]
	l2=[]
	flag=0
	c='0_'
	c+=str(vibhakti)
	l1=[]
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	#name='karak_'
	name=input('Enter name of output file: ')
	'''cho=input("Do you want to see result for "+vibhakti+" and "+c+" both forms or for single "+vibhakti+" form?(Press 's' for "+vibhakti+" and 'b' for both form) ")
	if cho=='b':''' 
	#name+=str(vibhakti+c+verb)
	f=open(os.path.join(path,name),'w')
	s="SNo\tOccurance\t\tkarak\tName\n"
	f.write(s)
	s=''
	print("SNo\tOccurance\t\tkarak\tName")		
	cursor=conn.execute('select distinct sid,filename,count(*),karak,rname from Tword where vibhakti=? or vibhakti=? and root=? and category="v" group by karak',(vibhakti,c,verb))
	cursor1=conn.execute('select distinct sid,filename,count(*),modifier,rname from Tword where vibhakti=?  or vibhakti=? and root=? and category="v" group by modifier',(vibhakti,c,verb))
	cursor2=conn.execute('select distinct sid,filename,count(*),fragment,rname from Tword where vibhakti=? or vibhakti=? and root=? and category="v" group by fragment',(vibhakti,c,verb))
	cursor3=conn.execute('select distinct sid,filename,count(*),saha,rname from Tword where vibhakti=? or vibhakti=? and root=? and category="v" group by saha',(vibhakti,c,verb))
	cursor4=conn.execute('select distinct sid,filename,count(*),shashthi,rname from Tword where vibhakti=?  or vibhakti=? and root=? and category="v" group by shashthi',(vibhakti,c,verb))
	cursor5=conn.execute('select distinct sid,filename,count(*),adverbs,rname from Tword where vibhakti=?  or vibhakti=? and root=? and category="v" group by adverbs',(vibhakti,c,verb))
	cursor6=conn.execute('select distinct sid,filename,count(*),cause,rname from Tword where vibhakti=? or vibhakti=? and root=? and category="v" group by cause',(vibhakti,c,verb))
	cursor7=conn.execute('select distinct sid,filename,count(*),relation,rname from Tword where vibhakti=?  or vibhakti=? and root=? and category="v" group by relation',(vibhakti,c,verb))
	cursor8=conn.execute('select distinct sid,filename,count(*),other,rname from Tword where vibhakti=? or vibhakti=? and root=? and category="v" group by other',(vibhakti,c,verb))
	cursor9=conn.execute('select distinct sid,filename,count(*),symbol,rname from Tword where vibhakti=?  or vibhakti=? and root=? and category="v" group by symbol',(vibhakti,c,verb))
	for row in cursor:
		if row[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row[2],end="")
			print("\t\t"+row[3]+"\t"+row[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row[2])
			s+=str("\t\t"+row[3]+"\t"+row[4]+"\n")
			f.write(s)
			s=''
			j.append(row[0])
			j.append(row[1])
			l.append(j)
	for row1 in cursor1:
		if row1[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row1[2],end="")
			print("\t\t"+row1[3]+"\t"+row1[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row1[2])
			s+=str("\t\t"+row1[3]+"\t"+row1[4]+"\n")
			f.write(s)
			s=''
			j.append(row1[0])
			j.append(row1[1])
			l.append(j)
	for row2 in cursor2:
		if row2[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row2[2],end="")
			print("\t\t"+row2[3]+"\t"+row2[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row2[2])
			s+=str("\t\t"+row2[3]+"\t"+row2[4]+"\n")
			f.write(s)
			s=''
			j.append(row2[0])
			j.append(row2[1])
			l.append(j)
	for row3 in cursor3:
		if row3[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row3[2],end="")
			print("\t\t"+row3[3]+"\t"+row3[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row3[2])
			s+=str("\t\t"+row3[3]+"\t"+row3[4]+"\n")
			f.write(s)
			s=''
			j.append(row3[0])
			j.append(row3[1])
			l.append(j)
	for row4 in cursor4:
		if row4[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row4[2],end="")
			print("\t\t"+row4[3]+"\t"+row4[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row4[2])
			s+=str("\t\t"+row4[3]+"\t"+row4[4]+"\n")
			f.write(s)
			s=''
			j.append(row4[0])
			j.append(row4[1])
			l.append(j)
	for row5 in cursor5:
		if row5[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row5[2],end="")
			print("\t\t"+row5[3]+"\t"+row5[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row5[2])
			s+=str("\t\t"+row5[3]+"\t"+row5[4]+"\n")
			f.write(s)
			s=''
			j.append(row5[0])
			j.append(row5[1])
			l.append(j)
	for row6 in cursor6:
		if row6[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row6[2],end="")
			print("\t\t"+row6[3]+"\t"+row6[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row6[2])
			s+=str("\t\t"+row6[3]+"\t"+row6[4]+"\n")
			f.write(s)
			s=''
			j.append(row6[0])
			j.append(row6[1])
			l.append(j)
	for row7 in cursor7:
		if row7[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row7[2],end="")
			print("\t\t"+row7[3]+"\t"+row7[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row7[2])
			s+=str("\t\t"+row7[3]+"\t"+row7[4]+"\n")
			f.write(s)
			s=''
			j.append(row7[0])
			j.append(row7[1])
			l.append(j)
	for row8 in cursor8:
		if row8[3]!='NULL':
			flag=1
			j=[]
			i=i+1	
			print(i,end="")
			print("\t",end="")
			print(row8[2],end="")
			print("\t\t"+row8[3]+"\t"+row8[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row8[2])
			s+=str("\t\t"+row8[3]+"\t"+row8[4]+"\n")
			f.write(s)
			s=''
			j.append(row8[0])
			j.append(row8[1])
			l.append(j)
	for row9 in cursor9:
		if row9[3]!='NULL':
			flag=1
			j=[]
			i=i+1
			print(i,end="")
			print("\t",end="")
			print(row9[2],end="")
			print("\t\t"+row9[3]+"\t"+row9[4])
			s+=str(i)
			s+=str("\t")
			s+=str(row9[2])
			s+=str("\t\t"+row9[3]+"\t"+row9[4]+"\n")
			f.write(s)
			s=''
			j.append(row9[0])
			j.append(row9[1])
			l.append(j)
	'''if cho=='s':
		#name+=str(vibhakti+verb)
		f=open(os.path.join(path,name),'w')
		s="SNo\tOccurance\tkarak\tName\n"
		f.write(s)
		s=''
		print("SNo\tOccurance\tkarak\tName")
		cursor=conn.execute('select distinct sid,filename,count(*),karak,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by karak',(vibhakti,verb,verb))
		cursor1=conn.execute('select distinct sid,filename,count(*),modifier,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by modifier',(vibhakti,verb,verb))
		cursor2=conn.execute('select distinct sid,filename,count(*),fragment,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by fragment',(vibhakti,verb,verb))
		cursor3=conn.execute('select distinct sid,filename,count(*),saha,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by saha',(vibhakti,verb,verb))
		cursor4=conn.execute('select distinct sid,filename,count(*),shashthi,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by shashthi',(vibhakti,verb,verb))
		cursor5=conn.execute('select distinct sid,filename,count(*),adverbs,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by adverbs',(vibhakti,verb,verb))
		cursor6=conn.execute('select distinct sid,filename,count(*),cause,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by cause',(vibhakti,verb,verb))
		cursor7=conn.execute('select distinct sid,filename,count(*),relation,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by relation',(vibhakti,verb,verb))
		cursor8=conn.execute('select distinct sid,filename,count(*),other,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by other',(vibhakti,verb,verb))
		cursor9=conn.execute('select distinct sid,filename,count(*),symbol,rname from Tword where vibhakti=? and root=? or word=? and category="v" group by symbol',(vibhakti,verb,verb))
		for row in cursor:	
			if row[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row[2],end="")
				print("\t\t"+row[3]+"\t"+row[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row[2])
				s+=str("\t\t"+row[3]+"\t"+row[4]+"\n")
				f.write(s)
				s=''
				j.append(row[0])
				j.append(row[1])
				l.append(j)
		for row1 in cursor1:
			if row1[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row1[2],end="")
				print("\t\t"+row1[3]+"\t"+row1[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row1[2])
				s+=str("\t\t"+row1[3]+"\t"+row1[4]+"\n")
				f.write(s)
				s=''
				j.append(row1[0])
				j.append(row1[1])
				l.append(j)
		for row2 in cursor2:
			if row2[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row2[2],end="")
				print("\t\t"+row2[3]+"\t"+row2[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row2[2])
				s+=str("\t\t"+row2[3]+"\t"+row2[4]+"\n")
				f.write(s)
				s=''
				j.append(row2[0])
				j.append(row2[1])
				l.append(j)
		for row3 in cursor3:
			if row3[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row3[2],end="")
				print("\t\t"+row3[3]+"\t"+row3[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row3[2])
				s+=str("\t\t"+row3[3]+"\t"+row3[4]+"\n")
				f.write(s)
				s=''
				j.append(row3[0])
				j.append(row3[1])
				l.append(j)
		for row4 in cursor4:
			if row4[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row4[2],end="")
				print("\t\t"+row4[3]+"\t"+row4[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row4[2])
				s+=str("\t\t"+row4[3]+"\t"+row4[4]+"\n")
				f.write(s)
				s=''
				j.append(row4[0])
				j.append(row4[1])
				l.append(j)
		for row5 in cursor5:
			if row5[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row5[2],end="")
				print("\t\t"+row5[3]+"\t"+row5[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row5[2])
				s+=str("\t\t"+row5[3]+"\t"+row5[4]+"\n")
				f.write(s)
				s=''
				j.append(row5[0])
				j.append(row5[1])
				l.append(j)
		for row6 in cursor6:
			if row6[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row6[2],end="")
				print("\t\t"+row6[3]+"\t"+row6[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row6[2])
				s+=str("\t\t"+row6[3]+"\t"+row6[4]+"\n")
				f.write(s)
				s=''
				j.append(row6[0])
				j.append(row6[1])
				l.append(j)
		for row7 in cursor7:
			if row7[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row7[2],end="")
				print("\t\t"+row7[3]+"\t"+row7[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row7[2])
				s+=str("\t\t"+row7[3]+"\t"+row7[4]+"\n")
				f.write(s)
				s=''
				j.append(row7[0])
				j.append(row7[1])
				l.append(j)
		for row8 in cursor8:
			if row8[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row8[2],end="")
				print("\t\t"+row8[3]+"\t"+row8[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row8[2])
				s+=str("\t\t"+row8[3]+"\t"+row8[4]+"\n")
				f.write(s)
				s=''
				j.append(row8[0])
				j.append(row8[1])
				l.append(j)
		for row9 in cursor9:
			if row9[3]!='NULL':
				flag=1
				j=[]
				i=i+1
				print(i,end="")
				print("\t",end="")
				print(row9[2],end="")
				print("\t\t"+row9[3]+"\t"+row9[4])
				s+=str(i)
				s+=str("\t")
				s+=str(row9[2])
				s+=str("\t\t"+row9[3]+"\t"+row9[4]+"\n")
				f.write(s)
				s=''
				j.append(row9[0])
				j.append(row9[1])
				l.append(j)'''
	if flag==0:
		print("No result found")
	elif flag==1:
		h=[]
		m=[]
		choice=input("Do you want to see sentences?(Press 'y' for yes and 'n' for no) ")
		if choice=='y':
			k=input("Enter karak: ")
			i=0
			print("SNo.\tSid\tFilename\t\t\t\tSentence")
			path1='/home/'+o+'/Treebank_Output'
			if not os.path.exists(path1):               
				os.makedirs(path1)
			#name1='Sentence_karak_'
			#name1+=str(k+vibhakti+verb)
			name1=input('Enter name of output file: ')
			f=open(os.path.join(path1,name1),'w')
			s1="Sid\tFilename\t\t\t\t\t\tSentence\n"
			f.write(s1)
			s1=''
			cursor10=conn.execute('select  distinct sid,filename from Tword where karak=? or modifier=? or fragment=? or saha=? or shashthi=? or adverbs=? or cause=? or relation=? or other=? or symbol=? ',(k,k,k,k,k,k,k,k,k,k))
			for row10 in cursor10:
				for j in l:
					if row10[0]==j[0]:
						if row10[1]==j[1]:
							print(j[0])
							h.append(row10[0])
							h.append(row10[1])
							m.append(h)
							i=i+1
							print(i,end="")
							print("\t",end="")
							cursor60=conn.execute('select distinct sid,filename,sentence from Tsentence where sid=? and filename=? group by sentence',(j[0],j[1]))
							for row60 in cursor60:
								print(row60[0],end="")
								print("\t",end="")
								print(row60[1]+"\t\t"+row60[2])
								s1=str(row60[0])
								s1+=str("\t"+row60[1]+"\t\t"+row60[2]+"\n")
								f.write(s1)
								s1=''
							break	
		ch=input("Do you want to see relation between words?(Press 'y' for yes and 'n' for no) ")
		if ch=='y':
			#na='Relation_karak_'
			na=input('Enter name of output file: ')
			choic=input('Do you want to see relation between words of single sentence?(press y for yes and n for no) ')
			#if cho=='s':
				#na+=str(vibhakti+verb)
			if choic=='y':
				si=input('Enter sid: ')
				fi=input('Enter filename: ')
				l1.append(si)
				l1.append(fi)
				l2.append(l1)
				relation(na,l1,l2)
			elif choic=='n':
				relation(na,h,m)
			'''elif cho=='b':
				#na+=str(vibhakti+c+verb)
				if choic=='y':
					si=input('Enter sid: ')
					fi=input('Enter filename: ')
					l1.append(si)
					l1.append(fi)
					l2.append(l1)
					relation(na,l1,l2)
				elif choic=='n':
					relation(na,h,m)'''
def relation1(name,sid,filename):
	flag=0
	j=[]
	l=[]
	cursor=conn.execute('select word,karak,modifier,fragment,symbol,saha,shashthi,adverbs,cause,relation,other,rname,wrelation,sid,filename,connection from Tword where sid=? and filename=?',(sid,filename))
	for row in cursor:
		flag=1
		if row[1]!='NULL':
			#print(row[0]+" "+row[1]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[1])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[2]!='NULL':
			#print(row[0]+" "+row[2]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[2])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[3]!='NULL':
			#print(row[0]+" "+row[3]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[3])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[4]!='NULL':
			#print(row[0]+" "+row[4]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[4])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[5]!='NULL':
			#print(row[0]+" "+row[5]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[5])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[6]!='NULL':
			#print(row[0]+" "+row[6]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[6])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[7]!='NULL':
			#print(row[0]+" "+row[7]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[7])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[8]!='NULL':
			#print(row[0]+" "+row[8]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[8])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[9]!='NULL':
			#print(row[0]+" "+row[9]+":"+row[12]+" "+row[11])
			j=[]
			j.append(row[9])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)	
		elif row[10]!='NULL':
			#print(row[0]+" "+row[10]+":"+row[12]+" "+row[11])
			j=[]	
			j.append(row[10])
			#j.append(row[13])
			j.append(row[12])
			j.append(row[11])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
		elif row[15]=='main':
			#print(row[0]+" NULL":"+row[12]+" "+row[11])
			j=[]
			a='NULL'
			b='NULL'
			j.append(a)
			j.append(b)
			#j.append(row[12])
			j.append(row[15])
			j.append(row[0])
			j.append(row[13])
			j.append(row[14])
			l.append(j)
	if flag==0:
		print('No result found')
	if flag==1:
		o=getpass.getuser()
		path='/home/'+o+'/Treebank_Output'
		if not os.path.exists(path):
			os.makedirs(path)
		f=open(os.path.join(path,name),'w')
		s=''
		cursor1=conn.execute('select sid,sentence,filename from Tsentence where sid=? and filename=?',(sid,filename))
		for row1 in cursor1:
			print(row1[0],end="")
			print("\t"+row1[1]+"\t"+row1[2])
			s+=str(row1[0])
			s+=str("\t"+row1[1]+"\t"+row1[2]+"\n\n")
			f.write(s)
			s=''
		for j in l:
			print("["+j[3]+"\t"+j[0],end="")
			#print(j[1],end="")
			print(":"+j[1]+"\t"+j[2]+"]",end="")
			s+=str("["+j[3]+"\t"+j[0]+":")
			s+=str(j[1])
			#s+=str(":")
			#s+=str(j[2])
			s+=str("\t"+j[2]+"]"+"\n")
			f.write(s)
			s=''
		print(" \n\n")
def sentence2(s1):
	j=[]
	k=[]
	name=input('Enter name of file: ')
	o=getpass.getuser()
	path='/home/'+o+'/Treebank_Output'
	if not os.path.exists(path):
		os.makedirs(path)
	f=open(os.path.join(path,name),'w')
	s="SNo\tsid\t\tfilename\t\t\t\tsentence\n"
	f.write(s)
	print(s+'\n')
	s=''
	#s2=str(s1)
	i=0
	cursor=conn.execute('select sid,filename,sentence from Tsentence where sentence like ?',('%'+s1+'%',))
	for row in cursor:
		i=i+1	
		print(i,end="")
		print('\t',end="")
		print(row[0],end="")
		print('\t'+row[1]+'\t'+row[2]+'\n')
		s=str(i)
		s+=str('\t')
		s+=str(row[0])
		s+=str('\t'+row[1]+'\t'+row[2]+'\n')
		f.write(s)
		j=[]
		j.append(row[0])
		j.append(row[1])
		k.append(j)
		s=''
	z=input('Do you want to see relation between words of sentence?(press "y" for yes and "n" for no) ')
	if z=='y':
		na=input('Enter name of output file: ')
		choic=input('Do you want to see relation between words of single sentence?(press "y" for yes and "n" for no) ')
		if choic=='y':
			si=input('Enter sid: ')
			fi=input('Enter filename: ')
			relation1(na,si,fi)
		elif choic=='n':
			relation(na,j,k)	


