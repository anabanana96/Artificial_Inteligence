# SEND+MORE=MONEY е криптоаритметичка загатка, што значи дека станува збор за наоѓање цифри кои ги заменуваат буквите за да се направи математичкиот израз вистинит. 
# Секоја буква во проблемот претставува една цифра (0–9). Две букви не можат да ја претставуваат истата цифра. Кога буквата се повторува, тоа значи дека цифрата се повторува во решението. 
  
from constraint import *
def check_sum(s, e, n, d, m, o, r, y):
    return ((s*1000 + e*100 + n*10 + d) + (m*1000 + o*100 + r*10 + e)) == \
        (m*10000 + o*1000 + n*100 + e*10 + y)


money_problem = Problem()

variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]

money_problem.addVariables(variables, range(0,10))
money_problem.addConstraint(AllDifferentConstraint())
money_problem.addConstraint(check_sum, variables)

print(money_problem.getSolution())
