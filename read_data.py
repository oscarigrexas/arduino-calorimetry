# Call with three arguments
# 1 = port
# 2 = Baudrate
# 3 = output file name
# ex: python tempsensor.py /dev/ttyACM0 9600 readings.csv

import serial, sys, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t0 = time.time()
times = []
temps = []

fig = plt.figure()
ax = fig.add_subplot()

def animate(i, x, y):
    x = times
    y = temps
    ax.clear()
    ax.plot(x, y)


with open(sys.argv[3], "w") as f:
    with serial.Serial(port=sys.argv[1], baudrate=sys.argv[2]) as ser:
        if ser.isOpen():
            ser.readline()
        while ser.isOpen():
            try:
                deltatime = time.time() - t0
                temp = float(ser.readline().split()[-1])
                times.append(deltatime)
                temps.append(temp)
                f.write('{}, {}\n'.format(deltatime, temp))
            except KeyboardInterrupt:
                print("{} written".format(sys.argv[3]))
                break

#ani = animation.FuncAnimation(fig, animate, fargs=(times, temps), interval=1000)
ax.plot(times, temps, color='#ff4040')
plt.title('Temperature over time')
plt.ylabel('Temperature (C)')
plt.xlabel('Time (s)')
plt.show()
