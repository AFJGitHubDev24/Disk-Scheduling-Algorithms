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


def SCAN(sequence, start, direction):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    head_movement = 0
    head_movement_approx = 0
    x.append(start)
    if direction == "Left":
        for i in temp:
            if i < start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse=True)
        for i in left:
            x.append(i)
        x.append(0)
        right.sort()
        for i in right:
            x.append(i)

        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        head_movement_approx = abs(start - 0)
        head_movement_approx = head_movement_approx + abs(0 - max(x))
    elif direction == "Right":
        for i in temp:
            if i > start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x.append(cylinder_max)
        left.sort(reverse=True)
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        head_movement_approx = abs(start - 199)
        head_movement_approx = head_movement_approx + abs(199 - min(x))

    y_approx.append(0)
    size = len(x)
    for i in range(0, size):
        y.append(-i)
        if (x[i] == 0 or x[i] == 199):
            y_approx.append(-i)
        if i != (size - 1):
            head_movement = head_movement + abs(x[i] - x[i + 1])
        else:
            y_approx.append(-i)
    string = 'Head movement = ' + str(head_movement) + ' cylinders'
    string2 = str(x)

    plt.plot(x, y, color="green", markerfacecolor='blue', marker='o', markersize=5, linewidth=2, label="SCAN")
    plt.plot(x_approx, y_approx, dashes=[6, 2], color="red", markerfacecolor='red', marker='D', markersize=5,
             linewidth=0.5, label="Approx SCAN")
    plt.ylim = (0, size)
    plt.xlim = (0, cylinder_max)
    plt.yticks([])
    plt.title("SCAN Disk Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.show()


def CSCAN(sequence, start, direction):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    head_movement = 0
    head_movement_approx = 0
    x.append(start)
    if direction == "Left":
        for i in temp:
            if i < start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse=True)
        for i in left:
            x.append(i)
        x.append(0)
        x.append(cylinder_max)
        right.sort(reverse=True)
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        x_approx.append(x[-1])
        head_movement_approx = abs(start - 0)
        head_movement_approx = head_movement_approx + abs(0 - max(x))
        head_movement_approx = head_movement_approx + abs(0 - x[-1])
    elif direction == "Right":
        for i in temp:
            if i > start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x.append(cylinder_max)
        x.append(0)
        left.sort()
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(cylinder_max)
        x_approx.append(0)
        x_approx.append(x[-1])
        headmovement_approx = abs(start - 199)
        headmovement_approx = headmovement_approx + abs(199 - 0)
        headmovement_approx = headmovement_approx + abs(0 - x[-1])

    y_approx.append(0)
    size = len(x)
    for i in range(0, size):
        y.append(-i)
        if x[i] == 0 or x[i] == 199:
            y_approx.append(-i)
        if i != (size - 1):
            head_movement = head_movement + abs(x[i] - x[i + 1])
        else:
            y_approx.append(-i)
    string = 'Head movement = ' + str(head_movement) + ' cylinders'
    string2 = str(x)

    plt.plot(x, y, color="green", markerfacecolor='blue', marker='o', markersize=5, linewidth=2, label="CSCAN")
    plt.plot(x_approx, y_approx, dashes=[6, 2], color="red", markerfacecolor='red', marker='D', markersize=5,
             linewidth=0.5, label="Approx C-SCAN")
    plt.ylim = (0, size)
    plt.xlim = (0, cylinder_max)
    plt.yticks([])
    plt.title("C-SCAN Disk Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.show()


def LOOK(sequence, start, direction):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    head_movement = 0
    head_movement_approx = 0
    x.append(start)
    if direction == "Left":
        for i in temp:
            if i < start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse=True)
        for i in left:
            x.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        head_movement_approx = abs(start - min(x))
        head_movement_approx = head_movement_approx + abs(min(x) - max(x))
    elif direction == "Right":
        for i in temp:
            if i > start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        left.sort(reverse=True)
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        head_movement_approx = abs(start - max(x))
        headmovement_approx = head_movement_approx + abs(max(x) - min(x))

    y_approx.append(0)
    size = len(x)
    for i in range(0, size):
        y.append(-i)
        if (x[i] == max(x) or x[i] == min(x)) and (i != size):
            y_approx.append(-i)
        if i != (size - 1):
            head_movement = head_movement + abs(x[i] - x[i + 1])
    string = 'Head movement = ' + str(head_movement) + ' cylinders'
    string2 = str(x)

    plt.plot(x, y, color="green", markerfacecolor='blue', marker='o', markersize=5, linewidth=2, label="LOOK")
    plt.plot(x_approx, y_approx, dashes=[6, 2], color="red", markerfacecolor='red', marker='D', markersize=5,
             linewidth=0.5, label="Approx LOOK")
    plt.ylim = (0, size)
    plt.xlim = (0, cylinder_max)
    plt.yticks([])
    plt.title("LOOK Disk Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.show()


def CLOOK(sequence, start, direction):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    head_movement = 0
    head_movement_approx = 0
    x.append(start)
    if direction == "Left":
        for i in temp:
            if i < start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse=True)
        for i in left:
            x.append(i)
        right.sort(reverse=True)
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        x_approx.append(x[-1])
        head_movement_approx = abs(start - min(x))
        head_movement_approx = head_movement_approx + abs(min(x) - max(x))
        head_movement_approx = head_movement_approx + abs(max(x) - x[-1])
    elif direction == "Right":
        for i in temp:
            if i > start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        left.sort()
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        x_approx.append(x[-1])
        head_movement_approx = abs(start - max(x))
        head_movement_approx = head_movement_approx + abs(max(x) - min(x))
        head_movement_approx = head_movement_approx + abs(min(x) - x[-1])

    y_approx.append(0)
    size = len(x)
    for i in range(0, size):
        y.append(-i)
        if (x[i] == min(x) or x[i] == max(x)) and (i != size):
            y_approx.append(-i)
        if i != (size - 1):
            head_movement = head_movement + abs(x[i] - x[i + 1])
        else:
            y_approx.append(-i)
    string = 'Head movement = ' + str(head_movement) + ' cylinders'
    string2 = str(x)
    string3 = 'Approx Headmovement = ' + str(head_movement_approx) + ' cylinders'

    plt.plot(x, y, color="green", markerfacecolor='blue', marker='o', markersize=5, linewidth=2, label="CLOOK")
    plt.plot(x_approx, y_approx, dashes=[6, 2], color="red", markerfacecolor='red', marker='D', markersize=5,
             linewidth=0.5, label="Approx C-LOOK")
    plt.ylim = (0, size)
    plt.xlim = (0, cylinder_max)
    plt.yticks([])
    plt.title("C-LOOK Disk Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(182.5, -11.5, string3, horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.show()


FCFS(sequence, start)
SSTF(sequence, start)
SCAN(sequence, start, "Left")
SCAN(sequence, start, "Right")
CSCAN(sequence, start, "Left")
CSCAN(sequence, start, "Right")
LOOK(sequence, start, "Left")
LOOK(sequence, start, "Right")
CLOOK(sequence, start, "Left")
CLOOK(sequence, start, "Right")
