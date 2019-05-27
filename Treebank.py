# author:- Bhavana Saraswat M.Tech Banasthali University 2016-2017
import Modules
i=1
print("\t Select option by number given below:\n\t1:- To obtain vibhakti and it corresponding karak-lists.\n\t2:- To obtain sentences corresponding to vibhakti and karak.\n\t3:- To extract words of given POS or category and karak having relation with verb.\n\t4:- To extract vibhakti corresponding to given POS or category.\n\t5:- To extract verb (without pof) corresponding to given vibhakti and karak.\n\t6:- To extract modifierchunk.\n\t7:- To obtain list of sentences which contains a specific word.\n\t8:- To extract pof-verb corresponding to given vibhakti and karak.\n\t9:-  To extract chunk of given vibhakti and karak relation with chunk.\n\t10:- To extract sentences corresponding to given vibhakti and karak and verb.\n\t11:- To extract karak with respect to vibhakti and verb.\n\t12:- To generate a new query.\n\t13:- To extract sentence contain given words\n\t14:- To extract TAM information of finite verb.\n")  
ch=input("Enter your choice: ")
while i==1:
	if ch=='1':
		vibhakti=input("Enter vibhakti: ")
		Modules.vibh(vibhakti);
	elif ch=='2':
		vibhakti=input("Enter vibhakti: ")
		Modules.vibh(vibhakti);
	elif ch=='3':
		pos=input("Enter POS or Category of word: ")
		Modules.category(pos);
	elif ch=='4':
		category=input("Enter Category or POS: ")
		Modules.vibhakti(category);
	elif ch=='5':
		Vibhakti=input("Enter vibhakti: ")
		#Karak=input("Enter karak: ")
		Modules.verb(Vibhakti);
	elif ch=='6':
		Modifier=input("Enter modifier: ")
		Modules.modify(Modifier);
	elif ch=='7':
		word=input("Enter word: ")
		Modules.Word(word);
	elif ch=='8':
		vibhakti=input("Enter vibhakti: ")
		#karak=input("Enter karak: ")
		Modules.pofverb(vibhakti);
	elif ch=='9':
		vibhakti=input("Enter vibhakti: ")
		#karak=input("Enter karak: ")
		Modules.modifyvibhakti(vibhakti);
	elif ch=='10':
		vibhakti=input("Enter vibhakti: ")
		#karak=input("Enter karak: ")
		verb=input("Enter verb: ")
		Modules.karaksentence(vibhakti,verb);
	elif ch=='11':
		vibhakti=input("Enter vibhakti: ")
		verb=input("Enter verb: ")
		Modules.karak(vibhakti,verb)
	elif ch=='12':
		q=input('Enter your query: ')
		Modules.query(q);
	elif ch=='13':
		s=input('Enter words: ')
		Modules.sentence2(s);
	elif ch=='14':
		Modules.finite_verb();
	elif ch<'0' or ch=='0' or ch>'15':
		print("You give wrong choice") 
	choice=input("do you want to continue(press 'y' for yes and 'n' for no): ")
	if choice=='y':
		print("\t Select option by number given below:\n\t1:- To obtain vibhakti and it corresponding karak-lists.\n\t2:- To obtain sentences corresponding to vibhakti and karak.\n\t3:- To extract words of given POS or category and karak having relation with verb.\n\t4:- To extract vibhakti corresponding to given POS or category.\n\t5:- To extract verb (without pof) corresponding to given vibhakti and karak.\n\t6:- To extract modifierchunk.\n\t7:- To obtain list of sentences which contains a specific word.\n\t8:- To extract pof-verb corresponding to given vibhakti and karak.\n\t9:-  To extract chunk of given vibhakti and karak relation with chunk.\n\t10:- To extract sentences corresponding to given vibhakti and karak and verb.\n\t11:- To extract karak with respect to vibhakti and verb.\n\t12:- To generate a new query.\n\t13:- To extract sentence contain given words\n\t14:- To extract TAM information of finite verb.\n")
		ch=input("Enter the desired number: ")
	if choice=='n':
		i=i+4
