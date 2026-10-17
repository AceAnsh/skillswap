"""Time-Credit ledger: 1 minute of teaching earns 1 credit; learners spend credits."""

STARTING_BALANCE = 30


class InsufficientCredits(Exception):
    pass


class Ledger:
    def __init__(self, starting_balance: int = STARTING_BALANCE):
        self.starting_balance = starting_balance
        self.balances = {}
        self.history = []

    def register(self, user_id: str):
        self.balances.setdefault(user_id, self.starting_balance)

    def balance(self, user_id: str) -> int:
        return self.balances[user_id]

    def complete_session(self, teacher_id: str, learner_id: str, minutes: int):
        """Move credits from learner to teacher once a session is completed."""
        if teacher_id == learner_id:
            raise ValueError("teacher and learner must be different users")
        if minutes <= 0:
            raise ValueError("minutes must be positive")
        if self.balances[learner_id] < minutes:
            raise InsufficientCredits(
                f"{learner_id} has {self.balances[learner_id]} credits, needs {minutes}")
        self.balances[learner_id] -= minutes
        self.balances[teacher_id] += minutes
        self.history.append((teacher_id, learner_id, minutes))
