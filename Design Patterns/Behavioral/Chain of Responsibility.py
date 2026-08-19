from __future__ import annotations
from abc import ABC, abstractmethod


# ==========================================
# 1. BASE HANDLER
# ==========================================
class Approver(ABC):
    """
    The Base Handler defines a method for building the chain and
    declares the request-handling method.
    """
    def __init__(self) -> None:
        self._next_approver: Approver | None = None

    def set_next(self, next_approver: Approver) -> Approver:
        self._next_approver = next_approver
        return next_approver  # Enables method chaining

    @abstractmethod
    def approve(self, amount: float, purpose: str) -> None:
        pass

    def pass_to_next(self, amount: float, purpose: str) -> None:
        if self._next_approver:
            self._next_approver.approve(amount, purpose)
        else:
            print(f"[X - REJECTED] No approver could process ${amount:.2f} for '{purpose}'.")


# ==========================================
# 2. CONCRETE HANDLERS
# ==========================================
class TeamLead(Approver):
    def approve(self, amount: float, purpose: str) -> None:
        if amount <= 500:
            print(f"[Team Lead] Approved ${amount:.2f} for '{purpose}'.")
        else:
            print(f"[Team Lead] ${amount:.2f} exceeds limit ($500). Passing along...")
            self.pass_to_next(amount, purpose)


class Manager(Approver):
    def approve(self, amount: float, purpose: str) -> None:
        if amount <= 2500:
            print(f"[Manager] Approved ${amount:.2f} for '{purpose}'.")
        else:
            print(f"[Manager] ${amount:.2f} exceeds limit ($2,500). Passing along...")
            self.pass_to_next(amount, purpose)


class Director(Approver):
    def approve(self, amount: float, purpose: str) -> None:
        if amount <= 10000:
            print(f"[Director] Approved ${amount:.2f} for '{purpose}'.")
        else:
            print(f"[Director] ${amount:.2f} exceeds limit ($10,000). Passing along...")
            self.pass_to_next(amount, purpose)


# ==========================================
# 3. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Create handler instances
    team_lead = TeamLead()
    manager = Manager()
    director = Director()

    # Link the chain: TeamLead -> Manager -> Director
    team_lead.set_next(manager).set_next(director)

    print("--- Request 1: $150 (Team Lunch) ---")
    team_lead.approve(150.00, "Team Lunch")

    print("\n--- Request 2: $1,200 (New Laptop) ---")
    team_lead.approve(1200.00, "Developer Laptop")

    print("\n--- Request 3: $8,500 (Annual Cloud Hosting) ---")
    team_lead.approve(8500.00, "Cloud Hosting Reserve")

    print("\n--- Request 4: $50,000 (New Office Lease) ---")
    team_lead.approve(50000.00, "New Office Lease")