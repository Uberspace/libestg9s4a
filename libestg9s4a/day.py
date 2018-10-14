import itertools


class Day:
    def __init__(self, day, reimbursements, deductions):
        self.day = day
        self.reimbursements = reimbursements
        self.deductions = deductions
        # TODO: enforce +/- of reimbursements/deductions?

    @property
    def amount(self):
        return sum(
            itertools.chain(
                self.reimbursements.values(),
                self.deductions.values(),
            )
        )
