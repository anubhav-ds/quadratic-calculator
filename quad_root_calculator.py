import cmath
from sympy.plotting import plot
from sympy import symbols

def roots(a, b,c):
    try:
        D = cmath.sqrt(b**2 - 4*a*c)
        x1 = (-b + D) / (2*a)
        x2 = (-b - D) / (2*a)

        print(f"The roots are {x1} and {x2}")
    except:
        raise Exception("Input is not a valid number, please try again.")
    
def plot_graph(a, b, c):
    x = symbols('x')
    plot(a*x**2 + b*x + c, (x, -10, 10), title='Quadratic Function', ylabel='f(x)', xlabel='x', show=True)

def main():
    while True:
        print("Welcome to the Quadratic Root Calculator!")
        try:
            a = float(input("Enter the coefficient a: "))
            b = float(input("Enter the coefficient b: "))
            c = float(input("Enter the coefficient c: "))
            roots(a, b, c)
            plot_graph(a, b, c)

            done = input("Do you want to calculate again? (yes/no): ").strip().lower()
            if done in ['y', 'yes']:
                continue
            elif done in ['n', 'no']:
                print("Thank you for using the Quadratic Root Calculator!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no' next time, calculator restarting.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            break

main()
        



