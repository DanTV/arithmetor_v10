from tkinter import *
import os
class Main:
    def finall(self, text):
        final = Tk()
        final.title("ОТВЕТ")
        if text.startswith("[rjustify]"):
            just = "right"
        else:
            just='left'
        otvet = Label(master=final,justify=just, text=text, font='Arial 30', fg='blue')
        otvet.pack(side='top', fill='x')
        ok_button = Button(master=final, text="OK", font='Arial 25', fg='blue', command=lambda: final.destroy())
        ok_button.pack(side='bottom', fill='x')
        final.mainloop()
    def minus(self):
        def doit():
            nonlocal umenwaemoe, vichitaemoe
            vichit = vichitaemoe.get()
            umenw = umenwaemoe.get()
            answer = umenw + " - "+vichit+" = "+str(int(umenw) - int(vichit))
            answer1 = " "+umenw+"\n"+"-\n"+"   "+" "*(len(umenw)-len(vichit))+vichit+"\n"+"  "+("-"*len(umenw))+"-"+"\n  "+str(int(umenw)-int(vichit))
            answer2 = "Пример\n"+answer+"\n\nСтолбик\n"+answer1
            return answer2
        self.armenu.destroy()
        self.minus1 = Tk()
        self.minus1.title("Minus")
        bg=Label(master=self.minus1, bg='lightblue', width=27, height=10)
        bg.pack()
        umenwaemoe = StringVar()
        vichitaemoe = StringVar()
        umen = Entry(master=bg, width=10, bg='yellow', textvariable=umenwaemoe)
        umen.pack()
        umen.place(x=5, y=3)

        znak = Label(master=self.minus1, text="--", font="Arial 16", bg='lightblue')
        znak.pack()
        znak.place(x=85, y=1)

        vich = Entry(master=bg, width=10, bg='yellow', textvariable=vichitaemoe)
        vich.pack()
        vich.place(x=120, y=3)

        ok_button = Button(master=bg, text="OK", font='Arial 16', bg='lightblue', width=15, height=1, command=lambda: self.finall(doit()))
        ok_button.pack()
        ok_button.place(x=2, y=35)

        self.minus1.mainloop()
    def umnowenie(self):
        def doit():
            nonlocal umn_var, umn_var2
            var1 = str(umn_var.get())
            var2 = str(umn_var2.get())
            answer = int(var1)*int(var2)
            answer1 = var1+" * "+var2+" = "+str(answer)
            nmbrs = []
            for c in range(0, len(var2)):
                print(c, "resultat v cycle")
                num = var2[(len(var2)-1-c)]
                num2 = int(num)*int(var1)
                nmbrs.append(str(num2*int(str("1"+"0"*c))))
            resultat=""
            for i in nmbrs:
                resultat = resultat+i+"\n+             "+" \n"
            resultat = resultat[:(len(resultat)-1)]+"0\n---------\n"
            resultat=resultat+str(answer)
            if int(var1) > int(var2):
                frst = var1
                scnd = var2
            else:
                frst=var2
                scnd=var1
            resultat1 = "[rjustify]\nПример\n"+answer1+"\n\nСтолбик\n"+frst+"\n"+"x"+" "*len(frst)+" \n"+scnd+"\n-----------\n"+resultat
            return resultat1

        self.armenu.destroy()
        self.umnowen = Tk()
        self.umnowen.title("Умножение")
        bg=Label(master=self.umnowen, width=27,height=5, bg='lightblue')
        bg.pack(side='top', fill='x')
        umn_var = StringVar()
        umn_var2= StringVar()
        umn_e = Entry(master=bg, width=30, bg='yellow',textvariable=umn_var)
        umn_e.pack()
        umn_e.place(x=5,y=20)
        umn_e2 = Entry(master=bg, width=30, bg='yellow', textvariable=umn_var2)
        umn_e2.pack()
        umn_e2.place(x=5,y=50)
        ok_button = Button(master=self.umnowen, text='OK', command=lambda: self.finall(doit()))
        ok_button.pack(side='bottom',fill='x')
        self.umnowen.mainloop()
    def sqr(self):
        def doit():
            symbols = {"1":"¹", "2":"²", "3":"³", "4":"⁴", "5":'⁵', '6':"6", '7':'⁷', '8':'⁸', '9':'9', '0':"0", "krn":"√"}
            nonlocal koren_var
            import math
            answer = math.sqrt(int(koren_var.get()))
            return (str(symbols["2"]+symbols["krn"])+str(koren_var.get())+" = "+str(answer))


        self.armenu.destroy()
        self.sqrtsa = Tk()
        self.sqrtsa.title("Извлечение корня")
        bg = Label(master=self.sqrtsa, width=27,height=5, bg='lightblue')
        bg.pack(side='top', fill='x')
        koren_var = StringVar()

        koren = Entry(master=bg, width=60, textvariable=koren_var, bg='yellow')
        koren.pack()
        koren.place(x=5, y=40)

        koren_info = Label(master=bg, text="Число", font='Arial 14', bg='lightblue')
        koren_info.pack()
        koren_info.place(x=380, y=40)

        ok_button = Button(master=self.sqrtsa, text="OK", bg='lightblue', font='Arial 25',
                           command=lambda: self.finall(doit()))
        ok_button.pack(side='bottom', fill='x')
        self.sqrtsa.mainloop()
    def plus(self):
        def doit():
            nonlocal slag1, slag2
            if int(slag1.get())>int(slag2.get()):
                f = slag1.get()
                s = slag2.get()
            else:
                f= slag2.get()
                s=slag1.get()
            answer=str(int(slag1.get())+int(slag2.get()))
            result="[rjustify]\nПример\n"+slag1.get()+" + "+slag2.get()+" = "+answer+"\n\nСтолбик\n"+f+"\n+"+" "*len(f)+" \n"+s+"\n"+"-"*len(f)+"\n"+answer
            return result
        self.armenu.destroy()
        self.pls = Tk()
        self.pls.title("Сложение")
        bg = Label(master=self.pls, width=27, height=5, bg='lightblue')
        bg.pack(side='top', fill='x')
        ok_button=Button(master=self.pls, text='OK', command=lambda: self.finall(doit()))
        ok_button.pack(side='bottom', fill='x')
        slag1=StringVar()
        slag2 = StringVar()
        one_slag = Entry(master=bg, width=60, textvariable=slag1, bg='yellow')
        one_slag.pack()
        one_slag.place(x=5,y=5)
        two_slag = Entry(master=bg, width=60, textvariable=slag2, bg='yellow')
        two_slag.pack()
        two_slag.place(x=5,y=40)
        self.pls.mainloop()
    def step(self):
        # √
        def doit():
            nonlocal oner, twor
            one = int(oner.get())
            two = int(twor.get())
            three = one
            result = str(one)
            for i in range(1, two):
                three = three*one
                print(three)
                result = result + " * " + str(one)
                print(result)
            result = str(one)+" "+result[2:]+" = "+ str(three)
            return result
        self.armenu.destroy()
        self.stepen = Tk()
        self.stepen.title("Возведение в степень")
        bg=Label(master=self.stepen, bg='lightblue', width=27, height=5)
        bg.pack(side='top', fill='x')
        oner = StringVar()
        one = Entry(master=bg, width=60, textvariable=oner)
        one.pack()
        one.place(x=5, y=5)

        twor = StringVar()
        two= Entry(master=bg, width=60, textvariable=twor)
        two.pack()
        two.place(x=5, y=40)

        one_info = Label(master=bg, text="Основание степени", font='Arial 14', bg='lightblue')
        one_info.pack()
        one_info.place(x=380, y= 1)

        two_info = Label(master=bg, text='Показатель степени', font='Arial 14', bg='lightblue')
        two_info.pack()
        two_info.place(x=380,y=36)

        ok_button = Button(master=self.stepen,text="OK", bg='lightblue', font='Arial 25', command=lambda: self.finall(doit()))
        ok_button.pack(side='bottom', fill='x')
        self.stepen.mainloop()

    def delen(self):
        self.finall("Извините, но эта версия Arithmetor'а поддерживает только:\nсложение, умножение, вычитание, извлечение квадратного корня и возведение в степень\n"
                    "Я надеюсь, что в новой версии деление будет воспроизводиться моей программой.\n\n\n"
                    "                                                               ® Fuckin' company ™2017")
    def go(self):
        self.hello.destroy()
        self.armenu = Tk()
        self.armenu.title("ArifmetoR 6000")
        bg = Label(master=self.armenu, width=120, height=38, bg='lightblue')
        bg.pack()


        # Извлечение корня
        sqrt_b = Button(master=bg, width=65,height=3, text="Извлечение квадратного корня",font="Arial 16",bg="lightgreen", command=self.sqr)
        sqrt_b.pack()
        sqrt_b.place(x=30, y=5)

        # Умножение
        umn_b = Button(master=bg, width=65, height=3, text="Умножение", font="Arial 16",bg="lightgreen", command=self.umnowenie)
        umn_b.pack()
        umn_b.place(x=30, y=100)

        # Минус
        min_b = Button(master=bg, width=65, height=3, text="Вычитание", font="Arial 16",bg="lightgreen", command=self.minus)
        min_b.pack()
        min_b.place(x=30, y=195)

        # Плюс
        plus_b = Button(master=bg, width=65, height=3, text="Сложение", font="Arial 16",bg="lightgreen", command=self.plus)
        plus_b.pack()
        plus_b.place(x=30, y=290)

        # Деление
        del_b = Button(master=bg, width=65, height=3, text="Деление[unavaible]", font="Arial 16",bg="lightyellow", command=self.delen)
        del_b.pack()
        del_b.place(x=30, y=385)

        # Возведение в степень
        step_b = Button(master=bg, width=65, height=3, text="Возведение в степень", font="Arial 16",bg="lightgreen", command=self.step)
        step_b.pack()
        step_b.place(x=30, y=385+95)

        self.armenu.mainloop()
    def nope(self, name):
        self.hello = Tk()
        self.hello.title("Hello!")
        hellos = Label(master=self.hello, text=("Здравствуй, "+name),fg='magenta', font="Arial 30")
        hellos.pack(side="top", fill='x')
        hellos_ok = Button(master=self.hello, text="OK",font="Arial 30", command=self.go)
        hellos_ok.pack(side="bottom", fill='x')
        self.hello.mainloop()

# Создание имени
if os.path.exists(("C:\\Users\\"+str(os.getlogin())+"\\name.txt")):
    name = open(("C:\\Users\\"+str(os.getlogin())+"\\name.txt"), "r")
    a = name.read()
    print("\n"*100)
    Main().nope(a)
else:
    a = str(input("Name/Имя: "))
    print("\n"*100)
    name = open(("C:\\Users\\"+str(os.getlogin())+"\\name.txt"), "w")
    name.write(a)
    name.close()
    Main().nope(a)
