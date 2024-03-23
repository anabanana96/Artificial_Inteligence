from constraint import *
def not_attacking(q1,q2):
    return q1[0]!=q2[0] and q1[1]!=q2[1] and abs(q1[0]-q2[0])!=abs(q1[1]-q2[1])

queens_problem = Problem()
n = int(input())
variables = []
domain = []

for i in range(n):
    variables.append(f"Q{i+1}")

for i in range(0,n):
    for j in range(0,n):
        domain.append((i,j))

queens_problem.addVariables(variables, domain)
for q1 in variables:
    for q2 in variables:
        if q1!=q2:
            queens_problem.addConstraint(not_attacking, (q1,q2))
print(queens_problem.getSolution())
