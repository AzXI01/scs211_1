#nocopyright--forstudycase
#python <glue.s>



#ยากเพราะโง่หรือไม่ได้เรียนก็ไม่รู้


# x = สำนักพิมพ์ = (Thairat) (Matichon) (Siam) (Thaipost) 
#c = ยอดขายเดือนมกรา
#f = ยอดขายเดือนกุมภา
##-------------------------------------------------##

#ข้อ1 ประกาศตัวแปร
from tkinter.tix import InputOnly


g = ['Thairat', 'Matichon', 'Siam', 'Thaipost']

#ข้อ2 ประกาศตัวแปลเดือนมก
h = ( '100', '200' , '50' ,'90')

#ข้อ3 ประกาศตัวแปลเดือนกุม
b = ('120', '250' , '90' ,'100')

##โจทย์ข้อ4 แสดงยอดขายทั้ง2เดือนขอสำนัก thaipost
print(g[3])
print("jansold")
print(h[3])
print("febsold")
print(b[3])

#ข้อ5
#('Newpapers')
n = []
a = int
sum = 0
while a != 0:
    a = int(InputOnly('enter num'))
    n.append(a)

del n[-1]
cntSum = len(n)
##-------------------------------------------------##
#!! Tuple จะเป็น (....)กันสับสน    !!ถ้ามันคำสั่งให้คำใน tupleเปลี่ยนแปลง code จะERR
#!! list จะเป็น [...] 









