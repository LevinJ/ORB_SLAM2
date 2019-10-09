import subprocess
import argparse
import os
import shutil
from scripts.eval_kitti import Eval_Kitti

class Run_Mono(object):
    def __init__(self):
        return 
    def eval_result(self, seq, dst):
        print("Evaludate sequence {}, result file={}".format(seq, dst))
        obj = Eval_Kitti()
        obj.process(seq, dst = dst)
        return
    def run_orb(self, seq):
        seq_num = int(seq)
        config_file = "03"
        if seq_num <=2:
            config_file = "00-02"
        elif seq_num >=4:
            config_file = "04-12"
        
        cmd = './Examples/Monocular/mono_kitti Vocabulary/ORBvoc.txt ./Examples/Monocular/KITTI{}.yaml /home/levin/workspace/data/kitti/sequences/{}'.format(config_file, seq)
        print("start executing .......")
        print(cmd)
        os.system(cmd)
        return
    def run(self):
        parser = argparse.ArgumentParser(description='''
        This script runs ORB mono algorithm. 
        ''')
        parser.add_argument('seq', help='sequence number of kitti dataset, like 04')
      
        args = parser.parse_args()
        
        seq = args.seq
        
        
        src = './KeyFrameTrajectory.txt'
        dst_path = './temp/slam_result/data/{}'.format(seq)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst = dst_path + "/KeyFrameTrajectory.txt"
        dst = os.path.abspath(dst)
        
        if not os.path.exists(dst):
            self.run_orb(seq)
            shutil.copyfile(src, dst)    
            print("Copy file from {} to {}".format(src, dst))
        self.eval_result(seq, dst)
        return



if __name__ == '__main__':
    obj = Run_Mono()
    obj.run()
    


