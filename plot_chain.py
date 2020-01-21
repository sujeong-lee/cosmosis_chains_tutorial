#import sys, os
import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt
from chainconsumer import ChainConsumer


# Set output figurename 
figname = 'contour.png'

# Calling DES chains
chainfile_name = 'example_chain.txt'
multinest_des_col_p = (0,4,3,2,1,6,18,-1)
cosmosis_multinest_chain = np.genfromtxt(chainfile_name, usecols=multinest_des_col)

# Set parameters' names and values
params_names = ['$\Omega_m$', '$A_s$', '$n_s$', '$\Omega_b$', '$h_0$', '$b$', '$\sigma_8$']
params_values = [3.057076e-01, 2.195731e-09, 9.683760e-01, 4.845864e-02,6.785960e-01, 2, 0.8152491E+00]


c = ChainConsumer()
c.add_chain(cosmosis_multinest_chain, parameters=params_values, name='example', weights = cosmosis_multinest_chain[:,-1])
#c.add_chain(chain_i, parameters = params_names[i], name=chain_names[i],weights=weights)
#fig = c.plotter.plot(figsize="column", truth=[0.0, 4.0])
# If we wanted to save to file, we would instead have written
fig = c.plotter.plot(filename=figname, figsize="column", truth=params_values)

# If we wanted to display the plot interactively...
# fig = c.plotter.plot(display=True, figsize="column", truth=[0.0, 4.0])

#fig.set_size_inches(3 + fig.get_size_inches())  # Resize fig for doco. You don't need this.



