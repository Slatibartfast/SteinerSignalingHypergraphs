Maximize
 obj: 700.0 Bx + 4.0 Dx + 3.0 Cx + 500.0 Ax - 2.0 Bd - 0.0 Dd - 1000000.0 Cd - 1.0 Ad - 5000.0 hyperedge2 - 3.0 hyperedge1
Subject To
 c44_hyperedge2: Cx - 1 hyperedge2 >= 0
 c43_hyperedge2: Dx - 1 hyperedge2 >= 0
 c44_hyperedge1: Bx + Ax - 2 hyperedge1 >= 0
 c43_hyperedge1: Dx - 1 hyperedge1 >= 0
 c45_A: Ad - Ax <= 0
 c45_B: Bd - Bx <= 0
 c45_C: Cd - Cx <= 0
 c45_D: Dd - Dx <= 0
 c46_B: Bd - Bx >= 0
 c46_D: Dd - Dx + hyperedge2 + hyperedge1 >= 0
 c46_C: Cd - Cx >= 0
 c46_A: Ad - Ax >= 0
Bounds
 Dx = 1
 Dd = 0
Binary
 Ax
 Bx
 Cx
 Dx
 Ad
 Bd
 Cd
 Dd
 hyperedge1
 hyperedge2
End
