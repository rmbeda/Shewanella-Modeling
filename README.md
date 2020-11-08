# Shewanella-Modeling
Subproject for predicting shewanella growth trend in an MFC

This is a numerical integration intended to predict the time-dependent trends in lactate availability and shewanella population given arbitrary initial conditions in terms of bacterial mass, lactate amount, and solution volume.

Main assumptions:

Assumption 1: Linear relation between bacterial growth rate and lactate consumption, based on a ratio between values found in the first link below.

Assumption 2: Lactate in the presence of a bacterium at a given time instant is consumed and contributes towards growth.

Given 'l' moles of lactate, 'm' grams of bacteria and volume 'V', lactate consumption is then -(1/(1000*V))*m moles per gram of bacteria per unit time (equal to the approximate volume of bacteria times the moles of lactate per mililitre).

Given the magnitude of the above lactate consumption rate, growth rate is simply that magnitude multiplied by the assumed ratio between doubling time and lactate consumption.

Useful information for this project may be found at locations below:

https://bionumbers.hms.harvard.edu/bionumber.aspx?s=n&v=1&id=111302 - lactate consumption rate at a growth rate of 0.085h^-1

https://onlinelibrary.wiley.com/doi/pdf/10.1002/bit.21101 - model/experiment comparison for shewanella growth (see page 129)

https://aem.asm.org/content/aem/48/4/755.full.pdf - Paper with abstract suggesting 0.22g/mL conversion between bacterial volume and ash-free dry weight

Concerning constants in the code:
'V' reflects known volume of container 
'm0' and 'lc0' represent initial bacterial mass and moles of lactate in solution. The hope is to know how they affect our expected culture progression. Initial lactate concentration may be used to calculate an initial lactate mass if desired (introduced for comparison with study above - not sure if reported experimental lactate concentration was initial or constant).
'Tmax' and 'steps' represent time period simulated and density of numerical integration steps. These can basically be changed arbitrarily to meet our predictive needs.
Molar mass of lactate is very well known and easy to find
‘Grow’ taken from bionumbers.harvard.edu
'Asfd_conv' represents 0.22g of ash free dry weight expected for most bacteria per mL of occupied volume (see https://aem.asm.org/content/aem/48/4/755.full.pdf)

