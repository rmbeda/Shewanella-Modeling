# Shewanella-Modeling
Subproject for predicting shewanella growth trend in an MFC

This is a numerical integration intended to predict the time-dependent trends in lactate availability and shewanella population given arbitrary initial conditions in terms of bacterial mass, lactate amount, and solution volume.

Main assumptions:
Assumption 1: Linear relation between bacterial growth rate and lactate consumption, based on a ratio between values found in the first link below.

Assumption 2: Lactate in the presence of a bacterium at a given time instant is consumed and contributes towards growth.

Given 'l' moles of lactate, 'm' grams of bacteria and volume 'V', lactate consumption is then -(1/(1000*V))*m moles per gram of bacteria per unit time (equal to the approximate volume of bacteria times the moles of lactate per mililitre).

Given the magnitude of the above lactate consumption rate, growth rate is simply that magnitude multiplied by the assumed ratio between doubling time and lactate consumption.


Useful information for this project may be found here:
https://bionumbers.hms.harvard.edu/bionumber.aspx?s=n&v=1&id=111302 - lactate consumption rate at a growth rate of 0.085h^-1
https://onlinelibrary.wiley.com/doi/pdf/10.1002/bit.21101 - model/experiment comparison for shewanella growth (see page 129)
