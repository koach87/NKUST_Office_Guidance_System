from tkinter import *

class Gui_For_Office:

    def __init__(self,master):
        self.master = master
        self.initUI()

    def start_page(self):
        pass

    def questions_page(self):
        pass

    def click_ok(self):
        self.start_page.pack_forget()
        self.test_btn = Button()


    def initUI(self):
        #set UI 
        self.master.geometry("300x300")
        self.master.title("Office Guidance System")
        self.start_page()

        #start page setting
        self.start_page = Frame(self.master, width=300, height=300, bg="gray")
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
        btn_OK = Button(start_page_middle,text = "OK",width = 10,command = self.click_ok)
        btn_OK.pack()

        #middle widget
        btn_guest = Button(start_page_middle,text = "非學生請點我",width = 10)
        btn_guest.pack()

        #middle frame setting
        start_page_middle.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #start page setting
        self.start_page.pack(expand=True, fill=BOTH)



if __name__ == "__main__":
    a = Gui_For_Office(Tk())
    a.master.mainloop()