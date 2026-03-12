import time


class FixedWindowCounter:
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.current_window = self._get_window()
        self.count = 0

    def _get_window(self):
        return int(time.time() / self.window_size)

    def allow_request(self):
        window = self._get_window()
        if window != self.current_window:
            self.current_window = window
            self.count = 0

        if self.count < self.limit:
            self.count += 1
            return True
        return False

