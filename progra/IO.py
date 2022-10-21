'''# import the library pulp as p 
import pulp as p



# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem1', p.LpMinimize)  

# Create problem Variables  
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 

# Objective Function 
Lp_prob += 3 * x + 5 * y    

# Constraints: 
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

# Display the problem 
print(Lp_prob) 

status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 

# Printing the final solution 
print(p.value(x), p.value(y), p.value(Lp_prob.objective)) '''

import pulp as pl


if __name__ == "__main__":
    
    # define the problem
    prob = pl.LpProblem("Empleados", pl.LpMinimize)
    
    # declare some variables
    x1 = pl.LpVariable("x1", lowBound=0, cat='Integer')
    x2 = pl.LpVariable("x2", lowBound=0, cat='Integer')
    x3 = pl.LpVariable("x3", lowBound=0, cat='Integer')
    x4 = pl.LpVariable("x4", lowBound=0, cat='Integer')
    x5 = pl.LpVariable("x5", lowBound=0, cat='Integer')
    x6 = pl.LpVariable("x6", lowBound=0, cat='Integer')
    x7 = pl.LpVariable("x7", lowBound=0, cat='Integer')

    # objective function - minimize value of empleados 
    prob += 500*(x1+x2+x3+x4+x5+x6+x7)
    
    # constraint - weight of objects cannot exceed 15
    prob += x1+x4+x5+x6+x7 >= 16
    prob += x1+x2+x5+x6+x7 >= 15
    prob += x1+x2+x3+x6+x7 >= 16
    prob += x1+x2+x3+x4+x7 >= 19
    prob += x1+x2+x3+x4+x5 >= 14
    prob += x2+x3+x4+x5+x6 >= 12
    prob += x3+x4+x5+x6+x7 >= 18

    print(prob)

    status = prob.solve()  # solve using the default solver, which is cbc
    print(pl.LpStatus[status])  # print the human-readable status
    print('valor óptimo:{}'.format(int(pl.value(prob.objective))))
    
    # print the values
    print("Lunes", pl.value(x1))
    print("Martes", pl.value(x2))
    print("Miercoles", pl.value(x3))
    print("Jueves", pl.value(x4))
    print("Viernes", pl.value(x5))
    print("Sabado", pl.value(x6))
    print("Domingo", pl.value(x7))
    