import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation

import pandas as pd


def read_csv(file):
    lightning_df = pd.read_csv(file)
    return lightning_df


def plot_lightning(file):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    for i in range(len(file.index)-1):
        xs = file.loc[i]["Latitude"]
        ys = file.loc[i]["Londitude"]
        zs = file.loc[i]["Height"]
        ax.scatter(xs, ys, zs)
        
        delay = file.loc[i+1]["Second"] - file.loc[i]["Second"]
        if delay > 0.05:
            plt.pause(1)
        else:
            plt.pause(delay)

    min_long = min(lighting_data['Londitude'])
    max_long = max(lighting_data['Londitude'])
    min_lat = min(lighting_data['Latitude'])
    max_lat = max(lighting_data['Latitude'])
    min_h = min(lighting_data['Height'])
    max_h = max(lighting_data['Height'])
    
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Londitude')
    ax.set_zlabel('Height(m)')

    ax.set_xlim(min_long,max_long)
    ax.set_ylim(min_lat,max_lat)
    ax.set_zlim(0,max_h)


    plt.show()   

def main():
    print("File: ALL20130801_G2a.csv")
    lightning_df = read_csv("ALL20130801_G2a.csv")
    plot_lightning(lightning_df)
    # min_max_params(lightning_df)
    # print(lightning_df)
    

main()

