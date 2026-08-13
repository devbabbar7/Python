# ==========================================
# 1. SUBSYSTEM CLASSES (Complex Details)
# ==========================================
class Amplifier:
    def turn_on(self) -> None:
        print("[Amplifier] Power ON")

    def set_volume(self, level: int) -> None:
        print(f"[Amplifier] Volume set to {level}")

    def turn_off(self) -> None:
        print("[Amplifier] Power OFF")


class Projector:
    def turn_on(self) -> None:
        print("[Projector] Lamp warming up... ON")

    def set_input_hdmi(self) -> None:
        print("[Projector] Input set to HDMI 1")

    def turn_off(self) -> None:
        print("[Projector] Cooling down... OFF")


class SmartLights:
    def dim(self, level: int) -> None:
        print(f"[Smart Lights] Dimmed to {level}%")


class StreamingPlayer:
    def turn_on(self) -> None:
        print("[Streaming Player] Loaded home screen")

    def play_movie(self, movie: str) -> None:
        print(f"[Streaming Player] Playing '{movie}'")

    def turn_off(self) -> None:
        print("[Streaming Player] Power OFF")


# ==========================================
# 2. FACADE CLASS (Simplified Interface)
# ==========================================
class HomeTheaterFacade:
    """
    The Facade delegates client requests to appropriate subsystem objects,
    hiding the complexity of managing multiple objects in a specific order.
    """
    def __init__(
        self,
        amp: Amplifier,
        projector: Projector,
        lights: SmartLights,
        player: StreamingPlayer,
    ):
        self._amp = amp
        self._projector = projector
        self._lights = lights
        self._player = player

    def watch_movie(self, movie_name: str) -> None:
        """One simple method replaces dozens of manual subsystem calls."""
        print(f"\n--- Setting up Home Theater for '{movie_name}' ---")
        self._lights.dim(10)
        self._projector.turn_on()
        self._projector.set_input_hdmi()
        self._amp.turn_on()
        self._amp.set_volume(30)
        self._player.turn_on()
        self._player.play_movie(movie_name)
        print("--- Enjoy the movie! ---")

    def end_movie(self) -> None:
        print("\n--- Shutting down Home Theater ---")
        self._lights.dim(100)
        self._player.turn_off()
        self._amp.turn_off()
        self._projector.turn_off()
        print("--- Home Theater Off ---")


# ==========================================
# 3. CLIENT EXECUTION
# ==========================================
if __name__ == "__main__":
    # Initialize complex subsystem objects
    amp = Amplifier()
    projector = Projector()
    lights = SmartLights()
    player = StreamingPlayer()

    # Pass subsystem instances into Facade
    home_theater = HomeTheaterFacade(amp, projector, lights, player)

    # Client interacts ONLY with the Facade!
    home_theater.watch_movie("Interstellar")
    home_theater.end_movie()