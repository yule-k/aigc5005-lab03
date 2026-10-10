#fetching; only module using requests

import requests
from .model import tvshow_from_dict

class TVMazeSource:
    """Download TV show records from the TVMaze API and return a list of TVShow instances."""

    def __init__(self, url, timeout=10):
        """Initialize the TVMazeSource with a URL and timeout."""
        self.url = url
        self.timeout = timeout

    def fetch(self):
        """Fetch TV show records from the API and return a list of TVShow instances."""
        response = requests.get(self.url, timeout=self.timeout)
        response.raise_for_status()

        raw_data = response.json()
        shows = []

        for show_data in raw_data:
            show = tvshow_from_dict(show_data)
            shows.append(show)
        return shows