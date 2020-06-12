from tkinter import *
import pandas as pd

class Gui_For_Office:

    def __init__(self,master):
        self.master = master
        self.initUI()

    def to_start_page(self):
        self.std_id.delete(0, 'end')
        self.questions_page.pack_forget()
        self.start_page.pack(expand=True, fill=BOTH)

    def to_questions_page(self):
        self.start_page.pack_forget()
        self.questions_page.pack(expand=True, fill=BOTH)

    def btn_OK_click(self):
        print(self.std_id.get())
        self.to_questions_page()

    def btn_guest_click(self):
        print('guest')
        self.to_questions_page()

    def call_back_question(self,question_index):
        print(self.xls_services.values[question_index][0])
        

    def initUI(self):
        # get services
        self.xls_services = pd.read_excel(r"C:\Users\user\Desktop\柯奇\py\Office_Guidace_System\GUI_services.xlsx", sheet_name= 0 )

        # get stdlist
        self.xls_stdlist = pd.read_excel(r"C:\Users\user\Desktop\柯奇\py\Office_Guidace_System\GUI_stdlist.xlsx", sheet_name= 0 )
        
        # set UI 
        self.master.state("zoom")
        self.master.title("Office Guidance System")

        # start page setting
        self.start_page = Frame(self.master, bg="gray")
        start_page_middle = Frame(self.start_page,bg = "white")

        # Label of notice
        notice_var = StringVar()
        notice = Label(start_page_middle, textvariable = notice_var)
        notice_var.set("請輸入學號")
        notice.pack()        

        # middle widget
        self.std_id = Entry(start_page_middle,width = 20)
        self.std_id.pack()

        # middle widget
        btn_OK = Button(start_page_middle,text = "OK",width = 10,command = self.btn_OK_click)
        btn_OK.pack()

        # middle widget
        btn_guest = Button(start_page_middle,text = "非學生請點我",width = 10, command = self.btn_guest_click)
        btn_guest.pack()

        # middle frame setting
        start_page_middle.place(relx=0.5, rely=0.5, anchor=CENTER)


        # qeustions page setting
        self.questions_page = Frame(self.master)

        questions_label_var = StringVar()
        questions_label = Label(self.questions_page,font = ("微軟正黑體",30), textvariable = questions_label_var)
        questions_label_var.set(self.xls_stdlist. +"您好，請選擇欲服務項目")
        questions_label.pack(anchor="n", side = TOP)

        buttons_frame = Frame(self.questions_page)
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        services_cnt = 12

        for i in range(services_cnt//3):
            for j in range(3):
                cnt = i*3+j
                b = Button(buttons_frame,text = self.xls_services.values[cnt][0] ,width = 30 ,height = 2 ,font =("微軟正黑體",24),
                            command = lambda x = cnt : self.call_back_question(x))
                b.grid(row = i, column = j, padx = 40, pady = 40)

        btn_cancel = Button(self.questions_page,text = "取消", font =("微軟正黑體",25), command = self.to_start_page)
        btn_cancel.pack(anchor="n", side =LEFT)
                
        self.to_start_page()




if __name__ == "__main__":
    a = Gui_For_Office(Tk())
    a.master.mainloop()