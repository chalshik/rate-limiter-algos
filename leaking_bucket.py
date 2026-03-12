import time


class LeakingBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.queue = []
        self.leak_rate = leak_rate
        self.last_leak_time = time.time()

    def _leak(self):
        now = time.time()
        elapsed = now - self.last_leak_time
        leaked = int(elapsed * self.leak_rate)
        if leaked > 0:
            self.queue = self.queue[leaked:]
            self.last_leak_time = now

    def allow_request(self, request_id):
        self._leak()
        if len(self.queue) < self.capacity:
            self.queue.append(request_id)
            return True
        return False

