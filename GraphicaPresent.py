import math
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os


class GraphicPresent:
    def __init__(self, ):
        pass
    def _qsrt(self, value_np):
        return np.sqrt(value_np)

    def _2D_Data_Video(self, x_value, y_value,x_stretch=1, y_stretch=1):
        """[create a video to demenstorate the data_np]

        Args:
            data_np ([np]): [using data1 for drawing]
            index_np ([type]): [using data2 for drawing]
            xlim ([type]): [xlim]
            step (int, optional): [xlim's step]. Defaults to 1.
            method (int, optional): [method for using data_np and index_np]. Defaults to 0.
            ylim (tuple, optional): [ylim] Defaults to (0,10).
        """
        if os.path.exists("./temp_displayArray"):
            os.system("rm -rf ./temp_displayArray")
        os.mkdir("./temp_displayArray")

        plt.rcParams['axes.facecolor'] = 'black'
        fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='black')
        ax = fig.add_subplot(111)

        plt.xlim(x_value[0], (x_value[-1]-x_value[0])*x_stretch)
        plt.ylim(y_value[0], (y_value[-1]-y_value[0])*y_stretch)
        for spine in ['top', 'right', "bottom", "left"]:
            ax.spines[spine].set_color("white")
        ax.set_xlabel('Dimension')
        ax.set_ylabel('Length ')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors="white")
        ax.tick_params(axis='y', colors="white")

        for j in range(0, x_value.shape[0]):
            displayArray_x = np.array([])
            displayArray_y = np.array([])
            count = 0
            for i in range(0, j+1):
                count = count+1
                displayArray_x = np.append(displayArray_x, x_value[i])
                displayArray_y = np.append(displayArray_y, y_value[i])
                ax.plot(displayArray_x, displayArray_y, "w-")
                ax.plot(displayArray_x,displayArray_x, "w--")
                plt.savefig(f'./temp_displayArray/displayArray_{str(j).zfill(10)}.png')

        if os.path.exists("out.mp4"):
            os.remove("out.mp4")
        os.system(f"ffmpeg -r 60 -f image2 -s 1920x1080 -pattern_type glob  -i './temp_displayArray/displayArray_*.png' -vcodec libx264 -crf 18  -pix_fmt yuv420p out.mp4")
        if os.path.exists("./temp_displayArray"):
            os.system("rm -rf ./temp_displayArray")


def main():
    ec = GraphicPresent()
    x_lim = [0, 10, 1]
    # x_value = np.arange(x_lim[0],x_lim[1],x_lim[2])
    x_value = np.array([0,1+1,2+2,3+3,4+4,5+5,6+6,7+7,8+8,9+9,10+10])
    y_value = ec._qsrt(x_value)
    print(y_value)
    
    
    
    
    ec._2D_Data_Video(x_value, y_value,y_stretch = 2)

if __name__ == '__main__':
    main()
