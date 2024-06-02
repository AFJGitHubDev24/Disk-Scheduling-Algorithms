from matplotlib import pyplot as plt
import math

sequence = [98, 183, 37, 122, 14, 129, 65, 67]
start = 53
cylinder_max = 199

def FCFS(sequence, start):
    temp = sequence.copy()
    temp.insert(0, start)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    size = len(temp)
    x = temp
    y = []
    head_movement = 0
    for i in range(0, size):
        y.append(-i)
        if i != size - 1:
            head_movement = head_movement + abs(temp[i] - temp[i + 1])
    string = 'Head movement = ' + str(head_movement) + ' cylinders'
    string2 = str(temp)
    plt.plot(x, y, color="green", markerfacecolor='blue', marker='o', markersize=5, linewidth=2, label="FCFS")
    plt.ylim = (0, size)
    plt.xlim = (0, cylinder_max)
    plt.yticks([])
    plt.title("First Come First Served Disk Scheduling Algorithm")
    plt.text(172.5, -8.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(172.5, -9.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.show()

FCFS(sequence, start)
