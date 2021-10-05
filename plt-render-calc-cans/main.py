import matplotlib.pyplot as plt
import numpy as np


# Everything is in terms of a cyl.
def getCost(r, h, tbc, lc):
    lat = 2 * float(np.pi) * r * h
    tb = float(np.pi) * (r ** 2)

    return (r, (lat * tbc) + (2 * tb * lc)), h


# returns new r & h
def getRH(v, c):
    if c.lower() == "y":
        v /= np.pi

    # B/c you can have any h or r for a given v, choose smaller para for lower variation.
    # apply round() to make it nicer, better to leave off though.
    h = float(np.random.uniform(0, 50))
    r = np.sqrt(v / (np.pi * h))

    return r, h


# plots the cyl, "can."
'''
def plotCyl(r, h):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 50)
    hx = np.linspace(0, h, 20)
    x = np.outer(r * np.sin(u), np.ones(len(hx)))
    y = np.outer(r * np.cos(u), np.ones(len(hx)))
    z = np.outer(np.ones(len(u)), hx)

    ax.plot_surface(x, y, z, cmap=plt.get_cmap('Blues_r'))

    plt.show()
'''

def plot2D(rhc):
    fig = plt.figure(1)
    x = [x[0][0] for x in rhc]
    y = [x[0][1] for x in rhc]

    plt.plot(x, y, 'o', color='black');

def plot3D(rhc):
    # plotting 3D
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')

    # scattering points
    x = [x[0][0] for x in rhc]
    y = [x[1] for x in rhc]
    z = [x[0][1] for x in rhc]
    ax.scatter(x, y, z)

    plt.show()


# check if volumes will be identical
def checkV(v, r, h):
    testV = np.pi * (r ** 2) * h
    if v == round(testV, 3):
        return True

    return False


v = 365.308
cost = 0.00016, 0.0005

# results
rhcArr = []

for i in range(100):
    rh = getRH(v, "n")
    rhcArr.append(list(getCost(rh[0], rh[1], cost[0], cost[1])))
rhcArr.sort()

print(rhcArr)
print("Largest r:", rhcArr[-1][0][0])  # largest radius
print("Largest h:",rhcArr[0][1])  # largest height
print("Largest c:",rhcArr[-1][0][1])  # largest cost

plot2D(rhcArr)
plot3D(rhcArr)

