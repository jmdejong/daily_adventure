

class Availability:
    
    def __init__(self, available, visible, reason=""):
        hidden = not visible
        available = available
        reason = reason


hidden = Availability(False, False, "")
available = Availability(True, True, "")

def unavailable(reason):
    return Availability(False, True, reason)
