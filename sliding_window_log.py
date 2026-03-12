import time
from collections import deque


class SlidingWindowLog:
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.log = deque()

    def allow_request(self):
        now = time.time()
        window_start = now - self.window_size

        while self.log and self.log[0] <= window_start:
            self.log.popleft()

        if len(self.log) < self.limit:
            self.log.append(now)
            return True
        return False

