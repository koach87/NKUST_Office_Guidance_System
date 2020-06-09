from tkinter import *
import os
class Gui_For_Office:

    def __init__(self,master):
        self.master = master
        self.initUI()

    def to_start_page(self):
        self.questions_page.pack_forget()
        self.start_page.pack(expand=True, fill=BOTH)


    def to_questions_page(self):
        self.start_page.pack_forget()
        self.questions_page.pack(expand=True, fill=BOTH)


    def initUI(self):
        #set UI 
        self.master.geometry("1920x1080")
        self.master.title("Office Guidance System")

        #start page setting
        self.start_page = Frame(self.master, width=1920, height=1080, bg="gray")
        start_page_middle = Frame(self.start_page,bg = "white")

        #Label of notice
        notice_var = StringVar()
        notice = Label(start_page_middle, textvariable = notice_var)
        notice_var.set("請輸入學號")
        notice.pack()        

        #middle widget
        std_id = Entry(start_page_middle,width = 20)
        std_id.pack()

        #middle widget
        btn_OK = Button(start_page_middle,text = "OK",width = 10,command = self.to_questions_page)
        btn_OK.pack()

        #middle widget
        btn_guest = Button(start_page_middle,text = "非學生請點我",width = 10)
        btn_guest.pack()

        #middle frame setting
        start_page_middle.place(relx=0.5, rely=0.5, anchor=CENTER)


        #qeustions page setting
        self.questions_page = Frame(self.master, width=1920, height=1080, bg="green")

        questions_label_var = StringVar()
        questions_label = Label(self.questions_page,font = ("微軟正黑體",30), textvariable = questions_label_var)
        questions_label_var.set("請選擇欲服務項目")
        questions_label.pack(anchor="n", side = TOP)

        buttons_frame = Frame(self.questions_page)
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        services_cnt = 9
        for i in range(services_cnt//3):
            for j in range(3):
                Button(buttons_frame,text = "test",width = 50,height = 10).grid(row = i, column = j, padx = 100, pady = 60)

        btn_cancel = Button(self.questions_page,text = "取消/上一頁", font =("微軟正黑體",30),command = self.to_start_page)
        btn_cancel.pack(anchor="n", side =LEFT)
                





if __name__ == "__main__":
    a = Gui_For_Office(Tk())
    a.to_start_page()
    a.master.mainloop()