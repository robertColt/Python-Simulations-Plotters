import matplotlib.pyplot as plot

n_particles = range(100, 1001, 100)

time = [50, 132, 255, 433, 697, 1000, 1408, 2000, 2700, 3595]
time_tabulated = []
time_verlet = [4, 9, 23, 40, 57, 65, 90, 117, 141, 185]
time_verlet_tabulated = [4, 8, 15, 26, 37, 50, 68, 104, 115, 143]


plot.style.use("ggplot")
plot.figure()
unoptimized, = plot.plot(n_particles, time, marker="o", label="Unoptimized", color="blue")
# tabulated, = plot.plot(n_particles, time, marker="o", label="Tabulated", color="red")
verlet, = plot.plot(n_particles, time_verlet, marker="o", label="Verlet", color="yellow")
verlet_tabulated, = plot.plot(n_particles, time_verlet_tabulated, marker="o",label="Verlet Tabulated", color="green")
plot.legend(handles=[verlet, verlet_tabulated, unoptimized])
plot.title("MD Simulation")
plot.xlabel("N particles")
plot.ylabel("Time (in s)")
# plot.xticks(np.arange(1, epochs+1, 1))
# plot.yticks(np.arange(train_history[-1], train_history[0], 0.1))
plot.savefig("all_plot")