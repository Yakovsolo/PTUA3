# Create a Plane, Boeing, Airbus classes.
# Base class should contain methods to get:  plane name, plane type (A320, B737 etc), max_speed (should be the funciotn: base_speed * model_speed_coeficient).
# Both plane subclasses should only take model type as input argument.

from typing import Optional


class Plane:
    BASE_SPEED = 750

    def __init__(
        self, model_type: str, name_suffix: str, model_speed_coeficient: float
    ) -> None:
        self.model_type = model_type
        self.name_suffix = name_suffix
        self.model_speed_coeficient = model_speed_coeficient

    def get_plane_name(self):
        return self.name_suffix + self.model_type

    def get_model_type(self):
        return self.model_type

    def get_max_speed(self):
        max_speed = self.BASE_SPEED * self.model_speed_coeficient
        return max_speed


class Boeing(Plane):
    NAME_SUFFICS = "B"

    BOEING_TYPE_SPEED_COEF = {
        "737": 1,
        "747": 1.2,
        "757": 1.35,
        "767": 1.5,
        "777": 1.8,
    }

    def __init__(self, model_type: str) -> None:
        self.model_type = model_type
        speed_coef = self._get_type_speed_coef()
        super().__init__(
            model_type=model_type,
            name_suffix=self.NAME_SUFFICS,
            model_speed_coeficient=speed_coef,
        )

    def _get_type_speed_coef(self) -> Optional[float]:
        return self.BOEING_TYPE_SPEED_COEF.get(self.model_type)


class Airbus(Plane):
    NAME_SUFFICS = "A"

    def __init__(self, model_type: str) -> None:
        super().__init__(self.NAME_SUFFICS, model_type=model_type)


my_plane = Boeing("747")

print(my_plane.get_plane_name())
print(f"My-plane max speed is: {my_plane.get_max_speed()} km/h")
