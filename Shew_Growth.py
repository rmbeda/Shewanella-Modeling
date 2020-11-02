# Last Modified by Robert Beda on September November 1, 2020
# Modelling Growth of Shewanella Oneidensis
# Assume linear relation of 0.00441mol/(gram*hour) consumed per 0.085 doublings/hour

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Robert, remember to run using Python3 in order to avoid weird 'infinite loop' error
# Before running, vary initial conditions and time-step info as desired:

V = 0.775/2 # L - Assumed volume of one half-cell (the one with the bacteria)
m0 = 0.03 # g - Initial bacterial population mass
lc0_m = 0.05
lc0 = 5 # mol (= ~0.9 g) - Initial moles of lactate
tmax = 72 # Number of hours over which to run the simulation
steps = 7200 # Number of time steps to use
print(lc0)
# For non-debugging use, don't edit past here.

molm = 90.08 # molar mass of lactate (g/mol)
grow = 0.085/0.00441 # doublings/hour per mol of lactate consumed/hour
asfd_conv = 0.22 # grams of bacteria per mL of bacterial volume
def l_per_gbac(l):
	"""Moles of Lactate consumed per gram of bacteria per hour"""
	return l/(1000*V)*(asfd_conv)**(-1)

def dldt(m, l):
	# Rate of change in amount of lactate (moles)
	return -l_per_gbac(l)*m

def dmdt(m, l):
	# Rate of change in mass of bacteria (grams)
	return -grow*dldt(m, l)*m

Ys0 = np.array([m0, lc0]) # initial conditions for odeint

dt = tmax/steps # Time differential between time steps
ts = np.arange(steps)*dt # Array of all times to be represented in plots.


def stepping(inits, ts):
	"""Returns rates of change of bacterial mass 
	and lactate amount.

	Based on  the linear ODE, this determines the current rates of change
	in m and l to be used in a later odeint function call.

	Arguments:
	inits -- 1-d array containing (in order) m0, l0, dm, dl
	tAF -- 1-d array containing all times at which rates of change
	       are to be evaluated
	Returns:
	1-d array containing (in order) dx/dt. dy/dt, dvx/dt, dvy/dt
	"""
	m = inits[0]
	l = inits[1]
	return np.array([dmdt(m, l), dldt(m, l)])


masses = integrate.odeint(stepping, Ys0, ts)
ms = masses[:,0]
ls = masses[:,1]
plt.plot(ts, ms, "r", label = "Bacterial Mass")
plt.xlabel("Time (Hours)")
plt.ylabel("Mass (g)")
plt.title("Bacteria")
plt.show()
plt.plot(ts, ls, "b", label = "Lactate Moles")
plt.xlabel("Time (Hours)")
plt.ylabel("Lactate (Moles)")
plt.title("Lactate in Solution")
plt.show()
