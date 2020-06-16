import socket, pandas

BUFSIZE = 4096
filename_excel = "net_test.xlsx"
def get_excel_col(staff_branch,data):
    for i in range(len(data['分機號碼'])):
        if data['分機號碼'][i] == staff_branch:
            print(i)
            return i
         
def get_staff_host(staff_branch):
    excel_data_df = pandas.read_excel(filename_excel, sheet_name='staff_host')
    data = excel_data_df.to_dict()
    col = get_excel_col(staff_branch,data)
    return get_excel_col_to_host(col,data)

def get_excel_col_to_host(col,data):
    return data['host'][col]
    
def host(data,staff_branch): #送data給 staff
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    staffhost, staffport = get_staff_host(staff_branch).split()
    print(staffhost, staffport)
    sock.connect((staffhost, int(staffport)))
    sock.send(data.encode('utf-8'))
    sock.close()

def staff(host, port):  # 等待資料傳送過來 接受完後關閉，接受後需在call一次  
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listeningSock.bind((host, port))
    listeningSock.listen(1)
    sock, sockname = listeningSock.accept()
    stu_data = sock.recv(BUFSIZE).decode('utf-8').split(" ")
    print(stu_data)
    return stu_data