

class Availability:
    
    def __init__(self, visible, available, reason=None):
        self.hidden = not visible
        self.available = available
        self.reason = reason

