from tkinter import *
import os

window=Tk()
window.iconbitmap(r'.\icons\logo1.ico')
window.title('Face Recognition')
window.geometry('800x400')

#function calling for files
def capture():
	os.system('python face-cap.py')

def train():
	os.system('python face.py')

def recognize():
	os.system('python webcam_recognizer.py')

#display text
l0=Label(window,text='Welcome to face recognition system:')
l0.config(font=("Courier", 20,"bold"))
l0.pack(pady=10)

middleframe=Frame(window)
middleframe.pack(pady=20)

pic1=PhotoImage(file='.\icons\camera.png')
# but1=Button(middleframe,image=pic1,command=capture)
but1=Label(middleframe,image=pic1)
but1.grid(column=0,row=0,padx=25)
b1=Button(middleframe,text='Capture',command=capture,bg='black',fg='white')
b1.config(font=("Courier", 10,"bold"))
b1.grid(column=0,row=1,padx=20,pady=20)


pic2=PhotoImage(file='.\icons\chip.png')
# but2=Button(middleframe,image=pic2,command=train)
but2=Label(middleframe,image=pic2)
but2.grid(column=1,row=0,padx=25)
b2=Button(middleframe,text='Train',command=train,bg='black',fg='white')
b2.config(font=("Courier", 10,"bold"))
b2.grid(column=1,row=1,padx=20,pady=20)


pic3=PhotoImage(file='./icons/recog.png')
# but3=Button(middleframe,image=pic3,command=recognize)
but3=Label(middleframe,image=pic3)
but3.grid(column=2,row=0,padx=25)
b3=Button(middleframe,text='Recognize',command=recognize,bg='black',fg='white')
b3.config(font=("Courier", 10,"bold"))
b3.grid(column=2,row=1,padx=20,pady=20)

statusbar = Label(window, text="Thank you for using our system. - Comp2073", relief=SUNKEN, anchor=W)
statusbar.config(font=("Courier", 10,"bold"))
statusbar.pack(side=BOTTOM, fill=X)

window.mainloop()