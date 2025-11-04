"""Configuration management for PyXMB."""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


class Config:
    """Manages PyXMB configuration."""
    
    def __init__(self, config_path: str = None):
        """Initialize configuration.
        
        Args:
            config_path: Path to configuration file. If None, uses default.
        """
        if config_path is None:
            config_path = os.path.join(os.path.expanduser("~"), ".pyxmb", "config.json")
        
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._get_default_config()
        else:
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration."""
        return {
            "categories": [
                {
                    "name": "Configurações",
                    "icon": "settings",
                    "items": [
                        {
                            "name": "Sistema",
                            "type": "action",
                            "action": "system_info"
                        },
                        {
                            "name": "Sobre",
                            "type": "action",
                            "action": "about"
                        }
                    ]
                },
                {
                    "name": "Fotos",
                    "icon": "photos",
                    "items": [
                        {
                            "name": "Ver Fotos",
                            "type": "launcher",
                            "command": "xdg-open ~/Pictures"
                        }
                    ]
                },
                {
                    "name": "Músicas",
                    "icon": "music",
                    "items": [
                        {
                            "name": "Reprodutor de Música",
                            "type": "launcher",
                            "command": "rhythmbox"
                        }
                    ]
                },
                {
                    "name": "Vídeos",
                    "icon": "videos",
                    "items": [
                        {
                            "name": "Reprodutor de Vídeos",
                            "type": "launcher",
                            "command": "vlc"
                        }
                    ]
                },
                {
                    "name": "Jogos",
                    "icon": "games",
                    "items": [
                        {
                            "name": "Steam",
                            "type": "launcher",
                            "command": "steam"
                        }
                    ]
                }
            ],
            "theme": {
                "background_color": [0, 20, 40],
                "wave_color": [100, 150, 200],
                "text_color": [255, 255, 255],
                "selected_color": [255, 200, 100],
                "icon_size": 64
            },
            "controls": {
                "up": ["UP", "w"],
                "down": ["DOWN", "s"],
                "left": ["LEFT", "a"],
                "right": ["RIGHT", "d"],
                "select": ["RETURN", "SPACE"],
                "back": ["ESCAPE", "BACKSPACE"]
            }
        }
    
    def save(self):
        """Save configuration to file."""
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get_categories(self) -> List[Dict[str, Any]]:
        """Get categories list."""
        return self.config.get("categories", [])
    
    def get_theme(self) -> Dict[str, Any]:
        """Get theme configuration."""
        return self.config.get("theme", {})
    
    def get_controls(self) -> Dict[str, List[str]]:
        """Get control mappings."""
        return self.config.get("controls", {})
