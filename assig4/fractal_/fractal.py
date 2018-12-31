import matplotlib.pyplot as plot


def plot_fractal(dataFileName, figName, title):
    # plot.style.use("ggplot")
    plot.figure()
    with open(dataFileName) as dataFile:
        rows = dataFile.readlines()
        # rows = rows[0:-1]

        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                if col == "1":
                    plot.plot(i, j, marker="o", color="k", markerSize="2")

    plot.title(title)
    plot.savefig(figName)


def plot_stats(dataFileName, figName, title):
    with open(dataFileName) as dataFile:
        plot.style.use("ggplot")
        plot.figure()
        min = 0
        max = 0
        rows = dataFile.readlines()
        x = []
        y = []
        for i, row in enumerate(rows):
            data = list(map(float, row.split("-")))
            # plot.plot(data[1], data[0], "ko-")
            x.append(data[1])
            y.append(data[0])
            if i == 0:
                min = data[0]
            if i == len(rows):
                max = data[1]
            # print("{}, {}",plot(data[1], data[0])
        plot.axis([4.5, 8, 1.5, 8])
        plot.plot(x, y)
        plot.xlabel("log(N_particles)")
        plot.ylabel("log(Rg)")
        plot.title(title)
        plot.savefig(figName)





p = 0.4
plot_fractal("fractal_/fractal", "fractal_/fractal04", "Fractal pnn = {:.2}".format(p))
# plot_stats("fractal_/statistics", "fractal_/stats04", "Rg vs N_partciles pnn = {:.2}".format(p))
