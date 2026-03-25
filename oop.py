# class HinhChuNhat:  #Khai báo lớp class bao gồm có chiều dài,chiều rộng
#     def __init__(self, chieuDai, chieuRong):
#         self.chieuDai = chieuDai
#         self.chieuRong = chieuRong
#     def chu_vi(self):                   #yêu cầu đề bài 1  tính P 
#         return (self.chieuDai+ self.chieuRong)*2 
#     def dien_tich(self):        #yêu cầu đề bài 2 : tính S 
#         return self.chieuRong * self.chieuDai
# #SỬ DỤNG IN RA MÀN HÌNH 
# hcn = HinhChuNhat(5,2)
# print('Dien tich cua hcn :',hcn.dien_tich())        # LỆNH : print("...",object.hành vi1())
# print("Chu vi cua hcn : ", hcn.chu_vi())

class BANK_ACC:
    def __init__(self, stk, ten, so_du):
        self.stk = stk
        self.ten = ten
        self.so_du = so_du
    def nap_tien(self, so_tien):
        if (so_tien <= 0):
            print("VUI LONG NHAP LAI SO TIEN MUON NAP")
        else :
            print("NAP TIEN THANH CONG")
        return so_tien + self.so_du  # đoạn này kbt code sao 
    def rut_tien(self,so_tien):
        if so_tien <= 0:
         print("So tien khong hop le")
        elif so_tien > self.so_du:
         print("Khong du tien")
        else:
         self.so_du -= so_tien
        print("Rut tien thanh cong")
    def chuyen_tien(self, so_tien, tai_khoan_nhan):
        if so_tien <= 0:
         print("So tien khong hop le")
        elif so_tien > self.so_du:
         print("Khong du tien")
        else:
         self.rut_tien(so_tien)
         tai_khoan_nhan.nap_tien(so_tien)
    def hien_thi(self):
        print("So TK:", self.stk)
        print("Ten:", self.ten)
        print("So du:", self.so_du)
tk01 = BANK_ACC(22334455, "NGUYỄN MINH TRÂM",5000 )
tk02 = BANK_ACC(11223344, "NGUYỄN MINH TRANG",1000)
tk01.nap_tien(3000)
tk01.rut_tien(1000)
tk01.chuyen_tien(200,tk02)
tk01.hien_thi()
tk02.hien_thi()