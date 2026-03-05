import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def find_intercepts_analytical():
    """
    Find intercepts using symbolic mathematics
    """

    # Define symbolic variable
    x = sp.Symbol('x')

    # Define the function
    f_expr = 2 * x ** 3 - x



    # Find x-intercepts (solve f(x) = 0)
    print("\n📌 Finding x-intercepts (solving f(x) = 0):")
    print(f"   Equation: {f_expr} = 0")

    # Factor the expression
    factored = sp.factor(f_expr)
    print(f"   Factored form: {factored} = 0")

    # Solve
    solutions = sp.solve(f_expr, x)
    print(f"\n   Solutions:")
    for i, sol in enumerate(solutions):
        print(f"   {i + 1}. x = {sol}")
        print(f"      Point: ({sol}, 0)")

    # Find y-intercept (x = 0)
    y_int = f_expr.subs(x, 0)
    print(f"\n📌 y-intercept (x = 0):")
    print(f"   y = {f_expr.subs(x, 0)}")
    print(f"   Point: (0, {y_int})")

    # Visual verification
    plt.figure(figsize=(12, 8))

    # Convert to numerical function for plotting
    f_num = sp.lambdify(x, f_expr, 'numpy')

    x_vals = np.linspace(-2, 2, 400)
    y_vals = f_num(x_vals)

    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='y = 2x³ - x')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

    # Plot intercepts
    for sol in solutions:
        plt.plot(float(sol), 0, 'ro', markersize=8)
        plt.annotate(f'({float(sol):.3f}, 0)', (float(sol), 0),
                     xytext=(10, 10), textcoords='offset points')

    plt.plot(0, float(y_int), 'ro', markersize=8)
    plt.annotate(f'(0, {float(y_int)})', (0, float(y_int)),
                 xytext=(10, -20), textcoords='offset points')

    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Analytical Solution: y = 2x³ - x', fontsize=14, fontweight='bold')
    plt.legend()
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()

    return solutions, y_int


# Run the analytical solution
solutions, y_int = find_intercepts_analytical()