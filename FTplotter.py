"""
This program contains a definition of a class that is responsible for 
calculating a fast Fourier transform of this Demanda Real as well as plotting
both the demand and its Fourier transform in the same figure.

Created on 2019-10-17
By Liudas Karalius
liudas.karalius.2@gmail.com
"""
import matplotlib.pyplot as pl
from scipy.fftpack import rfft, rfftfreq
import numpy as np

# The two following imports impose plotting in a separate window.
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

class FTplotter:
    """
    This class is responsible for executing FFT and plotting the results
    Axis limits are better explained in README.md
    """
    values = []
    time = []

    def __init__(self, indicator_data):
        """
        Initializes the plotter with indicator data.
        Demand vales are converted from kW to MW (factor of 1000).
        Time step of 10 minutes is represented in days (factor of 6*24).
        """
        self.values = [elem['value']/1000 for elem in indicator_data]
        self.time = np.linspace(0, len(self.values)/(6*24), num=len(self.values))

    def plot_energy_demand_and_ft(self):
        sample_freq = rfftfreq(len(self.values),d=self.time[1])
        demand_transform = abs(rfft(self.values))
        # 0th element of the transform is the average of the demand and hence is irrelevant for our purposes.
        demand_transform[0] = 0

        pl.figure(1, figsize=(16,7))
        pl.subplots_adjust(hspace=0.5)
        ax1 = pl.subplot(211)
        ax1.grid('major')
        ax1.plot(self.time, self.values, 'r-')
        ax1.set_xlabel('time (days)',fontweight='bold')
        ax1.set_ylabel('Energy Demand (MW)',fontweight='bold')
        ax2 = pl.subplot(212)
        ax2.grid('major')
        ax2.plot(sample_freq, demand_transform, 'b-')
        ax2.set_xlabel('frequency (days$^{-1}$)',fontweight='bold')
        ax2.set_ylabel('Amplitude (a.u.)',fontweight='bold')
        ax2.set_xlim([0.03, 6])
