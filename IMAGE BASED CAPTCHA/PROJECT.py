from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint

root=Tk()
root.geometry("600x600")      #WidthxHeight
root.title("IMAGE CAPTCHA")

#FRAME
f=Frame(root, height=600, width=600)
f.propagate(0)
f.pack(anchor=CENTER)


#RANDOMLY GENERATING A NUMBER
a=randint(1,3)


#IF-ELSE BLOCK TO GENERATE DIFFERENT CAPTCHAS

if a==1:                                            #FIRST CASE
    #HEADING
    heading1=Label(f,text="SELECT IMAGES REPRESENTING CAKES", font=("ComicSansMS", 14, "bold"), fg="blue")
    heading1.pack(anchor=CENTER)
    heading1.grid(row=0, columnspan=3)

    #PUTTING IMAGES IN GRID
    img1=ImageTk.PhotoImage(Image.open("BIRD 1.jpeg"))
    l1=Label(f, image=img1)
    l1.grid(row=1, column=0)
    
    img2=ImageTk.PhotoImage(Image.open("CAKE 1.jpeg"))
    l2=Label(f, image=img2)
    l2.grid(row=1, column=1)
    
    img3=ImageTk.PhotoImage(Image.open("ROAD 1.jpeg"))
    l3=Label(f, image=img3)
    l3.grid(row=1, column=2)

    img4=ImageTk.PhotoImage(Image.open("CAKE 2.jpeg"))
    l4=Label(f, image=img4)
    l4.grid(row=2, column=0)
    
    img5=ImageTk.PhotoImage(Image.open("CAKE 3.jpeg"))
    l5=Label(f, image=img5)
    l5.grid(row=2, column=1)
    
    img6=ImageTk.PhotoImage(Image.open("CAKE 4.jpeg"))
    l6=Label(f, image=img6)
    l6.grid(row=2, column=2)
    
    img7=ImageTk.PhotoImage(Image.open("BIRD 2.jpeg"))
    l7=Label(f, image=img7)
    l7.grid(row=3, column=0)
    
    img8=ImageTk.PhotoImage(Image.open("CAKE 5.jpeg"))
    l8=Label(f, image=img8)
    l8.grid(row=3, column=1)
    
    img9=ImageTk.PhotoImage(Image.open("ROAD 2.jpeg"))
    l9=Label(f, image=img9)
    l9.grid(row=3, column=2)


elif a==2:           #SECOND CASE
    #HEADING
    heading2=Label(f,text="SELECT IMAGES REPRESENTING BIRDS", font=("ComicSansMS", 14, "bold"), fg="blue")
    heading2.pack(anchor=CENTER)
    heading2.grid(row=0, columnspan=3)

    #PUTTING IMAGES IN GRID
    img10=ImageTk.PhotoImage(Image.open("CAKE 1.jpeg"))
    l10=Label(f, image=img10)
    l10.grid(row=1, column=0)

    img11=ImageTk.PhotoImage(Image.open("BIRD 1.jpeg"))
    l11=Label(f, image=img11)
    l11.grid(row=1, column=1)

    img12=ImageTk.PhotoImage(Image.open("ROAD 1.jpeg"))
    l12=Label(f, image=img12)
    l12.grid(row=1, column=2)

    img13=ImageTk.PhotoImage(Image.open("BIRD 2.jpeg"))
    l13=Label(f, image=img13)
    l13.grid(row=2, column=0)

    img14=ImageTk.PhotoImage(Image.open("BIRD 3.jpeg"))
    l14=Label(f, image=img14)
    l14.grid(row=2, column=1)

    img15=ImageTk.PhotoImage(Image.open("BIRD 4.jpeg"))
    l15=Label(f, image=img15)
    l15.grid(row=2, column=2)

    img16=ImageTk.PhotoImage(Image.open("CAKE 2.jpeg"))
    l16=Label(f, image=img16)
    l16.grid(row=3, column=0)

    img17=ImageTk.PhotoImage(Image.open("BIRD 5.jpeg"))
    l17=Label(f, image=img17)
    l17.grid(row=3, column=1)

    img18=ImageTk.PhotoImage(Image.open("ROAD 2.jpeg"))
    l18=Label(f, image=img18)
    l18.grid(row=3, column=2)


elif a==3:           #THIRD CASE
    #HEADING
    heading3=Label(f,text="SELECT IMAGES REPRESENTING CARS", font=("ComicSansMS", 14, "bold"), fg="blue")
    heading3.pack(anchor=CENTER)
    heading3.grid(row=0, columnspan=3)

    #PUTTING IMAGES IN GRID
    img19=ImageTk.PhotoImage(Image.open("CAKE 1.jpeg"))
    l19=Label(f, image=img19)
    l19.grid(row=1, column=0)

    img20=ImageTk.PhotoImage(Image.open("ROAD 1.jpeg"))
    l20=Label(f, image=img20)
    l20.grid(row=1, column=1)

    img21=ImageTk.PhotoImage(Image.open("BIRD 1.jpeg"))
    l21=Label(f, image=img21)
    l21.grid(row=1, column=2)

    img22=ImageTk.PhotoImage(Image.open("ROAD 2.jpeg"))
    l22=Label(f, image=img22)
    l22.grid(row=2, column=0)

    img23=ImageTk.PhotoImage(Image.open("ROAD 3.jpeg"))
    l23=Label(f, image=img23)
    l23.grid(row=2, column=1)

    img24=ImageTk.PhotoImage(Image.open("ROAD 4.jpeg"))
    l24=Label(f, image=img24)
    l24.grid(row=2, column=2)

    img25=ImageTk.PhotoImage(Image.open("CAKE 2.jpeg"))
    l25=Label(f, image=img25)
    l25.grid(row=3, column=0)

    img26=ImageTk.PhotoImage(Image.open("ROAD 5.jpeg"))
    l26=Label(f, image=img26)
    l26.grid(row=3, column=1)

    img27=ImageTk.PhotoImage(Image.open("BIRD 2.jpeg"))
    l27=Label(f, image=img27)
    l27.grid(row=3, column=2)


#CREATING VARIABLES FOR CHECKBUTTONS
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v9=IntVar()

#FUNCTION TO VERIFY
def verify(root):
    if(v2.get()==1 and v4.get()==1 and v5.get()==1 and v6.get()==1 and v8.get()==1):
        if(v1.get()==1 or v3.get()==1 or v7.get()==1 or v9.get()==1):
            messagebox.showinfo("ALERT", "YOU ARE NOT VERIFIED")
        else:
            messagebox.showinfo("SUCCESS", "YOU ARE VERIFIED")
    else:
        messagebox.showinfo("ALERT", "YOU ARE NOT VERIFIED")

#CREATING CHECBUTTONS
c1=Checkbutton(f, variable=v1, bd=0, onvalue=1, offvalue=0)
c1.grid(row=1, column=0)

c2=Checkbutton(f, variable=v2, bd=0, onvalue=1, offvalue=0)
c2.grid(row=1, column=1)

c3=Checkbutton(f, variable=v3, bd=0, onvalue=1, offvalue=0)
c3.grid(row=1, column=2)

c4=Checkbutton(f, variable=v4, bd=0, onvalue=1, offvalue=0)
c4.grid(row=2, column=0)

c5=Checkbutton(f, variable=v5, bd=0, onvalue=1, offvalue=0)
c5.grid(row=2, column=1)

c6=Checkbutton(f, variable=v6, bd=0, onvalue=1, offvalue=0)
c6.grid(row=2, column=2)

c7=Checkbutton(f, variable=v7, bd=0, onvalue=1, offvalue=0)
c7.grid(row=3, column=0)

c8=Checkbutton(f, variable=v8, bd=0, onvalue=1, offvalue=0)
c8.grid(row=3, column=1)

c9=Checkbutton(f, variable=v9, bd=0, onvalue=1, offvalue=0)
c9.grid(row=3, column=2)

#CREATING A BUTTON
b=Button(f, text="Verify", width=12, height=1, font=("Comicsans ms", 14, "bold"), bg="red", fg="yellow", activebackground="green", activeforeground="yellow")
b.grid(row=4, columnspan=3, padx=10, pady=10)
b.bind("<Button-1>", verify)

root.mainloop()
