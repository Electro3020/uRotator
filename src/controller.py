""" Controller simulator """
import time


class Controller:
    def __init__(self, limits: tuple):
        self.sensor_az = 0.0 # north
        self.sensor_al = 0.0 # horizon
        self.target_az = 0.0
        self.target_al = 0.0

        self.limits = limits

        self.is_rotating = False
        self.rotator_speed = 0.0

        self.sim_az = 90.0 # east
        self.sim_al = 45.0 # halfway up
        self.sim_init_time = time.time()
        self.sim_az_mot_spd = 12.0 # 12 degrees per second
        self.sim_al_mod_spd = 8.0
        self.time_since_value_set = 0

    def read_sensors(self):
        self.sensor_az = self.sim_az
        self.sensor_al = self.sim_al

    def begin_rotating(self):
        pass
