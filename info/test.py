#unicode=utf8
import numpy as np
import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation



def read_datas(file, file2):
    datas_file = pandas.read_csv(file)
    datas_2 = pandas.read_csv(file2, header = None)

    return datas_file, datas_2


def main():
    # Constants
    FILE_NAME = 'ALL20130801_G2a.csv'
    LANSCAPE_NAME = 'contour.csv'

    lighting_data, datas_contour = read_datas(FILE_NAME, LANSCAPE_NAME)

    # initialise figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot properties
    min_long = min(lighting_data['Londitude'])
    max_long = max(lighting_data['Londitude'])
    min_lat = min(lighting_data['Latitude'])
    max_lat = max(lighting_data['Latitude'])
    min_h = min(lighting_data['Height(m)'])
    max_h = max(lighting_data['Height(m)'])
    min_ohm = min(lighting_data['sigma '])
    max_ohm = max(lighting_data['sigma '])

    #print(min_long, max_long, min_lat, max_lat)

    ax.set_xlabel('Londitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Height (m)')
    ax.set_xlim(min_long,max_long)
    ax.set_ylim(min_lat,max_lat)
    ax.set_zlim(0,max_h)


    X = np.linspace(min_long, max_long, len(datas_contour[0])-1)
    Y = np.linspace(min_lat, max_lat, len(datas_contour[0]))
    XX, YY = np.meshgrid(X, Y)
    ax.contourf(XX, YY, datas_contour.values)

    # Plot the graph
    thunder = 1
    for i in range(len(lighting_data["Year"])-1):
        if lighting_data["Flash No."][i] > thunder:
            thunder = lighting_data["Flash No."][i]
            plt.cla()

            ax.set_xlabel('Londitude')
            ax.set_ylabel('Latitude')
            ax.set_zlabel('Height (m)')
            ax.set_xlim(min_long,max_long)
            ax.set_ylim(min_lat,max_lat)
            ax.set_zlim(0,max_h)

            ax.contourf(XX, YY, datas_contour.values)

        xs = lighting_data["Londitude"][i]
        ys = lighting_data["Latitude"][i]
        zs = lighting_data["Height(m)"][i]
        
        if lighting_data["sigma "][i] < 0.001:
            color = 'blue'
        elif lighting_data["sigma "][i] >= 0.001 and lighting_data["sigma "][i] < 0.01:
            color = 'green'
        elif lighting_data["sigma "][i] >= 0.01 and lighting_data["sigma "][i] < 0.1:
            color = 'orange'
        elif lighting_data["sigma "][i] >= 0.1 and lighting_data["sigma "][i] < 1:
            color = 'red'
        else:
            color = 'black'

        ax.scatter(xs, ys, zs, s=1, c = color, alpha=0.8)
        
        delay = lighting_data["Second"][i+1] - lighting_data["Second"][i]
        if delay > 0.05:
            plt.pause(1)
        else:
            if delay <= 0:
                delay = 0.01
            plt.pause(delay)


    

    ##ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(lighting_data), interval=self.change_play_speed)
    #ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(lighting_data), interval=1)

    ##def change_play_speed(self, speed):
    ##    self.speed = float(speed)
    ##    self.anim.event_source.interval = 100./self.speed

    #plt.tight_layout()
    #plt.show()

    

if __name__ == "__main__":
    main()

    