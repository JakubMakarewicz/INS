import matplotlib.pyplot as plt
import numpy as np

def try_input(prompt, validator):
  user_input = input(prompt)
  while not validator(user_input):
    user_input = input(prompt)
  return user_input

T = float(input("Please provide T: "))
x1_0 = float(input("Please provide x1_0: "))
x2_0 = float(input("Please provide x2_0: "))
x3_0 = float(input("Please provide x3_0: "))

w1c = try_input("Please provide w1: complex? (y/n)", lambda _input: _input in ['y', 'n']) == 'y'
if w1c:
  w1s = {}
  _w1 = float(input("Please provide w1: "))
  w1s[0] = _w1
  while try_input("Continue? (y/n)", lambda _input: _input in ['y', 'n']) == 'y':
    _w1 = float(input("Please provide w1: "))
    _limit = float(try_input("Please provide w1 lower-limit: ", lambda _input: float(_input) > list(w1s.keys())[-1]))
    w1s[_limit] = _w1

  w1 = lambda n: w1s[next(x for x in list(w1s.keys())[::-1] if x <= n)]
else:
  _w1 = float(input("Please provide w1: "))
  w1 = lambda _: _w1

w2c = try_input("Please provide w2: complex? (y/n)", lambda _input: _input in ['y', 'n']) == 'y'
if w2c:
  w2s = {}
  _w2 = float(input("Please provide w2: "))
  w2s[0] = _w2
  while try_input("Continue? (y/n)", lambda _input: _input in ['y', 'n']) == 'y':
    _w2 = float(input("Please provide w2: "))
    _limit = float(try_input("Please provide w2 lower-limit: ", lambda _input: float(_input) > list(w2s.keys())[-1]))
    w2s[_limit] = _w2

  w2 = lambda n: w2s[next(x for x in list(w2s.keys())[::-1] if x <= n)]
else:
  _w2 = float(input("Please provide w2: "))
  w2 = lambda _: _w2

def pos(n):
  def next_x(t,x,r):
    k1 = ((x + T * w1(t) * np.cos(r)) - x)
    k2 = ((x*k1/2 + T * w1(t+T/2) * np.cos(r)) - x*k1/2)
    k3 = ((x*k2/2 + T * w1(t+T/2) * np.cos(r)) - x*k2/2)
    k4 = ((x*k3 + T * w1(t+T) * np.cos(r)) - x*k3)
    return x + 1/6 *(k1 + 2*k2 + 2*k3 + k4)
  
  def next_y(t,y,r):
    k1 = ((y + T * w1(t) * np.sin(r)) - y)
    k2 = ((y*k1/2 + T * w1(t+T/2) * np.sin(r)) - y*k1/2)
    k3 = ((y*k2/2 + T * w1(t+T/2) * np.sin(r)) - y*k2/2)
    k4 = ((y*k3 + T * w1(t+T) * np.sin(r)) - y*k3)
    return y + 1/6 *(k1 + 2*k2 + 2*k3 + k4) 
  
  def next_r(t,r):
    k1 = ((r + T * w2(t)) - r)
    k2 = ((r*k1/2 + T * w2(t)) - r*k1/2)
    k3 = ((r*k2/2 + T * w2(t)) - r*k2/2)
    k4 = ((r*k3 + T * w2(t)) - r*k3)
    return r + 1/6 *(k1 + 2*k2 + 2*k3 + k4)   

  x = x1_0
  y = x2_0
  r = x3_0
  yield (x,y,r)
  for t in n:
    x = next_x(t,x,r)
    y = next_y(t,y,r)
    r = next_r(t,r)

    yield (x,y,r)

_, ax = plt.subplots(figsize=(8, 8))
n = np.linspace(0, 1000, 1000)
positions = list(pos(n))

plt.scatter(
  list(map(lambda x: x[0], positions)), 
  list(map(lambda x: x[1], positions)))

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Wykres")
ax.legend()
plt.show()