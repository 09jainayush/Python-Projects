from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.geometry("850x400")
root.title("LANGUAGE TRANSLATOR")

label1=Label(root, text="LANGUAGE TRANSLATOR", bg="brown", fg="goldenrod", font="ComicSansMS 25 bold") #HEADING
label1.pack(side=TOP, anchor=CENTER)

label2=Label(root, text="ENTER THE TEXT:", fg="red", font="ComicSansMS 15 bold") #LABEL
label2.pack(side=LEFT)
label2.place(x=100, y=100)

message=Entry(root,bg="pink", fg="Navy", font="ComicSansMS 15 bold") #ENTRY BOX
message.place(x=282, y=98, width=400, height=35)

label3=Label(root, text="SELECT THE LANGUAGE: ", fg="red", font="ComicSansMS 15 bold") #LABEL
label3.pack(side=LEFT)
label3.place(x=100, y=150)

lang=list(LANGUAGES.values())                 #DROPDOWN BOX
sel_lang=ttk.Combobox(root, values=lang, width=35)
sel_lang.place(x=352, y=155)

label4=Label(root, text="TRANSLATED TEXT: ", fg="red", font="ComicSansMS 15 bold") #LABEL
label4.pack(side=LEFT)
label4.place(x=100, y=200)

trans_text=Entry(root,bg="pink", fg="Navy", font="ComicSansMS 15 bold") #ENTRY BOX
trans_text.place(x=302, y=200, width=400, height=35)

def Translate():                #TRANSLATOR TOOL
    translator=Translator()
    translate1=translator.translate(text=message.get(), dest=sel_lang.get())
    trans_text.delete(0, END)
    trans_text.insert(END, translate1.text)

trans_btn=Button(root, text="TRANSLATE", bg="yellow", fg="red", font="ComicSansMS 15 bold", pady=5, padx=5, command=Translate, activebackground="green", activeforeground="pink")
trans_btn.place(x=350, y=250)
    
root.mainloop()
