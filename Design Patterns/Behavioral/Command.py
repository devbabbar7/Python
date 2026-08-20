from abc import ABC, abstractmethod


# ==========================================
# 1. RECEIVERS (The actual hardware/logic)
# ==========================================
class Light:
    def __init__(self, location: str):
        self.location = location

    def turn_on(self) -> None:
        print(f"[{self.location} Light] Light is ON")

    def turn_off(self) -> None:
        print(f"[{self.location} Light] Light is OFF")


class Stereo:
    def __init__(self):
        self.volume = 0

    def turn_on(self) -> None:
        print("[Stereo] Powered ON")

    def turn_off(self) -> None:
        print("[Stereo] Powered OFF")

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"[Stereo] Volume set to {self.volume}")


# ==========================================
# 2. COMMAND INTERFACE
# ==========================================
class Command(ABC):
    """
    The Command interface declares execution and undo methods.
    """
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# ==========================================
# 3. CONCRETE COMMANDS
# ==========================================
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

    def undo(self) -> None:
        self._light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self) -> None:
        self._light.turn_off()

    def undo(self) -> None:
        self._light.turn_on()


class VolumeUpCommand(Command):
    def __init__(self, stereo: Stereo):
        self._stereo = stereo
        self._previous_volume = 0

    def execute(self) -> None:
        self._previous_volume = self._stereo.volume
        self._stereo.set_volume(self._previous_volume + 10)

    def undo(self) -> None:
        self._stereo.set_volume(self._previous_volume)


# ==========================================
# 4. INVOKER (Remote Control with History)
# ==========================================
class RemoteControl:
    """
    The Invoker issues requests by calling execute() on Command objects.
    Maintains a stack of executed commands to support undo operations.
    """
    def __init__(self):
        self._history: list[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo_button_pressed(self) -> None:
        if not self._history:
            print("[Remote] Nothing to undo.")
            return

        last_command = self._history.pop()
        print("[Remote] Undoing last command:")
        last_command.undo()


# ==========================================
# 5. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Create Receivers
    living_room_light = Light("Living Room")
    stereo = Stereo()

    # Create Commands
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    vol_up = VolumeUpCommand(stereo)

    # Invoker
    remote = RemoteControl()

    print("--- Executing Actions ---")
    remote.execute_command(light_on)
    remote.execute_command(vol_up)
    remote.execute_command(vol_up)

    print("\n--- Undoing Actions Step-by-Step ---")
    remote.undo_button_pressed()  # Undoes volume 20 -> 10
    remote.undo_button_pressed()  # Undoes volume 10 -> 0
    remote.undo_button_pressed()  # Undoes Light ON -> OFF
    remote.undo_button_pressed()  # History empty