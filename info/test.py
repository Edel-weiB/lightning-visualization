#unicode=utf8
import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation

THUNDER = 1;



def read_datas(file):
    datas_file = pandas.read_csv(file)

    return datas_file


def main():
    # Constants
    FILE_NAME = 'ALL20130801_G2a.csv'

    lighting_data = read_datas(FILE_NAME)

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    sc = ax.scatter([],[],[], c='darkblue', alpha=0.5)

    def update(i):
        global THUNDER
        sc._offsets3d = (lighting_data.Londitude.values[:i], lighting_data.Latitude.values[:i], lighting_data.Height.values[:i])


    min_long = min(lighting_data['Londitude'])
    max_long = max(lighting_data['Londitude'])
    min_lat = min(lighting_data['Latitude'])
    max_lat = max(lighting_data['Latitude'])
    min_h = min(lighting_data['Height'])
    max_h = max(lighting_data['Height'])

    ax.set_xlabel('Londitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Height (m)')
    ax.set_xlim(min_long,max_long)
    ax.set_ylim(min_lat,max_lat)
    ax.set_zlim(0,max_h)

    #ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(lighting_data), interval=self.change_play_speed)
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(lighting_data), interval=1)

    #def change_play_speed(self, speed):
    #    self.speed = float(speed)
    #    self.anim.event_source.interval = 100./self.speed

    plt.tight_layout()
    plt.show()

    

if __name__ == "__main__":
    main()