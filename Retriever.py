"""
This module contains a definition of a function that is responsible for 
communication with the host and retrieval of requested data.

Created on 2019-10-17
By Liudas Karalius
liudas.karalius.2@gmail.com
"""

import requests

def retrieve(host, parameters, headers):
    
    try:
        response = requests.get(
                                 host,
                                 params=parameters,
                                 headers=headers
                                )
        if response.status_code == 200:
            print('Data request successful.')
            data = response.json()
        else:
            print('Data request failed under status code', response.status_code)
    except:
        print('An exception occured')
    return data