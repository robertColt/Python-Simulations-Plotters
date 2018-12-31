import matplotlib.pyplot as plot

def plot_data(data_list, labels, title, xlabel, ylabel, figName):
    plot.clf()
    plot.figure()
    plot.style.use("ggplot")
    handles = []
    for i, data in enumerate(data_list):
        handle, = plot.plot(data[0], data[1], label=labels[i])
        handles.append(handle)
    plot.legend(handles=handles)
    plot.title("MD Simulation")
    plot.xlabel(xlabel)
    plot.ylabel(ylabel)
    plot.savefig(figName)

fileNames=["stats50", "stats100", "stats150"]
# fileNames = fileNames[0:2]


data_cluster = []
data_span = []

for fileName in fileNames:
    probabilities = []
    cluster_sizes = []
    p_span = []
    # open file and populate above lists
    with open(fileName) as dataFile:
        lines = dataFile.readlines()
        for line in lines:
            data = list(map(float, line.split(" ")))
            probabilities.append(data[0])
            cluster_sizes.append(data[1])
            p_span.append(data[2])
    data_cluster.append([probabilities, cluster_sizes])
    data_span.append([probabilities, p_span])


plot_data(data_list=data_span, labels=fileNames, title="P vs P_span",
          xlabel="p", ylabel="p_span", figName="PvsPspan")
plot_data(data_list=data_cluster, labels=fileNames, title="P vs biggest cluster",
          xlabel="p", ylabel="biggest cluster size", figName="PvsMbiggest")