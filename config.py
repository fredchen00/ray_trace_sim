
class mmf_fibre:
	NA = 0.39
	n = 1.4630 #488nm RI.info
	r = 100e-6
	a = 0.996*r #x axis radius
	b = 1*r #y axis radius
	length=8000e-6 #length of fiber


class sim_config:
	num_threads=25 #number of threads to run the program #number of threads to run the program
	num_rays=1000**2 #approximate number of rays for each simulation
	step_size=5e-6	#scanning step size
	grid_size=[40,40] #scanning grid size
	offset_index=[0,0]	#starting posoition on the grid
	z_pos=-100e-6 # bead distance away from the fiber. should be <0
	save_dir='D:\Image Reg Data\Feb 15 2019\sim_test\\' # saving directory