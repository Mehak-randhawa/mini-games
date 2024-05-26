import random
import time
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

expr, answer = generate_problem()

wrong = 0
input("Press enter to start")
print("-------------------------------------")

start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
         guess = input("problem #" + str(i+1) + ": " + expr + " = ")
         if int(guess) == answer:
             print("Correct!")
             break
         else:
             print("Incorrect. Try again.")
         wrong = wrong + 1
end_time = time.time()
total_time = end_time - start_time
print("-------------------------------------")
print("nice work! you finished in " + str(total_time) + " seconds")