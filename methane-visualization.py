# Adapted from Andrea Gaspert

# import important packages
import numpy as np
import matplotlib.pyplot as plt


site_id = 'ATNeu' #change with desired site
local_path = '/Users/macbook/Box Sync/MethaneFluxnetSynthesisAnalysis/Data/Upscaling_Analysis/DataAggregated/' #change with how locally setup
file_path = local_path + site_id +'.csv'

data = np.genfromtxt(file_path, delimiter=',', skip_header=1, usecols=(2,7,17,18,19,20,37,45,46,47,48))

true_if_data = np.nan_to_num(data[:,1])> 0 #1 where data is a number, 0 elsewhere
position_data = np.where(true_if_data)[0] #positions of where data available

earliest = int(data[:,0][position_data[0]])
latest = int(data[:,0][position_data[-1]])

print('earliest: {} , latest: {}'.format(earliest, latest))

start = 2010
end = 2011

id_start = np.where(data[:,0] == float(start))[0][0]
id_end = np.where(data[:,0] == float(end))[0][0]

time_axis = np.arange(id_start,id_end)

plt.plot(time_axis,data[:,1][id_start:id_end],'b.',label=site_id+' data') #data for mean methane fluxes
plt.plot(time_axis,data[:,6][id_start:id_end],'r.',label=site_id+' filled data') #filled data
plt.ylabel('mean CH4 flux') # test change
plt.legend(loc='best')
plt.show()

plt.plot(time_axis,data[:,5][id_start:id_end],'b.',label=site_id+' data') #data for temperature
plt.plot(time_axis,data[:,10][id_start:id_end],'r.',label=site_id+' filled data') #filled data
plt.ylabel('Temperature')
plt.legend(loc='best')
plt.show()