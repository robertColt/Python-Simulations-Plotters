import matplotlib.pyplot as plot
import colorsys
import random


def get_N_HexCol(N=5):
    HSV_tuples = [(x * 1.0 / N, 0.7, 0.7) for x in range(N)]
    hex_out = []
    for rgb in HSV_tuples:
        rgb = map(lambda x: int(x * 255), colorsys.hsv_to_rgb(*rgb))
        hex_out.append('#%02x%02x%02x' % tuple(rgb))
    return hex_out


def get_data(fileName):
    with open(fileName) as dataFile:
        lines = dataFile.readlines()
        config = list(map(int, lines[0].split(" ")))
        lines = lines[1:]
        if lines[-1] == "\n":
            lines = lines[0:-1]
        n = config[0]
        frames = config[1]
        data = []
        i = 0
        print("Moview has size ", n, " and ", frames, "frames")
        for frame in range(frames):
            print("Processing frame ", frame)
            data.append([])
            j = 0
            while j < n:
                line = lines[i]
                data[frame].append(list(map(int, line.split(" "))))
                j+=1
                i+=1
        return data


def play_movie(data, hexcolors):
    print("playing movie")
    plot.figure(figsize=(6.35, 5.35))
    for f, frame in enumerate(data):
        plot.clf()
        print(len(frame[0]))
        plot.title("t = {}, N = {}".format(f + 1, len(frame[0])))

        for i, row in enumerate(frame):
            for j, col in enumerate(row):
                jindex = j
                if i%2 != 0:
                    jindex += 0.5
                if col == -1:
                    color = "#000000"
                else:
                    color = hexcolors[col-1]
                # print("plotting ", i, j)
                plot.plot([jindex], [i], marker="h", color=color, markersize=10)
        plot.pause(0.01)
    plot.show()


fileNames = ["perc02_hex", "perc04_hex", "perc055_hex", "perc09_hex"]
cluster_numbers = [400, 200, 150, 10]
index_to_use = 3

data = get_data(fileNames[index_to_use])
hexcolors = get_N_HexCol(cluster_numbers[index_to_use])
random.shuffle(hexcolors)
play_movie(data, hexcolors)