import subprocess
import argparse
import os

class Run_Mono(object):
    def __init__(self):
        return 
    def run(self):
        parser = argparse.ArgumentParser(description='''
        This script runs ORB mono algorithm. 
        ''')
        parser.add_argument('seq', help='sequence number of kitti dataset, like 04')
      
        args = parser.parse_args()
        
        seq = args.seq
        seq_num = int(seq)
        config_file = "03"
        if seq_num <=2:
            config_file = "00-02"
        elif seq_num >=4:
            config_file = "04-12"
        
        cmd = './Examples/Monocular/mono_kitti Vocabulary/ORBvoc.txt Examples/Monocular/KITTI{}.yaml /home/levin/workspace/data/kitti/sequences/{}'.format(config_file, seq)
        print("start executing .......")
        print(cmd)
        os.system(cmd)
        return



if __name__ == '__main__':
    obj = Run_Mono()
    obj.run()
    


