from tkinter import *
import random
from tkinter import messagebox
user_won=0
computer_won=0
options=["0","1","2"]
#0=سنگ
#1=کاغذ
#2=قیچی
windows = Tk()
windows.title("ُبازی سنگ کاغذ و قیچی")
windows.geometry("330x450")
def action(user_pick):
    global user_won
    global computer_won
    options=[0,1,2]
    random_number= random.randint(0,2)
    computer_pick=options[random_number]
    if user_pick == 0 and computer_pick== 2:
        x="این بارو تو بردی"
        user_won+=1
        
    elif user_pick == 1 and computer_pick== 0:
        x="این بارو تو بردی"
        user_won+=1
        
    elif user_pick == 2 and computer_pick== 1:
        x="این بارو تو بردی"
        user_won+=1
    elif user_pick==computer_pick:
        x="برابر شدیم بی تجربه دوباره امتحان کن"
    else:
        x="من بردم زیقی"
        computer_won+=1  
    x2=["سنگ","کاغذ","قیچی"]
    answer.config(text="انتخاب من {0} بود\n\n{1}".format(x2[computer_pick],x))
    buttom4.config(text="{0}:امتیاز تو".format(user_won))
    buttom5.config(text="{0}:امتیاز من".format(computer_won))
    
def user_won_result():
    messagebox.showinfo("نتیجه","تا این جای کار امتیاز تو {0} و امتیاز من {1}".format(user_won,computer_won))
    
frame_1=LabelFrame(windows,text="Input",font="zar",fg="#F6B17A",bg="#2D3250")
frame_1.pack(fill="both",expand=True)
frame_2=LabelFrame(windows,text="Output",font="zar",fg="#F6B17A",bg="#2D3250")
frame_2.pack(fill="both",expand=True)
text = Label(frame_1,text="انتخاب کن",font=("Ahang BlackSharp",15),
      bg="#2D3250",fg="white")
text.pack(pady=(70,1))



buttom1 = Button(frame_1,
       text="سنگ",font=("Ahang BlackSharp",15),
       bg="#F6B17A",command=lambda: (action(0)))
buttom1.pack(side="left",padx=(70,2))
buttom2 = Button(frame_1,
       text="کاغذ",font=("Ahang BlackSharp",15),
       bg="#F6B17A",command=lambda: (action(1)))
buttom2.pack(side="left",padx=(1,2))
buttom3 = Button(frame_1,
       text="قیچی",font=("Ahang BlackSharp",15),
       bg="#F6B17A",command=lambda: (action(2)))
buttom3.pack(side="left",padx=(1,2))

buttom4 = Button(frame_2,
       text=":امتیاز تو",font=("Ahang BlackSharp",15),
       bg="#F6B17A",
       command=user_won_result)
buttom4.pack(side="bottom",padx=(1,2))
buttom5 = Button(frame_2,
       text=":امتیاز من",font=("Ahang BlackSharp",15),
       bg="#F6B17A",
       command=user_won_result)
buttom5.pack(side="bottom",padx=(1,2))
answer=Label(frame_2,text='',font=("Ahang BlackSharp",13),
             bg="#2D3250",fg="white")
answer.pack(side="top")

windows.mainloop()