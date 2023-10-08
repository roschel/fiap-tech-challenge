from abc import ABC, abstractmethod

from core.domain.entities.order import Order, Combo

class IOrderCase(ABC):
    
    @abstractmethod
    def create_order(self, order: Order):
        """
        Create a new order.
        Args:
            order (Order): The order to be created.
        Returns:
            Order: The created order.
        """
        pass
   
    @abstractmethod
    def create_combo(self, combo: Combo):
        """
        Create a new combo.
        Args:
            combo (Combo): The combo to be created.
        Returns:
            Combo: The created combo.
        """
        pass
    
    # Additional methods related to orders and combos can be added here