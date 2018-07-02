from tkinter import *
from PIL import ImageTk
import random
res=0


root = Tk()
root.geometry("230x180")
root.resizable(width=False, height=False)
ImageSt = ImageTk.PhotoImage(file="stone.png")
ImageSh = ImageTk.PhotoImage(file="shear.png")
ImageP = ImageTk.PhotoImage(file="paper.png")
ImageW = ImageTk.PhotoImage(file="win.png")
ImageL = ImageTk.PhotoImage(file="lose.png")
ImageT = ImageTk.PhotoImage(file="tie.png")
def randomStep(fir):
	res = 0
	r = random.randint(0,2)
	knb = {0:'stone',1:'paper',2:'shear'}
	sec= knb[r]
	if r == 0 :
		secL.config(image=ImageSt)
	elif r == 1 :
		secL.config(image=ImageP)
	elif r == 2 :
		secL.config(image=ImageSh)
	if fir == 'st' and sec == 'paper':
	    res = 2
	elif fir == 'st' and sec == 'stone':
		res = 0
	elif fir == 'st' and sec == 'shear':
		res = 1
	elif fir == 'p' and sec == 'paper':
		res = 0
	elif fir == 'p' and sec == 'shear':
		res = 2
	elif fir == 'p' and sec == 'stone':
		res = 1
	elif fir == 'sh' and sec == 'shear':
		res = 0
	elif fir == 'sh' and sec == 'paper':
		res = 1
	elif fir == 'sh' and sec == 'stone':
		res = 2
	if res == 0 :
		secRes.config(image=ImageT )
	elif res == 2 :
		secRes.config(image=ImageL )
	elif res == 1 :
		secRes.config(image=ImageW )
def randomStepSh(ev):
	fir='sh'
	randomStep(fir);
	pass
def randomStepP(ev):
	fir='p'
	randomStep(fir);
	pass
def randomStepSt(ev):
	fir='st'
	randomStep(fir);
	pass

#Button(root,image=Image,command=lambda:print('+1 Coin')).pack()
secL = Label(root)
secL.place(x = 76,y=0)
secRes = Label(root)
secRes.place(x=76,y=80)
sh = Button(root,image=ImageSh)
sh.bind("<Button-1>",randomStepSh )
sh.place(x=0,y=100)
st = Button(root,image=ImageSt)
st.bind("<Button-1>",randomStepSt )
st.place(x=76,y=100)
p = Button(root,image=ImageP)
p.bind("<Button-1>",randomStepP )
p.place(x=152,y=100)
root.mainloop()
