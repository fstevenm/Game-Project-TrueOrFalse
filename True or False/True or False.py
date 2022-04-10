import tkinter,tkinter.messagebox
import random
import pygame

skor = 0
sisa_waktu=0
skor_tertinggi=[]

#======================================== DEF ======================================
def main():
    global skor,sisa_waktu,pertanyaan
    global betul,salah
    bermain()
    menubar_on()
#    tingkat_off()
    skor=0
    sisa_waktu=0
    sisa_waktu+=301
    
    betul=tkinter.Button(jendela1,image=gambar_benar,width=90,height=60,
                         bg='black',command=tru)
    betul.grid(row=5,column=0,columnspan=2)
    salah=tkinter.Button(jendela1,image=gambar_salah,width=90,height=60,
                         bg='black',command=fals)
    salah.grid(row=5,column=3)
    
    waktumundur()
    soal()
    
    Tombol.grid_forget()
    Tombol.config(text="Stop",command=stop,bg="red")
    label1.config(text="",bg='black')
    label2.config(text="",bg='black')
    
def stop():
    global sisa_waktu,skor_tertinggi,skor
    
    betul.grid_forget()
    salah.grid_forget()
    menubar_off()
#    tingkat_on()
    
    sisa_waktu=-1
    skor_tertinggi.append(skor)
    label1.config(text="skor tertinggi: "+str(max(skor_tertinggi)))
    label2.config(text="")
    Waktu.config(text="",bg='black')
    label_soal.config(text="Waktu habis")

    Waktu.after(1000,aktif)
    Tombol['state']='disabled'
    Tombol.grid(row=5,column=0,columnspan=4)
    Tombol.config(text="Main",command=main,bg="yellow")
    hopp()
    pygame.mixer.music.pause()
    
def aktif():
    Tombol['state']='normal'
    
def waktumundur(): 
    global sisa_waktu,skor
    if sisa_waktu>0:
        sisa_waktu-=1
        Waktu.config(text="Sisa Waktu: "+str(sisa_waktu),fg='white')
        Waktu.after(1000,waktumundur)
    elif sisa_waktu==0:
        betul.grid_forget()
        salah.grid_forget()
        menubar_off()
#        tingkat_on()
        
        skor_tertinggi.append(skor)
        label1.config(text="skor tertinggi: "+str(max(skor_tertinggi)))
        label2.config(text="SKOR ANDA = "+str(skor))
        Waktu.config(text="")
        label4.config(text="")
        label_soal.config(text="Waktu habis")
        
        Tombol['state']='disabled'
        Waktu.after(1000,aktif)
        Tombol.config(text="Main",command=main,bg="yellow")
        Tombol.grid(row=5,column=0,columnspan=4)
        
        pygame.mixer.music.pause()
        hopp()
        
def soal():
    global skor,pertanyaan,jawab,sisa_waktu
    global salah,betul
    if sisa_waktu>0:
        if 0<sisa_waktu<301:
            salah['state']='normal'
            betul['state']='normal'
            jawab = 'ya'
            if pertanyaan[0]=='4 + 4 = 12':
                silang()
            elif pertanyaan[0]=='2 - 1 = 0 ':
                silang()
            elif pertanyaan[0]=='21 + 4 = 25':
                centang()
            elif pertanyaan[0]=='2 x 7 = 14':
                centang()
            elif pertanyaan[0]=='223 + 241 = 444':
                silang()
            elif pertanyaan[0]=='21 - 12 = 9':
                centang()
            elif pertanyaan[0]=='24 : 12 = 2':
                centang()
            elif pertanyaan[0]=='234 + 123 = 357':
                centang()
            elif pertanyaan[0]=='11 - 4 = 6':
                centang()
            elif pertanyaan[0]=='12 + 47 = 69':
                silang()
            elif pertanyaan[0]=='222 - 111 = 111':
                centang()
            elif pertanyaan[0]=='25 + 18 = 45':
                silang()
            elif pertanyaan[0]=='40 x 3 = 130':
                silang()
            elif pertanyaan[0]=='50 - 27 = 23':
                centang()
            elif pertanyaan[0]=='(8 x 9) - 74 + 4 = 2':
                centang()
#            elif pertanyaan[0]=='Presiden pertama negara Republik Indonesia adalah Jokowi':
#                silang()
            elif pertanyaan[0]=='1 + 1 x 1 = 11':
                silang()
            elif pertanyaan[0]=='2 + 5 x 9 - 40 = 7':
                centang()
#            elif pertanyaan[0]=='{ ∅ } merupakan lambang dari himpunan kosong':
#                centang()
#            elif pertanyaan[0]=='A = {2,3,7,9,11,13}. A merupakan himpunan bilangan prima':
#                centang()
#            elif pertanyaan[0]=='Untuk melakukan perintah "find" pada komputer \nbisa dilakukan dengan cara menekan tombol Ctrl + F':
#                centang()
#            elif pertanyaan[0]=='Verb III dari "sing" adalah sang':
#                silang()
#            elif pertanyaan[0]=='Atom hidrogen memiliki simbol HI':
#                silang()
#            elif pertanyaan[0]=='Kabel penghubung HP dengan PC adalah kabel USB':
#                centang()
#            elif pertanyaan[0]=='Kerajaan Islam pertama di Pulau Jawa ialah Demak':
#                centang()
#            elif pertanyaan[0]=='Ibu Kota Propinsi Sumatera Selatan adalah Pekanbaru':
#                silang()
#            elif pertanyaan[0]=='Orang yang ahli dalam membuat peta disebut kartografi':
#                silang()
#            elif pertanyaan[0]=='Orang yang melakukan kegiatan distribusi disebut produsen':
#                silang()
#            elif pertanyaan[0]=='Pengikisan tanah oleh air hujan disebut erosi':
#                centang()
#            elif pertanyaan[0]=='Gigi sementara atau gigi yang bisa lepas secara alami\ndisebut gigi susu':
#                centang()
#            elif pertanyaan[0]=='Lambang sila ke-3 adalah Pohon beringin':
#                centang()
#            elif pertanyaan[0]=='Ibukota provinsi Banten adalah Tangerang':
#                silang()
#            elif pertanyaan[0]=='Gudeg adalah makanan khas Jakarta':
#                silang()
#            elif pertanyaan[0]=='Indonesia terletak pada 6°LU-11°LS dan 95°BT-141°BT':
#                centang()
#            elif pertanyaan[0]=='Undang-undang tidak tertulis disebut Adat-Istiadat':
#                silang()
#            elif pertanyaan[0]=='Trias Politika adalah Presiden, Wakil Presiden dan MPR':
#                silang()
#            elif pertanyaan[0]=='230 - 220 x 0,5 = 5!':
#                centang()
#            elif pertanyaan[0]=='114 : -3 + (-98 ) = -126':
#                silang()
#            elif pertanyaan[0]=='log 25 + log 5 + log 80 = 4':
#                centang()
#            elif pertanyaan[0]=='sin2A =2 sin A cos A':
#                centang()
            elif pertanyaan[0]=='-4 + 8 : (-2) x 2 + 5 -3 = 4':
                centang()
#            elif pertanyaan[0]=='1 - (2 + 11) x 2 + 11 = -12':
#                silang()
#            elif pertanyaan[0]=='¼ + ½ x ½ = 0,25':
#                silang()
#            elif pertanyaan[0]=='Satuan SI untuk gaya disebut Newton':
#                centang()
#            elif pertanyaan[0]=='0! = 0':
#                silang()
#            elif pertanyaan[0]=='Tari Piring berasal dari provinsi Riau':
#                silang()
#            
#            elif pertanyaan[0]=='Semua Bahan akan memuai jika dipanaskan':
#                silang()
#            elif pertanyaan[0]=='Hukum Ohm adalah V = I x R':
#                centang()
#            elif pertanyaan[0]=='Partikel listrik negatif disebut elektron':
#                centang()
#            elif pertanyaan[0]=='''Jika ada dua kawat saling sejajar dipasang saling berdekatan
#maka kedua kawat akan saling tarik-menarik
#jika dialiri arus searah''':
#                centang()
#            elif pertanyaan[0]=='Film "The Spongebob Movie" mengharuskan Spongebob \nberpetualang ke Shell City':
#                centang()
#            elif pertanyaan[0]=='Untuk menghilangkan suara televisi, \ntombol yang ditekan pada remot adalah muted':
#                silang()
#            elif pertanyaan[0]=='Bahasa inggris dari "korban" adalah victim':
#                centang()
#            elif pertanyaan[0]=='Volskraad adalah Dewan Rakyat':
#                centang()
#            elif pertanyaan[0]=='Pencipta lagu Maju Tak Gentar adalah Ibu Sud':
#                silang()
#            elif pertanyaan[0]=='Penemu mesin uap adalah Alexander Graham Bell':
#                silang()
#            elif pertanyaan[0]=='Benua terluas di dunia adalah Benua Eropa':
#                silang()
#            elif pertanyaan[0]=='Cetah adalah hewan yang memiliki kemampuan lari tercepat':
#                centang()
#            elif pertanyaan[0]=='Penemu radio adalah Marconi':
#                centang()
#            elif pertanyaan[0]=='Ibu kota negara Ceko adalah Raha':
#                silang()
#            elif pertanyaan[0]=='Pulang terbesar di dunia adalah Greendland':
#                centang()
#            elif pertanyaan[0]=='Log 18 = 0,889':
#                centang()
#            elif pertanyaan[0]=='ª log 1 = 0':
#                centang()
#            elif pertanyaan[0]=='Himpunan penyelesaian 2log (2x+1) = 3 adalah {7}':
#                silang()
#            elif pertanyaan[0]=='2log 4 + 2log 12 – 2log 6 = 4':
#                silang()
#            elif pertanyaan[0]=='3log 5 – 3 log 15 + 3log 9 = 1':
#                centang()
#            elif pertanyaan[0]=='Suku ke-10 dari barisan geometri 6, 12, 24, 48, … adalah 3074':
#                silang()
#            elif pertanyaan[0]=='3 x 3 / 3 - 3 + 3 x 3 = 3':
#                silang()
#            elif pertanyaan[0]=='Nilai dari cos 40° + cos 80° + cos 160° adalah 1/2':
#                silang()
#            elif pertanyaan[0]=='95°F = 308°K':
#                centang()
#            elif pertanyaan[0]=='Peluang muncul dadu pertama bermata 4 \ndari dua mata dadu yang dilempar adalah 4/36':
#                silang()
#            elif pertanyaan[0]=='7 + 7 / 7 + 7 x 7 - 7 = 56':
#                silang()
#            elif pertanyaan[0]=='Suara dengan frekuensi 20 - 20.000 Hz termasuk bunyi Audiosonik':
#                centang()
#            elif pertanyaan[0]=='9 x 9 - 9 + 18 = 40 + 10 x 5':
#                centang()
#            elif pertanyaan[0]=='303°K = 37,5°C':
#                centang()
            
        random.shuffle(pertanyaan)

        label_soal.config(text=pertanyaan[0])
        label4.config(text="skor: "+str(skor))
        
        if skor == 1:
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
        elif skor == 2:
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
        elif skor == 3:
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
        elif skor == 4:
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
        elif skor == 5:
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
        elif skor == 6:
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
        elif skor == 7:
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
        elif skor == 8:
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
        elif skor == 9:
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
        elif skor == 10:
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
        elif skor == 11:
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
        elif skor == 12:
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
        elif skor == 13:
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
        elif skor == 14:
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
        elif skor == 15:
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
            menang()
            
        elif skor<1:
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
        
        if skor>=0:
            benar.config(text="skor Anda " +str(skor))
        if skor<0:
            benar.config(text="skor Anda " +str(skor))

def centang():
    global jawab
    if jawab=='ya':
        naik()
    else:
        turun()

def silang():
    global jawab
    if jawab=='tidak':
        naik()
    else:
        turun()
        
def naik():
    global skor
    skor+=1
    label2.config(text="BENAR")
    lagu_benar()

def turun():
    global skor
    skor-=1
    label2.config(text="SALAH")
    payah()
    
#=========================== DEFINISI TINGKAT KESULITAN ======================================================
def normal():
    global pertanyaan
    pertanyaan = ['4 + 4 = 12','2 - 1 = 0 ','21 + 4 = 25','2 x 7 = 14','223 + 241 = 444','21 - 12 = 9','24 : 12 = 2','234 + 123 = 357','11 - 4 = 6',
            '12 + 47 = 69','222 - 111 = 111','25 + 18 = 45','40 x 3 = 130','50 - 27 = 23','(8 x 9) - 74 + 4 = 2','1 + 1 x 1 = 11','2 + 5 x 9 - 40 = 7','-4 + 8 : (-2) x 2 + 5 -3 = 4']
#    pertanyaan=['(8 x 9) - 74 + 4 = 2',
#    'Presiden pertama negara Republik Indonesia adalah Jokowi',
#    '1 + 1 x 1 = 11','2 + 5 x 9 - 40 = 7','{ ∅ } merupakan lambang dari himpunan kosong',
#    'A = {2,3,7,9,11,13}. A merupakan himpunan bilangan prima',
#    'Untuk melakukan perintah "find" pada komputer \nbisa dilakukan dengan cara menekan tombol Ctrl + F',
#    'Verb III dari "sing" adalah sang',
#    'Atom hidrogen memiliki simbol HI','Kabel penghubung HP dengan PC adalah kabel USB',
#    'Kerajaan Islam pertama di Pulau Jawa ialah Demak',
#    'Ibu Kota Propinsi Sumatera Selatan adalah Pekanbaru',
#    'Orang yang ahli dalam membuat peta disebut kartografi',
#    'Orang yang melakukan kegiatan distribusi disebut produsen',
#    'Pengikisan tanah oleh air hujan disebut erosi',
#    'Gigi sementara atau gigi yang bisa lepas secara alami\ndisebut gigi susu',
#    'Lambang sila ke-3 adalah Pohon beringin',
#    'Ibukota provinsi Banten adalah Tangerang',
#    'Gudeg adalah makanan khas Jakarta',
#    'Indonesia terletak pada 6°LU-11°LS dan 95°BT-141°BT',
#    'Undang-undang tidak tertulis disebut Adat-Istiadat',
#    'Trias Politika adalah Presiden, Wakil Presiden dan MPR',
#    '230 - 220 x 0,5 = 5!','114 : -3 + (-98 ) = -126',
#    'log 25 + log 5 + log 80 = 4','sin2A =2 sin A cos A',
#    '-4 + 8 : (-2) x 2 + 5 -3 = 4',
#    '1 - (2 + 11) x 2 + 11 = -12','¼ + ½ x ½ = 0,25',
#    'Satuan SI untuk gaya disebut Newton','0! = 0',
#    'Tari Piring berasal dari provinsi Riau'
#    ,'Semua Bahan akan memuai jika dipanaskan','Hukum Ohm adalah V = I x R',
#    'Partikel listrik negatif disebut elektron',
#    '''Jika ada dua kawat saling sejajar dipasang saling berdekatan
#maka kedua kawat akan saling tarik-menarik
#jika dialiri arus searah''',
#    'Film "The Spongebob Movie" mengharuskan Spongebob \nberpetualang ke Shell City',
#    'Untuk menghilangkan suara televisi, \ntombol yang ditekan pada remot adalah muted',
#    'Bahasa inggris dari "korban" adalah victim',
#    'Volskraad adalah Dewan Rakyat',
#    'Pencipta lagu Maju Tak Gentar adalah Ibu Sud',
#    'Penemu mesin uap adalah Alexander Graham Bell',
#    'Benua terluas di dunia adalah Benua Eropa',
#    'Cetah adalah hewan yang memiliki kemampuan lari tercepat',
#    'Penemu radio adalah Marconi',
#    'Ibu kota negara Ceko adalah Raha',
#    'Pulang terbesar di dunia adalah Greendland',
#    'Log 18 = 0,889','ª log 1 = 0','Himpunan penyelesaian 2log (2x+1) = 3 adalah {7}',
#    '2log 4 + 2log 12 – 2log 6 = 4',
#    '3log 5 – 3 log 15 + 3log 9 = 1',
#    'Suku ke-10 dari barisan geometri 6, 12, 24, 48, … adalah 3074',
#    '3 x 3 / 3 - 3 + 3 x 3 = 3',
#    'Nilai dari cos 40° + cos 80° + cos 160° adalah 1/2',
#    '95°F = 308°K',
#    '303°K = 37,5°C'
#    'Peluang muncul dadu pertama bermata 4 \ndari dua mata dadu yang dilempar adalah 4/36',
#    '9 x 9 - 9 + 18 = 40 + 10 x 5',
#    '7 + 7 / 7 + 7 x 7 - 7 = 56','Suara dengan frekuensi 20 - 20.000 Hz termasuk bunyi Audiosonik']            
          
#======================================== TOMBOLNYA ==============================
def tru():
    global jawab
    jawab='ya'
    soal()
    
def fals():
    global jawab
    jawab='tidak'
    soal()

#======================================== MENANG ==============================
def menang():
    global sisa_waktu
    sisa_waktu=-2
    Waktu.config(text="Sisa Waktu: "+str(0),fg='white')
    label_soal.config(text="YEAY")
    
    betul.grid_forget()
    salah.grid_forget()
    pygame.mixer.music.pause()
    menang_sound()
    
    Tombol['state']='disabled'
    Waktu.after(1000,aktif)
    Tombol.config(text="Main",command=main,bg="yellow")
    Tombol.grid(row=5,column=0,columnspan=4)
    
    tkinter.messagebox.showinfo("WINNER","Selamat Anda Menang!")
    
    

#======================================== MENU ==============================
    
def buatMenu():
    global menubar
    global menusize
    menubar = tkinter.Menu(window)
    menusize = tkinter.Menu(window, tearoff=False)
    menufile = tkinter.Menu(window, tearoff=False)
#    level = tkinter.Menu(window, tearoff=False)
#    
#    level.add_command(label="Normal",command=normal)
#    level.add_command(label="Sulit",command=sulit)
#    menusize.add_cascade(label="Tingkat Kesulitan",menu=level)
    
    menufile.add_command(label="Pembuat",command=info)
    menufile.add_command(label="Pendukung",command=info1)
    menusize.add_cascade(label="Informasi", menu=menufile)
    menusize.add_separator()
    
    menusize.add_command(label="Bantuan", command= bantuan)
    menubar.add_cascade(label="Menu", menu=menusize)
    
    menubar.add_command(label="Berhenti",command=stop)
    menubar.add_command(label="Keluar", command= keluar)
    window.config(menu=menubar)
    
#==================================== DEFINISI BFRHENTI JADI OFF ======================================================

def menubar_off():
    global menubar
    menubar.entryconfigure("Berhenti", state="disabled")
    
def menubar_on():
    global menubar
    menubar.entryconfigure("Berhenti", state="normal")

#==================================== DEFINISI KESULITAN JADI OFF ======================================================

def tingkat_off():
    global menusize
    menusize.entryconfigure("Tingkat Kesulitan", state="disabled")

def tingkat_on():
    global menusize
    menusize.entryconfigure("Tingkat Kesulitan", state="normal")

#======================================== ISI PERINTAH MENUBAR ======================================================

def bantuan():
    tkinter.messagebox.showinfo("TEST WARNA",''' Pilih Benar atau Salah untuk menjawab!\n skor 15 untuk menang.''')
    
def keluar():
    answer=tkinter.messagebox.askquestion("Keluar","Apakah anda ingin keluar beneran?",icon='question')
    if answer=='yes':
        window.destroy()
        pygame.mixer.music.pause()
    else :
        tkinter.messagebox.showinfo("NOTIF","Selamat datang kembali",icon='info')
         
def info():
    tkinter.messagebox.showinfo("Creator","Ferdinandus Steven Millicent\nNIM: 183114009")

def info1():
    tkinter.messagebox.showinfo("Supported","tkinter")

#======================================================== SOUND ======================================================
    
def bermain():
    pygame.mixer.music.load('main.wav')
    pygame.mixer.music.play(10)
    
def lagu_benar():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('lompat.wav'))

def payah():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('false.wav'))
    
def hopp():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('dead.wav'))
    
def menang_sound():
    pygame.mixer.Channel(4).play(pygame.mixer.Sound('menang1.wav'))
    
#=========================================================== MULAI ===================================================
window=tkinter.Tk()
window.title("Benar / Salah")
window.iconbitmap("icon.ico")

jendela1=tkinter.Frame(window)
jendela1.grid(row=0,column=0)

#jendela1a=tkinter.Frame(jendela1)
#jendela1a.grid(row=0,column=0)
#jendela1a.configure(bg='black')
#jendela1b=tkinter.Frame(jendela1)
#jendela1b.grid(row=1,column=0)
#jendela1b.configure(bg='black')

jendela2=tkinter.Frame(window)
jendela2.grid(row=0,column=1)
jendela1.configure(bg='black')

#===================================================JENDELA 1==========================================================
tkinter.Label(jendela1,text="\n",font="times 12",bg='black').grid()

label1=tkinter.Label(jendela1,text="",fg='white',bg='black')
label1.grid(row=0,column=0,rowspan=2,columnspan=4)
label2=tkinter.Label(jendela1,text="SELAMAT DATANG\nDI PERMAIN BENAR/SALAH",
                     bg='black',fg='white',font="times 18 bold")
label2.grid(row=1,column=0,columnspan=4)


Waktu=tkinter.Label(jendela1,text="",font="times 18 bold",bg='black',fg='white')
Waktu.grid(row=2,column=0,columnspan=4)

label_soal=tkinter.Label(jendela1,text="KLIK MULAI UNTUK MULAI BERMAIN",font="times 12 bold",
                       bg="orange",height=5,width=50,bd=8,relief='groove')
label_soal.grid(row=3,column=0,columnspan=4)

tkinter.Label(jendela1,text="\n",font="times 12",bg='black').grid()

Tombol=tkinter.Button(jendela1,text="Main",font="times 14 bold",bg="yellow",
                      command=main,height=2,width=10)
Tombol.grid(row=5,column=0,columnspan=4)

gambar_benar=tkinter.PhotoImage(file='benar.png')
gambar_salah=tkinter.PhotoImage(file='salah.png')

label4=tkinter.Label(jendela1,bg='black',fg='white')
label4.grid(row=7,column=0,columnspan=4)

label3=tkinter.Label(jendela1,text="Have Fun",bg='black',fg='white')
label3.grid(row=8,column=0,columnspan=4)


#===================================================JENDELA 2==========================================================
highlight=tkinter.Label(jendela2,text="Jawab 15 soal acak berikut dengan pilihan benar/salah\ndalam waktu 30 detik untuk menang!",
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

#===================================================================================
normal()

buatMenu()
menubar_off()
pygame.mixer.init(88400)


window.mainloop()