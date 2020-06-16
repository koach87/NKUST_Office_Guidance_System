from tkinter import *
import pandas as pd

class Gui_For_Office:

    def __init__(self,master):
        self.master = master
        self.initUI()

    def cancel(self):
        self.btn_cancel.pack(anchor="n", side =LEFT)
        self.to_start_page()

    def to_start_page(self):
        self.std_id.delete(0, 'end')
        self.questions_page.pack_forget()
        self.tchr_page.pack_forget()
        self.std_page.pack_forget()
        self.start_page.place(relx=0.5, rely=0.5, anchor=CENTER)

    def to_questions_page(self):
        self.btn_cancel.pack()
        self.start_page.pack_forget()
        self.questions_page.place(relx=0.5, rely=0.5, anchor=CENTER)

    def to_student_page(self):
        self.start_page.pack_forget()
        self.btn_cancel.pack()
        self.std_page.place(relx=0.5, rely=0.5, anchor=CENTER)

# ================================================================================
    # click action
    def click_tchr(self):
        pass

    def click_std(self):
        self.to_student_page()

    def click_guest(self):
        print('guest')
        self.to_questions_page()


    def click_std_OK(self):
        print(self.std_id.get())
        self.to_questions_page()

    def call_back_question(self,question_index):
        print(self.xls_services.values[question_index][0])
        print(self.xls_services.values[question_index][2])
        import net
        net.host(self.xls_services.values[question_index][0],int(self.xls_services.values[question_index][2]))


    def initUI(self):
        # get services
        self.xls_services = pd.read_excel("GUI_services.xlsx", sheet_name= 0 )

        # get stdlist
        self.xls_stdlist = pd.read_excel("GUI_stdlist.xlsx", sheet_name= 0 )
        self.xls_stdlist = self.xls_stdlist.set_index('std_num').T.to_dict('list')

        # set UI 
        self.master.iconbitmap("nkust.ico")
        self.master.state("zoom")
        self.master.title("Office Guidance System")
 
# ================================================================================
        # cancel frame
        cancel_frame = Frame(self.master, bg = "green").pack()
        self.btn_cancel = Button(cancel_frame, text = "取消", font = ("微軟正黑體",20))

# ================================================================================
        # start page setting
        self.start_page = Frame(self.master, bg="gray")
        start_page_middle = Frame(self.start_page,bg = "white")

        # Label of notice
        Label(start_page_middle, text = "請選擇身分").pack()

        # middle widget
        self.btn_std = Button(start_page_middle,text = "學生",width = 25, command = self.click_std)
        self.btn_std.pack()

        # middle widget
        self.btn_oth = Button(start_page_middle,text = "其他",width = 25, command = self.click_guest)
        self.btn_oth.pack()

        # middle widget
        self.btn_tchr = Button(start_page_middle,text = "導師",width = 25, command = self.click_tchr)
        self.btn_tchr.pack()

        # middle frame setting
        start_page_middle.pack()
        # start_page_middle.place(relx=0.5, rely=0.5, anchor=CENTER)

# ================================================================================
        # student page
        self.std_page = Frame(self.master)

        Label(self.std_page,text = "請輸入學號").pack()

        self.std_id = Entry(self.std_page,width = 50)
        self.std_id.pack()

        # middle widget
        std_btn_OK = Button(self.std_page,text = "確定",width = 25,command = self.click_std_OK)
        std_btn_OK.pack()

# ================================================================================
        # teacher page
        self.tchr_page = Frame(self.master)
        Label(self.tchr_page, text = "請選擇所屬科系").pack()
        


# ================================================================================
        # qeustions page
        self.questions_page = Frame(self.master)

        self.questions_label_var = StringVar()

        questions_label = Label(self.questions_page, font = ("微軟正黑體",30), textvariable = self.questions_label_var)
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

        
        # # nkust image
        # im = PhotoImage(file = "nkust.gif")
        # aa = Label(self.questions_page, image = im)
        # aa.pack()
                
        self.to_start_page()
    




if __name__ == "__main__":
    a = Gui_For_Office(Tk())
    a.master.mainloop()