'''
Title: Leaky Integrate-and-Fire neuron spiking simulator
Author: Gonzalo Contreras Aso

Based on https://neuronaldynamics.epfl.ch/online/Ch1.S3.html
'''

import numpy as np
import matplotlib.pyplot as plt
from LIF import *

plt.style.use('seaborn-deep')
plt.rcParams.update({'font.size': 15, 'legend.fontsize': 15})
plt.rcParams.update({'text.usetex': True, "font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Times New Roman"]})


params = {'u0': -30, 'tau': 15, 'uR': -40, 'R': 5, 'theta': 30}

currents = ['None', 'low', 'high', 'pulse', 'linear_incr', 'linear_dec']
Is = [lambda t: 0, lambda x: 10, lambda x: 20, lambda t: short_pulse(t, 10, 20), lambda t: t/4, lambda t: max(50 - t,0)]
labels = ['$I(t)=0$', '$I(t)=10$', '$I(t)=20$', '$I(t)=\{50\,$ if $\, 10<t<20; \, $ otherwise $\, 0\}$', '$I(t)=t/4$', '$I(t)=\max(50-t,0)$']

for I, current, label in zip(Is, currents, labels):
    
    print(current)
    
    # Compute the solution
    uv, tv = solve_system(0.001, I, params)
    Iv = [I(t) for t in tv]
    
    # Plot it
    fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize = (8,10))
    fig.suptitle('Neuronal response to an external current')
    fig.supxlabel('t')
    
    ax1.plot(tv, Iv, color='orange', label=label)
    ax1.set_title('Applied current')
    ax1.set_ylabel('I(t)')
    ax1.legend(loc='best')
    
    ax2.plot(tv, uv)
    ax2.set_title('Voltage solution')
    ax2.set_ylabel('u(t)')    
    
    plt.savefig(f'Figures-LIF/{current}.png', facecolor='white', transparent=False)

