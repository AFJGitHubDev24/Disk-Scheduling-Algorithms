from matplotlib import pyplot as plt
import math

sequence = [98, 183, 37, 122, 14, 129, 65, 67]
start = 53
cylinder_max = 199

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

LOOK(sequence, start, "Left")
LOOK(sequence, start, "Right")
