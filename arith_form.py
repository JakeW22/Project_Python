# Jake Wakerley

"""
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
"""
import re

def arithmetic_arranger(problems, solve = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
        if(re.search("[^\s0-9.+-]", problem)): # Searches for values that are not whitespace
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error: Numbers cannot be more than four digits."
        
        sum = ""
        if (operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))
        
        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ""
        res = (str(sum).rjust(length))
        for s in range(length):
            line += "-"
        
        if problem != problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            sumx += res + "    "
        else:
            first += top
            second += bottom
            lines += line
            sumx += res
        

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first = first + "\n" + second + "\n" + lines
    return string

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))