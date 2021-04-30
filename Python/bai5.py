class chuoi():
    def __init__(self):
        self.s=""
    def Input(self):
        self.s=raw_input('Nhap chuoi : ')
    def Output(self):
        print 'Chuoi cuyen thanh chu hoa la : ',self.s.upper()
bai5=chuoi()
bai5.Input()
bai5.Output()
