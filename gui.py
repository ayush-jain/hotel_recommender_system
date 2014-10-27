from Tkinter import *
import tkMessageBox
import tfidf
import collab
top = Tk()
top.title("Hotel Recommender System")

def addInfo():
	a=E6.get()
	#print a 
	#tkMessageBox.showinfo( 'Successfully Added ', a)
	if(a=="TestUser"):
		f=open("input","a")
		name="name:" + E3.get()
		location="location: " + E4.get()
		date = "date: "+ E5.get()
		content="content: "+text.get("1.0",END).splitlines()[0]
		f.write("\n\n")
		f.write(name+"\n")
		f.write(location+"\n")
		f.write(date+"\n")
		f.write(content)
	else:
		f=open("Collaborativeinput.txt","a")
		f.write('\n')
		#no=E1.get()
		name=E3.get()
		l=E4.get().split(',')
		r=E2.get()
		f.write(str(a)+" "+name+" "+l[0]+" "+l[1]+" "+r)

	tkMessageBox.showinfo( "Successfully Added ", "Exit for completion")
	#lines =text.get("1.0",END).splitlines()[0]
	#print (lines)


def getreco():
	#tkMessageBox.showinfo( "Hello Python", "Hello World")	
	a=E6.get()
	txt="\n"
	txt1="\n"
	if(a=="TestUser"):
		l=E4.get().split(',')
		no=int(E1.get())
		res=tfidf.get_results(l[0],no)
		for each in res:
			txt=txt+each[0]+"\n"
		tkMessageBox.showinfo( "Content Based Filtering : Top Recommendations", txt)
	else:
		no=int(E1.get())
		res=collab.get_collab(a,no)
		for each in res[0]:
			txt=txt + each[1]+"\n"
		for each in res[1]:
			txt1=txt1+each[1] +"\n"	
		tkMessageBox.showinfo( "Collaborative Based Filtering : Top Recommendations", txt + "\n"+txt1)	


f=Frame(top)
L1 = Label(f, text=" UserName ")
L1.pack( side = LEFT)
E1 = Entry(f, bd =5)
E1.pack(side = RIGHT)
L2 = Label(f, text=" Date ")
L2.pack( side = LEFT)
E2 = Entry(f, bd =5)
E2.pack(side = RIGHT)
L3 = Label(f, text=" Location ")
L3.pack( side = LEFT)
E3 = Entry(f, bd =5)
E3.pack(side = RIGHT)
L4 = Label(f, text=" HotelName ")
L4.pack( side = LEFT)
E4 = Entry(f, bd =5)
E4.pack(side = RIGHT)
L5 = Label(f, text=" Rating ")
L5.pack( side = LEFT)
E5 = Entry(f, bd =5)
E5.pack(side = RIGHT)
L6 = Label(f, text="No. of Reco")
L6.pack(side=LEFT)
E6 = Entry(f, bd =5)
E6.pack(side = RIGHT)
f.pack(side=TOP)
f1=Frame(top)
L6 = Label(f1, text="AddReview ")
L6.pack( side = TOP)
text=Text(f1)
text.pack(side=BOTTOM)
f1.pack()
f2=Frame(top)
B1 = Button(f2, text ="Add_Review", command = addInfo)
B1.pack(side=LEFT)
B2 = Button(f2, text ="Get_Recommendation", command = getreco)
B2.pack(side=RIGHT)
f2.pack(side=BOTTOM)



top.mainloop()