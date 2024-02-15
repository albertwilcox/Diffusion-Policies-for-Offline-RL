import argparse
import os
import json
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo')
    parser.add_argument('--experiment')
    parser.add_argument('--group')
    args = parser.parse_args()

    envs = os.listdir('results')

    means = []

    for env in envs:
        folder = os.path.join('results', env, args.algo, args.experiment, args.group)
        avgs = []
        for seed in os.listdir(folder):
            data_file = os.path.join(folder, seed, 'best_score_offline.txt')
            with open(data_file, 'r') as f:
                data = json.load(f)
            avg = data['best normalized score avg']
            avgs.append(avg)
        mean = np.mean(avgs)
        std = np.std(avgs)
        print(env, mean, std)

        means.append(mean)
    
    print('Total', np.sum(means))
