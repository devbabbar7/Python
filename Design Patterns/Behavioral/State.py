from __future__ import annotations
from abc import ABC, abstractmethod


# ==========================================
# 1. STATE INTERFACE
# ==========================================
class VendingMachineState(ABC):
    """
    Declares state-specific methods that every concrete state must implement.
    """
    @abstractmethod
    def insert_coin(self, machine: VendingMachine) -> None:
        pass

    @abstractmethod
    def press_button(self, machine: VendingMachine) -> None:
        pass

    @abstractmethod
    def dispense(self, machine: VendingMachine) -> None:
        pass


# ==========================================
# 2. CONCRETE STATES
# ==========================================
class IdleState(VendingMachineState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[Idle] Coin inserted. Transitioning -> HasMoneyState.")
        machine.set_state(HasMoneyState())

    def press_button(self, machine: VendingMachine) -> None:
        print("[Idle] Error: Please insert a coin first.")

    def dispense(self, machine: VendingMachine) -> None:
        print("[Idle] Error: No transaction in progress.")


class HasMoneyState(VendingMachineState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[HasMoney] Coin already inserted. Press button to select item.")

    def press_button(self, machine: VendingMachine) -> None:
        print("[HasMoney] Item chosen. Transitioning -> DispensingState.")
        machine.set_state(DispensingState())
        machine.dispense()  # Trigger dispensing

    def dispense(self, machine: VendingMachine) -> None:
        print("[HasMoney] Error: Select item before dispensing.")


class DispensingState(VendingMachineState):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("[Dispensing] Error: Busy dispensing, cannot accept coins right now.")

    def press_button(self, machine: VendingMachine) -> None:
        print("[Dispensing] Error: Already dispensing item.")

    def dispense(self, machine: VendingMachine) -> None:
        print("[Dispensing] Success: Dispensing item! Transitioning -> IdleState.")
        machine.set_state(IdleState())


# ==========================================
# 3. CONTEXT
# ==========================================
class VendingMachine:
    """
    Maintains a reference to an instance of a State subclass
    that represents the current state of the VendingMachine.
    """
    def __init__(self) -> None:
        self._state: VendingMachineState = IdleState()

    def set_state(self, state: VendingMachineState) -> None:
        self._state = state

    def insert_coin(self) -> None:
        self._state.insert_coin(self)

    def press_button(self) -> None:
        self._state.press_button(self)

    def dispense(self) -> None:
        self._state.dispense(self)


# ==========================================
# 4. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    machine = VendingMachine()

    print("--- 1. Trying to press button without coin ---")
    machine.press_button()

    print("\n--- 2. Inserting coin and purchasing item ---")
    machine.insert_coin()
    machine.press_button()

    print("\n--- 3. Verifying machine reset to Idle after dispensing ---")
    machine.press_button()