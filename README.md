# FT_of_Demanda_Real
This project consists of one pythin script: FT_of_demanda_real.py.
The script accesses Spanish electricity demand data of a given time period and performs its Fast Fourier Transform (FFT).
It consists of two main sections - DEFINITIONS and OPERATIONS. In its own right DEFINITIONS consists of two parts: 1) a "retrieve" function that communicates with the host and retrieves requested data; 2) the "FTplotter" class which is responsible for both executing FFT and plotting the results. Real fast Fourier transform (rfft) was used fot the task, as energy demand is expected to be described by a real function, meaning that its FT will be symmetrical around the vertical axis. OPERATIONS section contains the declaration of request parameters, as well as calls for both elements of DEFINITIONS section. 

The FT plot was deliberately plotted from 0.03 to 6 days^(-1). Given we are only considering a time period of 35 days, any components corresponding to frequencies below 1/35~=0.03 days^(-1) may be prone to underfitting and should be discarded. 6 days^(-1) were chosen because generally higher frequency components grow weaker - in other words, to retain focus on the most important part of the plot.

RESULTS:
The peak at 1 days^(-1) dominates the frequency spectrum, indicating that spanish population tend to have similar energy usage habits day to day. Seven smaller peaks between 0.03 and 1 days^(-1) is a hint to the 7-day week. For example, the first one among them (at around 0.14 days^(-1)) corresponds to weekly repeating components of the demand.
