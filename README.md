# FT_of_Demanda_Real
This project consists of one pythin script: FT_of_demanda_real.py.
The script accesses Spanish electricity demand data of a given time period and performs its Fast Fourier Transform.
Real fast Fourier transforms were used, as we are expecting energy demand to be described by a real function, meaning that its FT will be symmetrical around y axis.

The FT plot was deliberately plotted from 0.03 to 6 days^(-1). Given we are only considering a time period of 35 days, any components corresponding to frequencies below 1/35~=0.03 days^(-1) may be seen as overfitting and should be discarded. 6 days^(-1) were chosen because generally higher frequency components grow weaker - in other words, to retain focus on the most important part of the plot.
