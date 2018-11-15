import numpy as np
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='Log file')
    args = parser.parse_args()

    data = np.genfromtxt(args.file, delimiter=',', names=True)


    plt.figure()
    plt.plot(data['_Episode'], -data['_MeanReward'])
    plt.ylim([0, 100])
    plt.show()

if __name__ == '__main__':
    main()
