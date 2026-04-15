#CLASS DOG 
class ConCho:
  def __init__(self, ten, gioi_tinh,mau_sac):
    self.ten = ten
    self.gioi_tinh = gioi_tinh
    self.mau_sac = mau_sac
  def __str__(self):
    return f"Tên chó: {self.ten} | Giới tính: {self.gioi_tinh} | Màu sắc: {self.mau_sac}"
A = ConCho("Alaska", "đực", "đen trắng")
print(A)

#CLASS Ô TÔ 
class Car:
    def __init__(self, ten, loai_xe,gia_thanh):
        self.ten = ten
        self.loai_xe = loai_xe
        self.gia_thanh = gia_thanh
    def __str__(self):
        return (f"Tên xe:{self.ten} | Dòng xe:{self.loai_xe} | Gia thành:{self.gia_thanh}")
F = Car("Mercedes", "xe thể thao", ">= 1 tỷ")
print(F)

#CLASS TÀI KHOẢN : 
class BankAcc:
    def __init__(self, ten, stk, so_du):
        self.ten = ten
        self.stk = stk 
        self.so_du = so_du
    def __str__(self):
        return(f"Tên chủ tài khoản :{self.ten} | Số tài khoản :{self.stk} | Số dư hiện tại:{self.stk}")
TK01 = BankAcc(" NGUYEN MINH TRAM ", "1736597", "10000000000000 VND")
print(TK01)

