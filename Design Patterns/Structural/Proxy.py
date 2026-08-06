from abc import ABC, abstractmethod
import time


# 1. Subject Interface
class VideoDownloader(ABC):
    """
    The Subject interface declares common operations for both RealVideoDownloader
    and ProxyVideoDownloader. Client code works strictly with this interface.
    """
    @abstractmethod
    def download_video(self, video_id: str) -> str:
        pass


# 2. Real Subject (Heavy & Slow Object)
class RealVideoDownloader(VideoDownloader):
    """
    The RealSubject performs the actual heavy work (e.g., establishing database
    connections, downloading files over network, heavy processing).
    """
    def __init__(self):
        print("[Real Server] Establishing expensive network connection...")

    def download_video(self, video_id: str) -> str:
        print(f"[Real Server] Downloading video '{video_id}' over network...")
        time.sleep(2)  # Simulates 2-second network latency
        return f"Video Data for '{video_id}'"


# 3. Proxy Subject (Controls Access, Caching, and Lazy Loading)
class ProxyVideoDownloader(VideoDownloader):
    """
    The Proxy holds a reference to RealSubject and controls access to it.
    It intercepts calls to handle lazy initialization and caching.
    """
    def __init__(self):
        self._real_downloader = None  # Lazy loading: Not created until needed
        self._cache = {}             # Cache dictionary to store previous downloads

    def download_video(self, video_id: str) -> str:
        # Step 1: Caching Check - return instantly if result already exists
        if video_id in self._cache:
            print(f"[Proxy] Video '{video_id}' found in CACHE! Returning instant result.")
            return self._cache[video_id]

        # Step 2: Lazy Initialization - instantiate real object ONLY on first miss
        if self._real_downloader is None:
            print("[Proxy] First request received. Instantiating RealVideoDownloader...")
            self._real_downloader = RealVideoDownloader()

        # Step 3: Forward call to RealSubject and store result in cache
        print(f"[Proxy] '{video_id}' not in cache. Fetching from Real Server...")
        result = self._real_downloader.download_video(video_id)
        self._cache[video_id] = result

        return result


# --- Client Execution ---
if __name__ == "__main__":
    # Client code interacts only via the Proxy interface
    downloader = ProxyVideoDownloader()

    print("--- Request 1: Fetching 'python_tutorial' ---")
    downloader.download_video("python_tutorial")

    print("\n--- Request 2: Fetching 'python_tutorial' again ---")
    downloader.download_video("python_tutorial")

    print("\n--- Request 3: Fetching 'lld_patterns' ---")
    downloader.download_video("lld_patterns")