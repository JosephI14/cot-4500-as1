import math

import numpy


# Question 1: Use double precision, calculate the resulting values (format to 5 decimal places)
def double_precison(fin: float, man: float):
  fin = fin - 1023
  fin = 2**(fin)
  man = 1 + man
  precise = fin * man
  return precise


# Question 2: Repeat exercise 1 using three-digit chopping arithmetic
def chopped(digit: float, decimal: int):
  value = 10**decimal
  return math.floor((digit * value) / value) * .001


# Question 3: Repeat exercise 1 using three-digit rounding arithmetic
def rounding(roun: float):
  value = 10**3
  return math.ceil(roun * value) / value


def function(v: float):
  return (v * v * v) + (4 * (v * v)) - 10


def function2(w: float):
  return 3 * (w * w) + (8 * w)


def bisection(x: float, y: float):
  tolerence = .0001
  max_iter = 20
  count_iter = 0

  while count_iter <= max_iter:
    midpoint = (x + y) / 2

    if abs(x - y) <= tolerence:
      return count_iter
    elif numpy.sign(function(a)) != numpy.sign(function(midpoint)):
      y = midpoint
    elif numpy.sign(function(b)) != numpy.sign(function(midpoint)):
      x = midpoint

    count_iter = count_iter + 1

  return count_iter


def function3(new: float):
  tolerence = .0001
  comp = new

  rel = function(new) / function1(new)

  count_new = 1

  while abs(rel) >= tolerence:
    comp = comp - rel
    count_new = 1 + count_new
    rel = function(comp) / function2(comp)

  return


# Code for getting the values to compile
if __name__ == "__main__":
  s = float(0b10000000111)
  c = float(0b11101010111001)

  c = math.frexp(c)

  c = (mantisa, norm)

  answer = double_precision(s, mantisa)

  val1 = "{0:.4f}".format(answer)
  val2 = chopped(answer, 3)
  val2 = "{0:.3f}".format(val2)
  val3 = rounding(answer * .001)

  print(val1, end="\n\n")
  print(val2, end="\n\n")
  print(val3, end="\n\n")

  val1 = float(val1)

  val4 = val3 * 1000
  absolute_error = abs(val1 - val4) * .001
  print(absolute_error)

  relative_error = abs(val1 - val4)
  relative_error = relative_error / abs(val1)
  print(relative_error, end="\n\n")

  z = (10**1 / 3) * 10
  z = z - 1
  z = round(z)

  print(z, end="\n\n")
  #Qustion 6
  bisection_method = bisection(-4, 7)
  print(bisection_method, end="\n\n")

  newton_method = function3(7)
  print(newton_method)
