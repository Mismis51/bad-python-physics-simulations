from math import sin, cos, sqrt, atan

class ObjectTrajectory:
    def __init__(self, gravity, initial_position, initial_velocity, angle):
        self.gravity = gravity
        self.position = initial_position
        self.velocity = initial_velocity
        self.angle = angle

    def _y_velocity(self):
        return self.velocity * sin(self.angle)

    def _x_velocity(self):
        return self.velocity * cos(self.angle)

    def _updatePosition(self, elapsed_time, x_velocity, y_velocity):
        self.position[0] += x_velocity * elapsed_time
        self.position[1] += y_velocity * elapsed_time

    def _updateVelocity(self, x_velocity, y_velocity):
        self.angle =  atan(y_velocity / x_velocity)
        self.velocity = sqrt(x_velocity ** 2 + y_velocity ** 2)

    def updateObject(self, elapsed_time):
        w_x_velocity = self._x_velocity()
        w_y_velocity = self._y_velocity() + self.gravity * elapsed_time
        self._updatePosition(elapsed_time, w_x_velocity, w_y_velocity)
        self._updateVelocity(w_x_velocity, w_y_velocity)