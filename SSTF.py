from matplotlib import pyplot as plt
import math

sequence = [98, 183, 37, 122, 14, 129, 65, 67]
start = 53
cylinder_max = 199

def SSTF(sequence, start):
    temp = sequence.copy()

    def next_in_sequence(seq, val):
        diff = 0
        mindiff = math.inf
        nextval = 0
        print('SSTF Shortest Time Sequence and values: ')
        print(seq)
        for i in range(0, len(seq)):
            if (seq[i] != val):
                diff = abs(seq[i] - val)
                if (diff < mindiff):
                    mindiff = diff
                    nextval = seq[i]
        return nextval

    temp.insert(0, start)
    val = start
    x = []
    y = []
    size = 0
    x.append(start)
    head_movement = 0
    while(len(temp)):
        val = next_in_sequence(temp, val)
        print(val)
        x.append(val)
        temp.remove(val)
    size = len(x)
    for i in range(0, size):
        y.append(-i)
        if i != (size - 1):
            head_movement = head_movement + abs(x[i] - x[i + 1])
    string = 'Head movement = ' + str(head_movement) + ' cylinders'
    string2 = str(x)

    plt.plot(x, y, color="green", markerfacecolor='blue', marker='o', markersize=5, linewidth=2, label="SSTF")
    plt.ylim = (0, size)
    plt.xlim = (0, cylinder_max)
    plt.yticks([])
    plt.title("Shortest Seek Time First Disk Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(182.5, -11.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.show()

SSTF(sequence, start)
