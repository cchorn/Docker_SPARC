# this is a script to import Spike2 files
###########################################################
"""
filename = name of Spike2 file
sample_rate = 20000 ... in most cases
gain = amplification correction to convert to uV (this depends on your I/O setttings)
... ours is 50 = multiplication factor for 20K amp
........... 25 = multiplication factor for 10K amp
........... 12.5 = multipication factor for 5K amp
save_start = start time for saving data to file (sec)
save_end = end time for saving data to file (sec)
display_start = start time for displaying data in a plot (sec)
display_end = end time for displaying data in a plot (sec)
"""
def importSpike2(filename, gain, sample_rate, save_start, save_end, display_start, display_end, graph):
	"Function that loads a .smr file"
	# the following global definition is needed to access the signal data in other notebook cells
	global asig
	# print todays date and time
	import time
	## dd/mm/yyyy format
	print (time.strftime("%d/%m/%Y"))
	## 12 hour format ##
	print (time.strftime("%I:%M:%S"))
	print ("\n====================")
	# import a Spike2 file (CED)
	r = neo.Spike2IO(filename)
	bl = r.read()[0]
	asig = bl.segments[0].analogsignals[0]
	# keep the signal as a 16 bit float
	asig = np.float16(asig)
	asig = asig * gain
	datatype = asig.dtype
	pts = round(float(np.prod(asig.shape)), 0)
	secs = round(pts/sample_rate, 2)
	mins = round(secs/60.0, 2)
	hrs = round(mins/60, 3)
	print("{}:\n====================".format(filename.split("/")[-1]))
	print("{} data points\n{} sec\n{} min\n{} hr".format(pts, secs, mins, hrs))
	print(sample_rate, "Hz")
	print (datatype)
	# plot data if wanted
	if graph: # only if graph == True
		fig, ax = plt.subplots(1, 1, figsize=(8, 3))
		start = display_start * sample_rate
		end = display_end * sample_rate
		asig_display = asig[start:end]
		time = np.arange(display_start, display_end, 1.0/sample_rate)
		ax.plot(time, asig_display, "b") # b = blue
		ax.set_xlabel("seconds", fontsize = 12)
		ax.set_ylabel("microvolts", fontsize = 12)
		plt.grid()
		plt.tight_layout()
		plt.show()