Maximize
 obj: 0 + 3.0 Fx + 7.0 Mx + 21.0 Cx + 19.0 Ex + 16.0 Jx + 7.0 Lx + 24.0 Ix + 4.0 Hx + 8.0 Gx + 12.0 Dx + 14.0 Bx + 7.0 Ax + 2.0 Kx - 14.0 Fd - 0.0 Md - 1.0 Cd - 98.0 Ed - 24.0 Jd - 0.0 Ld - 12.0 Id - 4.0 Hd - 37.0 Gd - 16.0 Dd - 32.0 Bd - 10.0 Ad - 0.0 Kd - 14.0 e2 - 8.0 e9 - 14.0 e5 - 19.0 e11 - 57.0 e4 - 5.0 e3 - 12.0 e10 - 4.0 e1 - 9.0 e7 - 45.0 e12 - 31.0 e8 - 33.0 e6
Subject To
 c44_e2: Bx - 1 e2 <= 0
 c43_e2: Fx - 1 e2 <= 0
 c44_e9: Hx - 1 e9 <= 0
 c43_e9: Lx - 1 e9 <= 0
 c44_e5: Ex - 1 e5 <= 0
 c43_e5: Hx + Lx - 2 e5 <= 0
 c44_e11: Lx - 1 e11 <= 0
 c43_e11: Hx + Kx - 2 e11 <= 0
 c44_e4: Ex + Dx - 2 e4 <= 0
 c43_e4: Hx + Kx - 2 e4 <= 0
 c44_e3: Cx - 1 e3 <= 0
 c43_e3: Fx + Gx - 2 e3 <= 0
 c44_e10: Ix - 1 e10 <= 0
 c43_e10: Mx + Lx - 2 e10 <= 0
 c44_e1: Ax - 1 e1 <= 0
 c43_e1: Bx + Dx - 2 e1 <= 0
 c44_e7: Ix - 1 e7 <= 0
 c43_e7: Jx - 1 e7 <= 0
 c44_e12: Ex - 1 e12 <= 0
 c43_e12: Bx - 1 e12 <= 0
 c44_e8: Jx - 1 e8 <= 0
 c43_e8: Ix - 1 e8 <= 0
 c44_e6: Fx + Gx - 2 e6 <= 0
 c43_e6: Ix - 1 e6 <= 0
 c45_A: Ad - Ax <= 0
 c45_B: Bd - Bx <= 0
 c45_C: Cd - Cx <= 0
 c45_D: Dd - Dx <= 0
 c45_E: Ed - Ex <= 0
 c45_F: Fd - Fx <= 0
 c45_G: Gd - Gx <= 0
 c45_H: Hd - Hx <= 0
 c45_I: Id - Ix <= 0
 c45_J: Jd - Jx <= 0
 c45_K: Kd - Kx <= 0
 c45_L: Ld - Lx <= 0
 c45_M: Md - Mx <= 0
 c46_F: Fd - e2 - e3 >= 1
 c46_M: Md - e10 >= 1
 c46_C: Cd >= 1
 c46_E: Ed >= 1
 c46_J: Jd - e7 >= 1
 c46_L: Ld - e5 - e10 - e9 >= 1
 c46_I: Id - e8 - e6 >= 1
 c46_H: Hd - e5 - e4 - e11 >= 1
 c46_G: Gd - e3 >= 1
 c46_D: Dd - e1 >= 1
 c46_B: Bd - e1 - e12 >= 1
 c46_A: Ad >= 1
 c46_K: Kd - e4 - e11 >= 1
Bounds
 Mx = 1
 Md = 0
 Lx = 1
 Ld = 0
 Kx = 1
 Kd = 0
Binary
 Ax
 Bx
 Cx
 Dx
 Ex
 Fx
 Gx
 Hx
 Ix
 Jx
 Kx
 Lx
 Mx
 Ad
 Bd
 Cd
 Dd
 Ed
 Fd
 Gd
 Hd
 Id
 Jd
 Kd
 Ld
 Md
 e1
 e10
 e11
 e12
 e2
 e3
 e4
 e5
 e6
 e7
 e8
 e9
End
