import os
from typing import Dict, Any
from pathlib import Path

class Config:
    # Base URL for the application
    BASE_URL = "https://the-internet.herokuapp.com"
    
    # Browser settings
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    
    # Timeouts
    DEFAULT_TIMEOUT = 30000  # 30 seconds
    NAVIGATION_TIMEOUT = 60000  # 60 seconds
    
    # Screenshot settings
    SCREENSHOTS_DIR = Path("test-results/screenshots")
    SCREENSHOT_ON_FAILURE = True
    
    # Test data
    TEST_DATA_DIR = Path("test-data")
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """Get all configuration values as a dictionary."""
        return {
            key: value for key, value in cls.__dict__.items()
            if not key.startswith('_') and not callable(value)
        } 