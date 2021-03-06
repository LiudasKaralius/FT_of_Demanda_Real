"""
This controls the process, during which real spanish electricity demand
between the specified dates is downloaded, Fourier tranformed and plotted.
Module Retriever is responsible for database access and data download.
Module FTplotter is responsible for Fourier transforming and plotting the data.

Created on 2019-10-17
By Liudas Karalius
liudas.karalius.2@gmail.com
"""

from modules.FTplotter import FTplotter
from modules.Retriever import retrieve

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
