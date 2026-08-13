from abc import ABC, abstractmethod


# ==========================================
# 1. IMPLEMENTATION HIERARCHY (Hardware/Engine)
# ==========================================
class Device(ABC):
    """
    The Implementation interface defines low-level operations.
    Concrete implementations match these methods to specific hardware.
    """
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        pass


class TV(Device):
    def turn_on(self) -> None:
        print("[TV] Display screen ON")

    def turn_off(self) -> None:
        print("[TV] Display screen OFF")

    def set_volume(self, percent: int) -> None:
        print(f"[TV] Speakers volume set to {percent}%")


class Radio(Device):
    def turn_on(self) -> None:
        print("[Radio] Audio tuner ON")

    def turn_off(self) -> None:
        print("[Radio] Audio tuner OFF")

    def set_volume(self, percent: int) -> None:
        print(f"[Radio] Dial volume set to {percent}%")


# ==========================================
# 2. ABSTRACTION HIERARCHY (Control Layer)
# ==========================================
class RemoteControl:
    """
    The Abstraction defines high-level control logic.
    It maintains a reference to an Implementation object (The Bridge).
    """
    def __init__(self, device: Device):
        self._device = device  # The Bridge

    def toggle_power(self) -> None:
        self._device.turn_on()

    def volume_up(self) -> None:
        self._device.set_volume(50)


class AdvancedRemoteControl(RemoteControl):
    """
    Refined Abstraction extends the control layer with new features
    without modifying any implementation classes.
    """
    def mute(self) -> None:
        print("[Advanced Remote] Muting device...")
        self._device.set_volume(0)


# ==========================================
# 3. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Case 1: Standard remote controlling a TV
    tv = TV()
    basic_remote = RemoteControl(tv)
    basic_remote.toggle_power()
    basic_remote.volume_up()

    print()

    # Case 2: Advanced remote controlling a Radio (Any Remote + Any Device!)
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.mute()