import net
from win10toast import ToastNotifier

while True:
    x = net.staff('localhost',6666)
    toaster = ToastNotifier()
    toaster.show_toast(u'{}'.format(x[0]), u'{}'.format(''.join(x[1:])))
    print(x)
