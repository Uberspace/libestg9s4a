import datetime as DT
import typing
from enum import Flag, auto

from .day import Day


class Reimbursements(Flag):
    MEALS_FULL = auto()
    MEALS_REDUCED = auto()
    HOTEL = auto()


class Deductions(Flag):
    BREAKFAST = auto()
    LUNCH = auto()
    DINNER = auto()
    HOTEL = auto()
