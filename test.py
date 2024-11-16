import matplotlib.pyplot as plt
import numpy as np
import random 
import threading
import time

class LidarData():
    def __init__(self) -> None:
        self.b_lidar_daemon = True
        self.START_ANGLE = -137.5
        self.MAXIMUM_ANGLE = 137.5
        self.ANGLE_INCRIMENT = 0.16
        self.zig_angle = 0.0
        self.raser_thickness = 5
        self.wall_data = list(range(1502))
        self.ranges = list(range(1502))
        self.min_angle, self.max_angle = self.start_lidar()
        
    
    def start_lidar(self):
        min_angle = self.START_ANGLE + random.random() * self.ANGLE_INCRIMENT
        max_angle = ((self.MAXIMUM_ANGLE - min_angle) // self. ANGLE_INCRIMENT) * self. ANGLE_INCRIMENT + min_angle
        return min_angle, max_angle
    
    
    def ranges_creater(self, noise_range):
        self.ranges = [self.wall_data[i] + (random.random() * noise_range) for i in range(len(self.wall_data))] 
        
        
    def lidar_runner(self):
        while self.b_lidar_daemon:
            self.ranges_creater(0.1)
            time.sleep(0.01)
            

class CalLidarTest():
    def __init__(self) -> None:
        pass
    
    
def main():
    lidar = LidarData()
    lidar_thread = threading.Thread(target=lidar.lidar_runner)
    lidar_thread.start()
    lidar_thread.join()
    
    
if __name__ == "__main__":
    main()