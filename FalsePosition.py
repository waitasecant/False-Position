import math
def f(x): return math.cos(x)-x*math.exp(x)


def FalsePosition(x0, x1):
    return (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))


x0 = 0
x1 = 1
max = 100
tol = 0.00173
print("Method of False Position/ Linear Interpolation method \n")
for i in range(max):
    x2 = FalsePosition(x0, x1)
    if f(x0)*f(x2) < 0:
        test = True
        print(f"Iteration {i+1}: \nInitial interval is ({round(x0,6)},{round(x1,6)}) \nx{i} = {round(x0,6)}, f(x{i}) = {round(f(x0),6)}\t x{i+1} = {round(x1,6)}, f(x{i+1}) = {round(f(x1),6)}\tx{i+2} = {round(x2,6)}, f(x{i+2}) = {round(f(x2),6)}")
        if abs(x1-x2) < tol:
            print(
                f"Since |x{i+1}-x{i+2}| = {abs(round(x1-x2,6))}<{tol}, we have reached the stopping condition \n")
            break
        else:
            pass
        x1 = x2
        print(
            f"Since f(x{i})*f(x{i+2}) = {round(f(x0)*f(x2),6)}<0, New interval is ({round(x0,6)},{round(x1,6)}) \n")
        if abs(f(x2)) < tol:
            print(
                f"Since |f({round(x2,6)})| = {abs(round(f(x2),6))}<{tol}, we have reached the stopping condition \n")
            break
        else:
            pass
    elif f(x1)*f(x2) < 0:
        test = True
        print(f"Iteration {i+1}: \nInitial interval is ({round(x0,6)},{round(x1,6)}) \nx{i} = {round(x0,6)}, f(x{i}) = {round(f(x0),6)}\tx{i+1} = {round(x1,6)}, f(x{i+1}) = {round(f(x1),6)}\t x{i+2} = {round(x2,6)}, f(x{i+2}) = {round(f(x2),6)}")
        if abs(x2-x0) < tol:
            print(
                f"Since |x{i+2}-x{i}| = {abs(round(x2-x0,6))}<{tol}, we have reached the stopping condition \n")
            break
        else:
            pass
        x0 = x2
        print(
            f"Since f(x{i+1})*f(x{i+2}) = {round(f(x1)*f(x2),6)}<0, New interval is ({round(x0,6)},{round(x1,6)}) \n")
        if abs(f(x2)) < tol:
            print(
                f"Since |f({round(x2,6)})| = {abs(round(f(x2),6))}<{tol}, we have reached the stopping condition \n")
            break
        else:
            pass
else:
    test = False
    print("No root in the interval")
if test == True:
    print(
        f"The value of the root is {round(x2,6)} and the number of iterations required is {i+1}")
