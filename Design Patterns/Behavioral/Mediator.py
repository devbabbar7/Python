from __future__ import annotations
from abc import ABC, abstractmethod


# ==========================================
# 1. MEDIATOR INTERFACE
# ==========================================
class AirTrafficControl(ABC):
    """
    The Mediator interface declares methods for components to notify
    the mediator about various events.
    """
    @abstractmethod
    def request_landing(self, flight: Flight) -> bool:
        pass

    @abstractmethod
    def register_flight(self, flight: Flight) -> None:
        pass


# ==========================================
# 2. BASE COMPONENT (Colleague)
# ==========================================
class Flight(ABC):
    """
    The Base Component stores a reference to a mediator instance.
    It communicates with other flights solely through this mediator.
    """
    def __init__(self, flight_number: str, atc: AirTrafficControl | None = None):
        self.flight_number = flight_number
        self.atc = atc

    def set_mediator(self, atc: AirTrafficControl) -> None:
        self.atc = atc

    @abstractmethod
    def land(self) -> None:
        pass

    @abstractmethod
    def wait_in_holding(self) -> None:
        pass


# ==========================================
# 3. CONCRETE COMPONENTS
# ==========================================
class CommercialAirplane(Flight):
    def land(self) -> None:
        if not self.atc:
            print(f"[{self.flight_number}] No ATC connection! Cannot land.")
            return

        print(f"[{self.flight_number}] Requesting landing clearance from ATC...")
        # Delegate coordination to the Mediator
        if self.atc.request_landing(self):
            print(f"[{self.flight_number}] Successfully landed on the runway.")
        else:
            self.wait_in_holding()

    def wait_in_holding(self) -> None:
        print(f"[{self.flight_number}] Holding pattern: Circling at 10,000 ft.")


# ==========================================
# 4. CONCRETE MEDIATOR
# ==========================================
class AirportTower(AirTrafficControl):
    """
    The Concrete Mediator coordinates all component flights.
    It maintains runway availability and manages flight queues.
    """
    def __init__(self):
        self._flights: list[Flight] = []
        self._is_runway_clear: bool = True

    def register_flight(self, flight: Flight) -> None:
        self._flights.append(flight)
        flight.set_mediator(self)

    def request_landing(self, flight: Flight) -> bool:
        if self._is_runway_clear:
            print(f"[ATC Tower] Clearance GRANTED for {flight.flight_number}. Runway is clear.")
            self._is_runway_clear = False  # Lock runway during landing
            return True
        else:
            print(f"[ATC Tower] Clearance DENIED for {flight.flight_number}. Runway is currently BUSY.")
            return False

    def clear_runway(self) -> None:
        print("\n[ATC Tower] Runway has been cleared for next flight.\n")
        self._is_runway_clear = True


# ==========================================
# 5. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Create the Central Mediator
    tower = AirportTower()

    # 2. Create Components
    flight_aa = CommercialAirplane("AA-101")
    flight_ua = CommercialAirplane("UA-202")

    # 3. Register components with Mediator
    tower.register_flight(flight_aa)
    tower.register_flight(flight_ua)

    # 4. Flight 1 requests landing -> Approved
    flight_aa.land()

    print()

    # 5. Flight 2 requests landing while runway is occupied -> Denied / Waits
    flight_ua.land()

    # 6. Tower clears runway
    tower.clear_runway()

    # 7. Flight 2 retries landing -> Approved
    flight_ua.land()