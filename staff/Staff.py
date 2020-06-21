import net
from win10toast import ToastNotifier

ip_port = []
with open('staff_ip_port.txt') as f:
    ip_port = f.read().split(' ')

print(ip_port)


while True:
    x = net.staff(ip_port[0],int(ip_port[1]))
    toaster = ToastNotifier()
    toaster.show_toast(u'{}'.format(x[0]), u'{}'.format(''.join(x[1:])))
    print(x)
