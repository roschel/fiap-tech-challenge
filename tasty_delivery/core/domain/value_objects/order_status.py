from enum import Enum


class OrderStatus(Enum):
    RECEIVED = 1
    DOING = 2
    FINISHED = 3
    DELIVERED = 4
