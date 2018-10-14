import datetime as DT

from libestg9s4a import Day, Deductions, Reimbursements


def test_day():
    d = Day(
        day=DT.date(2018, 5, 1),
        reimbursements={
            Reimbursements.MEALS_FULL: 10,
            Reimbursements.HOTEL: 100,
        },
        deductions={
            Deductions.BREAKFAST: -5,
        }
    )

    assert d.amount == 105
