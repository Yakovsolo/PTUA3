import time

class Carrier:
    """Shuttle cost currency is USD    
    Shutlle weight is in kg    
    Year built should be in this format: YYYY"""    
    
    def __init__(self,cost: float, year_built: int, weight: float) -> None:
        self._cost: float = cost        
        self._year_built: int = year_built        
        self._weight: float = weight    
        
    def get_age(self) -> int:
        current_timestamp = time.time()
        current_year = time.gmtime(current_timestamp).tm_year        
        return current_year - self._year_built    
    
    def get_cost(self) -> float:
        return self._cost    
    
    def get_weight(self) -> float:
        return self._weight
    

class SpaceShuttle(Carrier):
    pass