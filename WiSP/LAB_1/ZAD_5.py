import matplotlib.pyplot as plt
import numpy as np

def try_input(prompt, valid_values):
  user_input = input(prompt)
  while user_input not in valid_values:
    user_input = input(prompt)
  return user_input

x_left = int(input("Left limit for x (default 0): ") or 0) # ad. 3
x_right = int(input("Right limit for x (default 10): ") or 10) # ad. 3

graph_color = input("Graph Color (default 'black'): ") or "black" # ad.4

x = np.linspace(x_left, x_right, 100) # ad. 1: 10 -> 100

_, ax = plt.subplots(figsize=(10, 5))

funcs_dict = {
  "x":      lambda x, ax: ax.plot(x, x, color=graph_color, label="y=x"), 
  "sin(x)": lambda x, ax: ax.plot(x, np.sin(x), label="y=sin(x)"), 
  "cos(x)": lambda x, ax: ax.plot(x, np.cos(x), label="y=cos(x)"), 
  "x^3":    lambda x, ax: ax.plot(x, x**3, label="y=x^3")
}

for func in funcs_dict.keys():
  if try_input(f"Show {func}? y/n: ", ["y","n"]) == "y": 
    funcs_dict[func](x,ax)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Wykres")
ax.legend()
plt.show()