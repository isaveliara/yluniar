import math
import re

#function to normalize the equation: reordering terms, replacing superscripts, etc...
def normalize_equation(equation):
    equation = equation.replace('²', '^2')
    equation = re.sub(r'(\d)(x)', r'\1*\2', equation)
    equation = equation.replace(" ", "")
    return equation

#function to extract coefficients from different types of quadratic equations
def extract_coefficients(equation):
    #match for ax² + bx + c = 0 (general quadratic)
    match_general = re.match(r'([+-]?\d*)\*?x\^2\s*([+-]?\d*)\*?x\s*([+-]?\d+)?\s*=0', equation)

    #match for ax² + bx = 0 (quadratic without constant)
    match_b_only = re.match(r'([+-]?\d*)\*?x\^2\s*([+-]?\d*)\*?x\s*=0', equation)

    #match for ax² + c = 0 (quadratic without linear term)
    match_c_only = re.match(r'([+-]?\d*)\*?x\^2\s*([+-]?\d+)\s*=0', equation)
    #match for bx + c = 0 (linear equation)
    match_linear = re.match(r'([+-]?\d*)\*?x\s*([+-]?\d+)\s*=0', equation)

    #if its a general form: ax^2 + bx + c = 0
    if match_general:
        a = int(match_general.group(1)) if match_general.group(1) not in ["", "+", "-"] else (1 if match_general.group(1) in ["", "+"] else -1)
        b = int(match_general.group(2)) if match_general.group(2) not in ["", "+", "-"] else (1 if match_general.group(2) in ["", "+"] else -1)
        c = int(match_general.group(3)) if match_general.group(3) else 0
        return a, b, c

    #if its of the form: ax² + bx = 0
    elif match_b_only:
        a = int(match_b_only.group(1)) if match_b_only.group(1) not in ["", "+", "-"] else (1 if match_b_only.group(1) in ["", "+"] else -1)
        b = int(match_b_only.group(2)) if match_b_only.group(2) not in ["", "+", "-"] else (1 if match_b_only.group(2) in ["", "+"] else -1)
        return a, b, 0

    #if its of the form: ax² + c = 0
    elif match_c_only:
        a = int(match_c_only.group(1)) if match_c_only.group(1) not in ["", "+", "-"] else (1 if match_c_only.group(1) in ["", "+"] else -1)
        c = int(match_c_only.group(2)) if match_c_only.group(2) else 0
        return a, 0, c

    #if its a linear equation: bx + c = 0
    elif match_linear:
        b = int(match_linear.group(1)) if match_linear.group(1) not in ["", "+", "-"] else (1 if match_linear.group(1) in ["", "+"] else -1)
        c = int(match_linear.group(2)) if match_linear.group(2) else 0
        return 0, b, c

    #if its a constant equation like 4 = 0
    elif re.match(r'([+-]?\d+)\s*=0', equation):
        return 0, 0, int(re.match(r'([+-]?\d+)\s*=0', equation).group(1))

    else:
        raise ValueError("The input equation is not in a valid format.")

#function to solve quadratic equations or simpler cases
def solve_equation(a, b, c, steps):
    if a != 0:    #Quadratic equation
        delta = b**2 - 4*a*c
        steps.append(f"Delta: Δ = {b}^2 - 4*{a}*{c}")
        steps.append(f"            Δ = {delta}")
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            steps.append("Two solutions: {x' = "+f"{x1}"+"; x'' = "+f"{x2}"+"}")
        elif delta == 0:
            x = (-b) / (2 * a)
            steps.append(f"One solution: x = {x}")
        else:
            steps.append("No real solutions!")
    elif b != 0:    #Linear equation
        x = -c / b
        steps.append(f"Linear solution: x = {x}")
    elif c == 0:    #Trivial equation (0 = 0)
        steps.append("Infinite solutions (0 = 0).")
    else:
        steps.append("No solution!")

#function to process the equation with step recording
def process_equation_with_steps(equation):
    steps = []
    try:
        steps.append(f"Input: {equation}")
        normalized_eq = normalize_equation(equation)
        steps.append(f"Formalized: {normalized_eq}")
        a, b, c = extract_coefficients(normalized_eq)
        
        if a == 0 and b == 0 and c != 0:
            steps.append("No solution! (Invalid constant equation)")
        else:
            steps.append(f"Type of equation: {'Quadratic' if a != 0 else 'Linear'}")
            solve_equation(a, b, c, steps)
    except ValueError as e:
        steps.append(str(e))
    
    return steps
