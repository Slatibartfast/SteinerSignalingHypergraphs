Maximize
 obj: 3.0 Cx + 500.0 Ax + 4.0 Dx + 700.0 Bx - 1000000.0 Cd - 1.0 Ad - 0.0 Dd - 2.0 Bd + 0.0Cc + 0.0Ac + 0.0Dc + 0.0Bc + 0.0 AToA + 0.0 CToB + 0.0 DToC + 0.0 BToB + 0.0 AToB + 0.0 CToC + 0.0 BToA + 0.0 BToC + 0.0 AToD + 0.0 DToD + 0.0 AToC + 0.0 CToD + 0.0 BToD + 0.0 DToB + 0.0 CToA + 0.0 DToA - 3.0 hyperedge1 - 5000.0 hyperedge2
Subject To
 c44_hyperedge1: Ax + Bx - 2 hyperedge1 >= 0
 c43_hyperedge1: Dx - 1 hyperedge1 >= 0
 c44_hyperedge2: Cx - 1 hyperedge2 >= 0
 c43_hyperedge2: Dx - 1 hyperedge2 >= 0
 c45_A: Ad - Ax <= 0
 c45_B: Bd - Bx <= 0
 c45_C: Cd - Cx <= 0
 c45_D: Dd - Dx <= 0
 c46_C: Cd - Cx >= 0
 c46_A: Ad - Ax >= 0
 c46_D: Dd - Dx + hyperedge1 + hyperedge2 >= 0
 c46_B: Bd - Bx >= 0
 dc1_A: Ac - Ax <= 0
 dc1_B: Bc - Bx <= 0
 dc1_C: Cc - Cx <= 0
 dc1_D: Dc - Dx <= 0
 dc2_C: Cc - Cx + hyperedge2 >= 0
 dc2_A: Ac - Ax + hyperedge1 >= 0
 dc2_D: Dc - Dx >= 0
 dc2_B: Bc - Bx + hyperedge1 >= 0
 dc3_CToC: Cc + Cd + CToC <= 2
 dc3_CToA: Cc + Ad + CToA <= 2
 dc3_CToD: Cc + Dd + CToD <= 2
 dc3_CToB: Cc + Bd + CToB <= 2
 dc3_AToC: Ac + Cd + AToC <= 2
 dc3_AToA: Ac + Ad + AToA <= 2
 dc3_AToD: Ac + Dd + AToD <= 2
 dc3_AToB: Ac + Bd + AToB <= 2
 dc3_DToC: Dc + Cd + DToC <= 2
 dc3_DToA: Dc + Ad + DToA <= 2
 dc3_DToD: Dc + Dd + DToD <= 2
 dc3_DToB: Dc + Bd + DToB <= 2
 dc3_BToC: Bc + Cd + BToC <= 2
 dc3_BToA: Bc + Ad + BToA <= 2
 dc3_BToD: Bc + Dd + BToD <= 2
 dc3_BToB: Bc + Bd + BToB <= 2
Bounds
 Dx = 1
 Dd = 0
 AToA = 1
 CToB = 0
 DToC = 0
 BToB = 1
 AToB = 0
 CToC = 1
 BToA = 0
 BToC = 0
 AToD = 1
 DToD = 1
 AToC = 0
 CToD = 1
 BToD = 1
 DToB = 0
 CToA = 0
 DToA = 0
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
 AToA
 CToB
 DToC
 BToB
 AToB
 CToC
 BToA
 BToC
 AToD
 DToD
 AToC
 CToD
 BToD
 DToB
 CToA
 DToA
End
