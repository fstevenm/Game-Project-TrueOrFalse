import tkinter,tkinter.messagebox
import random

pertanyaan=['Apakah benar (8x9)-74+4= 2?',
            'Presiden pertama negara Republik Indonesia adalah Jokowi']
jawab=['benar','salah']
Skor = 0
SisaWaktu=0
SkorTinggi=[]

def enter(Event):
    soal()

def main():
    global Skor,SisaWaktu
    Skor=0
    SisaWaktu=0
    SisaWaktu+=31
    waktumundur()
    soal()
    e['state']='normal'
    Tombol.config(text="Stop",command=stop,bg="red")
    label1.config(text="",bg='black')
    label2.config(text="",bg='black')
    
    
def stop():
    global SisaWaktu
    SisaWaktu=-1
    SkorTinggi.append(Skor)
    label1.config(text="Skor tertinggi: "+str(max(SkorTinggi)))
    label2.config(text="")
    Waktu.config(text="",bg='black')
    TeksSoal.config(text="Waktu habis")
    e.delete(0, tkinter.END) 
    Waktu.after(1000,aktif)
    Tombol['state']='disabled'
    Tombol.config(text="Main",command=main,bg="lime")
    e['state']='disabled'

def aktif():
    Tombol['state']='normal'
    
def waktumundur(): 
    global SisaWaktu
    if SisaWaktu>0:
        SisaWaktu-=1
        Waktu.config(text="Sisa Waktu: "+str(SisaWaktu),fg='white')
        Waktu.after(1000,waktumundur)
    elif SisaWaktu==0:
        SkorTinggi.append(Skor)
        label1.config(text="Skor tertinggi: "+str(max(SkorTinggi)))
        label2.config(text="")
        Waktu.config(text="")
        TeksSoal.config(text="Waktu habis")
        e.delete(0, tkinter.END) 
        Waktu.after(1000,aktif)
        Tombol.config(text="Main",command=main,bg="lime")
        Tombol['state']='disabled'
        e['state']='disabled'

def soal():
    global Skor,pertanyaan,jawab,SisaWaktu
    if SisaWaktu>0:
        if 0<SisaWaktu<30:
            if pertanyaan[0]=='Apakah benar (8x9)-74+4= 2?':
                if e.get().lower()==jawab[0]:
                    Skor+=1
                    label2.config(text="Benar")
                else:
                    Skor-=1
                    label2.config(text="Salah")
            elif pertanyaan[0]=='Presiden pertama negara Republik Indonesia adalah Jokowi':
                if e.get().lower()==jawab[1]:
                    Skor+=1
                    label2.config(text="Benar")
                else:
                    Skor-=1
                    label2.config(text="Salah")
                    
        if Skor == 1:
            skor1.config(bg='red')
            skor2.config(bg='lightgrey')
            skor3.config(bg='lightgrey')
            skor4.config(bg='lightgrey')
            skor5.config(bg='lightgrey')
            skor6.config(bg='lightgrey')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 2:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='lightgrey')
            skor4.config(bg='lightgrey')
            skor5.config(bg='lightgrey')
            skor6.config(bg='lightgrey')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 3:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='lightgrey')
            skor5.config(bg='lightgrey')
            skor6.config(bg='lightgrey')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 4:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='lightgrey')
            skor6.config(bg='lightgrey')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 5:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='lightgrey')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 6:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 7:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 8:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 9:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 10:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='red')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 11:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='red')
            skor11.config(bg='red')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 12:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='red')
            skor11.config(bg='red')
            skor12.config(bg='red')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 13:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='red')
            skor11.config(bg='red')
            skor12.config(bg='red')
            skor13.config(bg='red')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        elif Skor == 14:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='red')
            skor11.config(bg='red')
            skor12.config(bg='red')
            skor13.config(bg='red')
            skor14.config(bg='red')
            skor15.config(bg='lightgrey')
        elif Skor == 15:
            skor1.config(bg='red')
            skor2.config(bg='red')
            skor3.config(bg='red')
            skor4.config(bg='red')
            skor5.config(bg='red')
            skor6.config(bg='red')
            skor7.config(bg='red')
            skor8.config(bg='red')
            skor9.config(bg='red')
            skor10.config(bg='red')
            skor11.config(bg='red')
            skor12.config(bg='red')
            skor13.config(bg='red')
            skor14.config(bg='red')
            skor15.config(bg='red')
            tkinter.messagebox.showdialog("WINNER","Selamat Anda Menang!")
            SisaWaktu=-1
        elif Skor<1:
            skor1.config(bg='lightgrey')
            skor2.config(bg='lightgrey')
            skor3.config(bg='lightgrey')
            skor4.config(bg='lightgrey')
            skor5.config(bg='lightgrey')
            skor6.config(bg='lightgrey')
            skor7.config(bg='lightgrey')
            skor8.config(bg='lightgrey')
            skor9.config(bg='lightgrey')
            skor10.config(bg='lightgrey')
            skor11.config(bg='lightgrey')
            skor12.config(bg='lightgrey')
            skor13.config(bg='lightgrey')
            skor14.config(bg='lightgrey')
            skor15.config(bg='lightgrey')
        
        if Skor>=0:
            benar.config(text="Skor Anda " +str(Skor))
        if Skor<0:
            benar.config(text="Skor Anda " +str(Skor))
    
        random.shuffle(pertanyaan)
        e.delete(0,tkinter.END)
        TeksSoal.config(text=pertanyaan[0])
        label1.config(text="Skor: "+str(Skor))
        

        
window=tkinter.Tk()
jendela1=tkinter.Frame(window)
jendela1.grid(row=0,column=0)
jendela2=tkinter.Frame(window)
jendela2.grid(row=0,column=1)
jendela1.configure(bg='black')

#===================================================JENDELA 1==========================================================
tkinter.Label(jendela1,text="\n",font="times 12",bg='black').grid()

label1=tkinter.Label(jendela1,text="",fg='white',bg='black')
label1.grid(row=0,column=0,rowspan=2,columnspan=4)
label2=tkinter.Label(jendela1,text="Selamat datang di permainan True/False",
                     bg='black',fg='white',font="times 18 bold")
label2.grid(row=1,column=0,columnspan=4)
#label3=tkinter.Label(jendela1,text="")
#label3.grid(row=2,column=0)
Waktu=tkinter.Label(jendela1,text="",font="times 18 bold",bg='black',fg='white')
Waktu.grid(row=2,column=0,columnspan=4)


TeksSoal=tkinter.Label(jendela1,text="Siap?",font="times 12 bold",bg="yellow",height=1,width=50)
TeksSoal.grid(row=3,column=0,columnspan=4)

tkinter.Label(jendela1,text="\n",font="times 12",bg='black').grid()

Tombol=tkinter.Button(jendela1,text="Main",font="times 14 bold",bg="lime",
                      command=main,height=2,width=10)
Tombol.grid(row=5,column=0,columnspan=4)

window.bind(Tombol,enter)
e=tkinter.Entry(jendela1)
e['state']='disabled'
window.bind('<Return>',enter)
e.focus_set()
e.grid(row=4,column=0,columnspan=4)



#===================================================JENDELA 2==========================================================
highlight=tkinter.Label(jendela2,text="Jawab 15 soal dengan tepat \ndalam waktu 30 detik untuk menang",
                        font="Arial 12 bold")
highlight.grid(row=0,column=0,columnspan=3)

skor1=tkinter.Label(jendela2,text="1",font="Arial 10",bg='lightgrey',width=6)
skor2=tkinter.Label(jendela2,text="2",font="Arial 10",bg='lightgrey',width=6)
skor3=tkinter.Label(jendela2,text="3",font="Arial 10",bg='lightgrey',width=6)
skor4=tkinter.Label(jendela2,text="4",font="Arial 10",bg='lightgrey',width=6)
skor5=tkinter.Label(jendela2,text="5",font="Arial 10",bg='lightgrey',width=6)
skor6=tkinter.Label(jendela2,text="6",font="Arial 10",bg='lightgrey',width=6)
skor7=tkinter.Label(jendela2,text="7",font="Arial 10",bg='lightgrey',width=6)
skor8=tkinter.Label(jendela2,text="8",font="Arial 10",bg='lightgrey',width=6)
skor9=tkinter.Label(jendela2,text="9",font="Arial 10",bg='lightgrey',width=6)
skor10=tkinter.Label(jendela2,text="10",font="Arial 10",bg='lightgrey',width=6)
skor11=tkinter.Label(jendela2,text="11",font="Arial 10",bg='lightgrey',width=6)
skor12=tkinter.Label(jendela2,text="12",font="Arial 10",bg='lightgrey',width=6)
skor13=tkinter.Label(jendela2,text="13",font="Arial 10",bg='lightgrey',width=6)
skor14=tkinter.Label(jendela2,text="14",font="Arial 10",bg='lightgrey',width=6)
skor15=tkinter.Label(jendela2,text="15",font="Arial 10",bg='lightgrey',width=6)
skor1.grid(row=1,column=0)
skor2.grid(row=2,column=0)
skor3.grid(row=3,column=0)
skor4.grid(row=4,column=0)
skor5.grid(row=5,column=0)
skor6.grid(row=1,column=1)
skor7.grid(row=2,column=1)
skor8.grid(row=3,column=1)
skor9.grid(row=4,column=1)
skor10.grid(row=5,column=1)
skor11.grid(row=1,column=2)
skor12.grid(row=2,column=2)
skor13.grid(row=3,column=2)
skor14.grid(row=4,column=2)
skor15.grid(row=5,column=2)


benar=tkinter.Label(jendela2,text="")
benar.grid(row=6,column=0,columnspan=3)



window.mainloop()
