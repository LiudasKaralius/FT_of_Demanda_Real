If you are using cmd, run 'Main.py' script using IPython.
If you are not able to run the scrit, try pip-installing 'requirements.txt'.

This project consists of three python scripts: 'Main.py', 'Retriever.py' and 'FTplotter.py'. The later two are contained in folder 'modules'. These three scripts are discussed separately below.

'Main.py'     is the script which controls the process and adresses both 'Retriever.py' and 'FTplotter.py'. Here the request parameters and headers are set.

'Retriever.py'     contains a definition of a function which accesses the database and downloads the requested data.

'FT.plotter'     contains a definition of a class that is responsible for calulating a fast Fourier transform of this Demanda Real as well as plotting both the demand and its Fourier transform in the same figure. Real fast Fourier transform (rfft) was used fot the task, as energy demand is expected to be described by a real function, meaning that its FT will be symmetrical around the vertical axis. The FT plot was deliberately plotted from 0.03 to 6 days^(-1). Given we are only considering a time period of 35 days, any components corresponding to frequencies below 1/35~=0.03 days^(-1) may be prone to underfitting and should be discarded. 6 days^(-1) were chosen because generally higher frequency components grow weaker - in other words, to retain focus on the most important part of the plot. The output figure is saved as a .png file in the working directory.


RESULTS:
The peak at 1 days^(-1) dominates the frequency spectrum, indicating that spanish population tend to have energy usage habits that repeat periodically, day to day. Seven smaller peaks between 0.03 and 1 days^(-1) is a hint to the 7-day week. For example, the first one among them (at around 0.14 days^(-1)) corresponds to weekly repeating demand components. All this can be seen from 'spanish_energy_demand.png'.
