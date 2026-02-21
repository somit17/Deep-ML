import numpy as np

a = np.array([[1, 3]])
b = np.array([[4, 5]])

print(f"Shape = {a.shape}")
print(f"Shape = {b.shape}")

if a.shape!=b.shape:
    print("-1")
print(f"ADD = *{a+b}")
c = a+b
print(*c.tolist())