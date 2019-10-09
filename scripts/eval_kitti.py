from mono_eva2 import exec_main
import numpy as np
import matplotlib.pyplot as plt

import argparse

class Object(object):
    pass

class Eval_Kitti(object):
    def __init__(self):
        return 
    def process(self, seq, dst=None):
        args = Object()
        args.ground_time = '/home/levin/workspace/data/kitti/sequences/{}/times.txt'.format(seq)  
        args.ground_data = '/home/levin/workspace/data/kitti/data_odometry_poses/dataset/poses/{}.txt'.format(seq)    
        args.res_time = '/home/levin/workspace/ORB_SLAM2/temp/slam_result/data/{}/KeyFrameTrajectory.txt'.format(seq)  
        if dst is not None:
            args.res_time = dst
        args.verbose = True
        print("gt time={}".format(args.ground_time))
        print("gt data={}".format(args.ground_data))
        print("result file={}".format(args.res_time))
        exec_main(args)
        return
    def run(self):
        parser = argparse.ArgumentParser(description='''
        This script computes the absolute trajectory error from the ground truth trajectory and the estimated trajectory. 
        ''')
        parser.add_argument('seq', help='sequence number of kitti dataset, like 04')
        args = parser.parse_args()
        self.process(args.seq)   
        return



if __name__ == '__main__':
    obj = Eval_Kitti()
    obj.run()
    
    
