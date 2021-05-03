import numpy as np
from datetime import datetime, timedelta


class WalkingCalculator:

    def __init__(self, goal, start_date, end_date, file_path):
        self.goal = goal
        self.start_date = start_date
        self.end_date = end_date
        f = open(file_path, "r")
        self.kms = [round(float(num), 2) for num in f.read().splitlines()]
        self.sum = round(np.sum(self.kms), 2)
        self.avg = round(np.average(self.kms), 2)
        self.now = self.start_date + timedelta(days=len(self.kms))

    def calculate_remaining_average(self):
        remaining_days = (self.end_date - self.now).days
        remaining_distance = self.goal - self.sum
        remaining_average = remaining_distance / remaining_days
        return remaining_average

    def calculate_trend_end_date(self):
        trend_duration = round(self.goal / self.avg, 2)
        trend_end_date = self.start_date + timedelta(days=trend_duration)
        return trend_end_date

    def calculate_potential_distance(self):
        remaining_days = (self.end_date - self.now).days
        potential_distance = remaining_days * self.avg + self.sum
        return potential_distance
