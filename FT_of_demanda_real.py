"""
Created on 2019-10-17
By Liudas Karalius
liudas.karalius.2@gmail.com

"""
# This program dowloads real electricity demand during a period between the
# specified dates. It then calculates a fast Fourier transform of this demand.
# Both the demand and its Fourier transform are then plotted in the same
# figure.

import requests
import matplotlib.pyplot as pl
from scipy.fftpack import rfft, rfftfreq
import numpy as np

# The two following imports impose plotting in a separate window.
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')


# ______________________________ DEFINITIONS __________________________________
# This function is responsible for communication with the host and retrieval of
# requested data
def retrieve(host,parameters,headers):
    try:
        response = requests.get(
                                 host,
                                 params=parameters,
                                 headers=headers
                                )
        if response.status_code == 200:
            print('Data request successful.')
            data = response.json() # Converts byte response into JSON object.
        else:
            print('Data request failed under status code', response.status_code)
    except:
        print('An exception occured')
    return data

# This class is responsible for executing FFT and plotting the results
class FTplotter:
    
    # Further, demand vales are converted from kW to MW (factor of 1000).
    # Time step of 10 minutes is represented in days (factor of 6*24).
    def __init__(self, indicator_data):
        self.values = [elem['value']/1000 for elem in indicator_data]
        self.time = np.linspace(0, len(self.values)/(6*24), num=len(self.values))

    def plot_energy_demand_and_ft(self):
        sample_freq = rfftfreq(len(self.values),d=self.time[1])
        demand_transform = abs(rfft(self.values))
        demand_transform[0] = 0     # 0th element of the transform is the
                                    # average of the demand and hence is
                                    # irrelevant for our purposes.

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
        ax2.set_xlim([0.03, 6])  # Axis limits are better explained in README.md 


# _____________________________ OPERATIONS ____________________________________
host = 'https://api.esios.ree.es/indicators/1293'
parameters = {
               'start_date' : '2018-09-02T00:00:00+0100',
               'end_date' : '2018-10-07T00:00:00+0100',
             }
headers = {
            'Accept' : 'application/json; application/vnd.esios-api-v1+json',
            'Content-Type' : 'application/json',
            'Host' : 'api.esios.ree.es',
            'Authorization' : 'Token token="23df430b183995125a4b387b46556b4d217a69d2d1451ff246d87ee50785eafc"'
          }

data = retrieve(host, parameters, headers)


plotter = FTplotter(data['indicator']['values'])
plotter.plot_energy_demand_and_ft()
