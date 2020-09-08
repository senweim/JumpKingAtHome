
# set up libraries used in this notebook
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from scipy.stats import linregress

# enter data and display in a table
x_var = "Length, L (m)" # independent variable label, symbol (units)
y_var = "Period, T (s)" # dependent variable label, symbol (units)
x = [7.75e+06, 1.00e+07, 1.25e+07, 1.50e+07, 1.75e+07, 2.00e+07, 2.25e+07, 2.50e+07] # independent variable measurements
y = [3.26e+09, 2.52e+09, 2.00e+09, 1.73e+09, 1.44e+09, 1.29e+09, 1.13e+09, 1.03e+09] # dependent variable measurements
data = {x_var: x, y_var: y}
print (tabulate(data, headers="keys", tablefmt="fancy_grid"))

# graph the data
plt.plot(x,y,'bo')
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.grid(which='major', axis='both')
plt.axis([0, 3.00e+07, 0, 4.00e+09])
plt.title('Length of Pendulum (m) vs Pendulum Period (s)')
plt.xticks(np.arange(0, 3.00e+07, 0.25e+07))
plt.yticks(np.arange(0, 4.00e+09, 0.50e+09))
plt.show()

# find new x values
x1 = np.array(x)
x2 = 1/x1

# find the best fit line
m2, b2, r2, p2, e2 = linregress(x2,y)
m2 = m2*1e-16
m2 = round(m2,2) * 1e16
b2 = b2*1e-7
b2 = round(b2,2) * 1e7
r2 = round(r2,3)
x_fit = x2
y_fit = m2*x_fit+b2
eqn = "Linear Fit Equation: T = " + str(m2) + "sqrt(L) + " + str(b2) + "\n"
err = "Linear Fit Match: R-squared = " + str(r2) + "\n"
print (eqn)
print (err)

# replot the data with the best fit line
plt.plot(x2,y,'bo')
plt.plot(x_fit,y_fit,'r-')
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.grid(which='major', axis='both')
plt.axis([0, 1e-07, 0, 4.00e+09])
plt.title('Length of Pendulum (m) vs Pendulum Period (s)')
plt.xticks(np.arange(0, 2e-07, 0.25e-07))
plt.yticks(np.arange(0, 4.00e+09, 0.50e+09))
plt.show()