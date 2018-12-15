import sympy

#差分商補間(Newtonian interpolation)
#ダサい初期値設定
x0 = -1
x1 = 0
x2 = 1
x3 = 2
F0 = 4
F1 = -2
F2 = -1.2
F3 = -0.52
f1_1 = (F0 - F1) / (x1 - x0)
f1_2 = (F1 - F2) / (x2 - x1)
f1_3 = (F3 - F2) / (x3 - x2)
f2_1 = (f1_2 - f1_1) / (x2 - x0)
f2_2 = (f1_3 - f1_2) / (x3 - x1)
f3_1 = (f2_2 - f2_1) / (x3 - x0)

#Declare variable x
x = sympy.Symbol('x')

F_2 = F0 + (x - x0)*f1_1 + (x - x0)*(x - x1)*f2_1
print('ニュートンの二次多項式 F(x) =', F_2)

#Expand expression
print('ニュートンの二次多項式 F(x) =',sympy.expand(F_2))

F_3 = F0 + (x - x0)*(f1_1) + (x - x0)*(x - x1)*f2_1 + (x - x0)*(x - x1)*(x - x2)*(f3_1)
print('ニュートンの三次多項式 F(x) =',F_3)

print('ニュートンの三次多項式 F(x) =',sympy.expand(F_3))
