

class Rhombus:
    def __init__(self, side_a, angle_a):
        if side_a <= 0:
            raise ValueError("A side must > 0.")
        if not (0 < angle_a < 180):
            raise ValueError("Angle must be in range 0 - 180")

        setattr(self, 'side_a', side_a)
        setattr(self, 'angle_a', angle_a)

        setattr(self, 'angle_b', 180 - angle_a)
