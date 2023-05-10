def bmi(weight: float, height: float) -> float:
    if height <= 1 or height > 3:
        raise ValueError("Invalid height")
    if weight <= 30 or weight > 200:
        raise ValueError("Invalid weight")
    return round(weight / (height**2), 14)


if __name__ == "__main__":
    print(bmi(weight=89, height=1.78))
