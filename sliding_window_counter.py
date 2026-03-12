import time


class SlidingWindowCounter:
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.current_window = self._get_window()
        self.current_count = 0
        self.previous_count = 0

    def _get_window(self):
        return int(time.time() / self.window_size)

    def allow_request(self):
        now = time.time()
        window = self._get_window()

        if window != self.current_window:
            self.previous_count = self.current_count if window == self.current_window + 1 else 0
            self.current_count = 0
            self.current_window = window

        elapsed_in_window = now - (self.current_window * self.window_size)
        previous_weight = 1 - (elapsed_in_window / self.window_size)
        estimated_count = self.previous_count * previous_weight + self.current_count

        if estimated_count < self.limit:
            self.current_count += 1
            return True
        return False

