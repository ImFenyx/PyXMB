#!/usr/bin/env python3
"""
Generate a sample configuration file for PyXMB.

This script creates a configuration file with example categories and items
that can be customized by the user.
"""

import json
import sys
import os
from pathlib import Path


def generate_config(output_path: str = None, extended: bool = False):
    """Generate a sample configuration file.
    
    Args:
        output_path: Path where to save the config. If None, prints to stdout.
        extended: If True, includes additional categories and items.
    """
    
    if extended:
        # Extended configuration with more categories and items
        config = {
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
                        },
                        {
                            "name": "Gerenciador de Arquivos",
                            "type": "launcher",
                            "command": "nautilus"
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
                        },
                        {
                            "name": "GIMP",
                            "type": "launcher",
                            "command": "gimp"
                        },
                        {
                            "name": "Inkscape",
                            "type": "launcher",
                            "command": "inkscape"
                        }
                    ]
                },
                {
                    "name": "Músicas",
                    "icon": "music",
                    "items": [
                        {
                            "name": "Rhythmbox",
                            "type": "launcher",
                            "command": "rhythmbox"
                        },
                        {
                            "name": "Spotify",
                            "type": "launcher",
                            "command": "spotify"
                        },
                        {
                            "name": "Audacity",
                            "type": "launcher",
                            "command": "audacity"
                        }
                    ]
                },
                {
                    "name": "Vídeos",
                    "icon": "videos",
                    "items": [
                        {
                            "name": "VLC",
                            "type": "launcher",
                            "command": "vlc"
                        },
                        {
                            "name": "MPV",
                            "type": "launcher",
                            "command": "mpv"
                        },
                        {
                            "name": "OBS Studio",
                            "type": "launcher",
                            "command": "obs"
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
                        },
                        {
                            "name": "Lutris",
                            "type": "launcher",
                            "command": "lutris"
                        },
                        {
                            "name": "RetroArch",
                            "type": "launcher",
                            "command": "retroarch"
                        }
                    ]
                },
                {
                    "name": "Internet",
                    "icon": "network",
                    "items": [
                        {
                            "name": "Firefox",
                            "type": "launcher",
                            "command": "firefox"
                        },
                        {
                            "name": "Chrome",
                            "type": "launcher",
                            "command": "google-chrome"
                        },
                        {
                            "name": "Discord",
                            "type": "launcher",
                            "command": "discord"
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
    else:
        # Basic configuration
        config = {
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
    
    config_json = json.dumps(config, indent=2, ensure_ascii=False)
    
    if output_path:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(config_json)
        
        print(f"✓ Configuration file created: {output_path}")
        print(f"\nTo use this configuration, run:")
        print(f"  pyxmb --config {output_path}")
    else:
        print(config_json)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate a sample PyXMB configuration file"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output file path (default: print to stdout)"
    )
    parser.add_argument(
        "-e", "--extended",
        action="store_true",
        help="Generate extended configuration with more items"
    )
    parser.add_argument(
        "-d", "--default",
        action="store_true",
        help="Save to default user config location (~/.pyxmb/config.json)"
    )
    
    args = parser.parse_args()
    
    if args.default:
        output_path = os.path.join(
            os.path.expanduser("~"),
            ".pyxmb",
            "config.json"
        )
        
        # Check if file exists
        if os.path.exists(output_path):
            response = input(f"File {output_path} already exists. Overwrite? (y/N): ")
            if response.lower() != 'y':
                print("Cancelled.")
                return 0
    else:
        output_path = args.output
    
    generate_config(output_path, args.extended)
    return 0


if __name__ == "__main__":
    sys.exit(main())
