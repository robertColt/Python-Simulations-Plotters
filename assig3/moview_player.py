import matplotlib.pyplot as plt

def getData(fileName):
    with open(fileName) as dataFile:
        n_size = int(dataFile.readline())
        frames = int(dataFile.readline())

        data = []

        for frame in range(frames):
            data.append([]) # add a frame
            counter = 0
            frameData = dataFile.readline().strip().split(" ")

            counter = 0
            for row in range(n_size):
                data[frame].append([])  # add rows for the frame
                for col in range(n_size):
                    data[frame][row].append(frameData[counter])
                    counter+=1
    return data


def play_movie(data):
    for f, frame in enumerate(data):
        plt.clf()
        plt.title("t = {}".format(f + 1))
        for i, row in enumerate(frame):
            for j, color in enumerate(row):
                plt.plot([i], [j], color, markersize=15)
        plt.pause(0.4)

    plt.show()



# movie_data = getData("ising_movie_lowT") #0.5
movie_data = getData("ising_movie_tc") #2.11
# movie_data = getData("ising_movie_high") #3.7
play_movie(movie_data)


# plt.axis([0, 10, 0, 10])
# colors = ["ro", "bo"]
# for f in range(10):
#     plt.clf()
#     plt.title("t = {}".format(f))
#     colorId = f % 2
#     for i in range(10):
#         for j in range(10):
#             plt.plot([i], [j], colors[colorId], markersize=15)
#     plt.pause(0.5)

# plt.show()