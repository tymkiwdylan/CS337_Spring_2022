# Dylan Tymkiw
# CS337
# Project 2
# 02/16/2022

import re


class Process:
    def __init__(self, id, duty, arrival_time, priority):
        self.id = id
        self.duty = duty
        self.arrival_time = arrival_time
        self.priority = priority
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.status = "running"
        self.queue = 0
        self.isFirst = True

    # Setters
    def set_duty(self, duty):
        self.duty = duty

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def set_priority(self, priority):
        self.priority = priority

    def set_wait_time(self, wait_time):
        self.wait_time = wait_time

    def set_turnaround_time(self, turnaround_time):
        self.turnaround_time = turnaround_time

    def set_response_time(self, response_time):
        self.response_time = response_time

    def toggle_status(self, status):
        self.status = status

    def set_queue(self, queue):
        self.queue = queue

    # Getters
    def get_response_time(self):
        return self.response_time

    def get_status(self):
        return self.status

    def get_queue(self):
        return self.queue

    def get_duty(self):
        return self.duty

    def get_arrival_time(self):
        return self.arrival_time

    def get_priority(self):
        return self.priority

    def get_wait_time(self):
        return self.wait_time

    def get_turnaround_time(self):
        return self.turnaround_time

    def get_ID(self):
        return self.id
