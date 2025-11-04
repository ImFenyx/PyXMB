# Quick Start Guide - PyXMB

## Installation

```bash
# Clone the repository
git clone https://github.com/ImFenyx/PyXMB.git
cd PyXMB

# Install dependencies
pip install -r requirements.txt

# Install PyXMB
pip install -e .
```

## First Run

```bash
# Run PyXMB
pyxmb
```

On first run, PyXMB will automatically create a default configuration at `~/.pyxmb/config.json`.

## Basic Navigation

### Keyboard
- **← →** - Navigate between categories (horizontal)
- **↑ ↓** - Navigate between items (vertical)
- **Enter** - Select item / Enter category
- **ESC** - Go back / Exit

### Alternative Keys (WASD)
- **A D** - Navigate categories
- **W S** - Navigate items
- **Space** - Select item

### Gamepad
- **D-Pad / Left Stick** - Navigate
- **A Button (Cross)** - Select
- **B Button (Circle)** - Back

## Understanding the Interface

```
     ┌─────────────────────────────────────────┐
     │         PyXMB Launcher                  │
     └─────────────────────────────────────────┘
     
     Wave Background (animated)
     
     [⚙️]    [🖼️]    [🎵]    [🎬]    [🎮]
   Settings Photos Music  Videos Games
                    ↑
              (selected)
              
              Reprodutor de Música
              Steam
              OBS Studio
              
     Help: ← → Navigate | Enter Select | ESC Back
```

## Customization

### Generate Custom Configuration

```bash
# Generate basic config
python generate_config.py -o my-config.json

# Generate extended config with more items
python generate_config.py -e -o my-config.json

# Save to default location
python generate_config.py -d
```

### Edit Configuration

Edit `~/.pyxmb/config.json` to:

1. **Add new categories:**
```json
{
  "name": "My Category",
  "icon": "custom",
  "items": [...]
}
```

2. **Add new items:**
```json
{
  "name": "My App",
  "type": "launcher",
  "command": "my-app"
}
```

3. **Change colors:**
```json
"theme": {
  "background_color": [10, 10, 30],
  "wave_color": [50, 100, 200],
  "text_color": [255, 255, 255],
  "selected_color": [255, 150, 50]
}
```

### Use Custom Configuration

```bash
pyxmb --config /path/to/my-config.json
```

## Common Tasks

### Adding a Game

Edit your config and add to the "Jogos" category:

```json
{
  "name": "My Game",
  "type": "launcher",
  "command": "/path/to/game"
}
```

### Adding a Music Player

Edit your config and add to the "Músicas" category:

```json
{
  "name": "VLC",
  "type": "launcher",
  "command": "vlc"
}
```

### Opening a Folder

```json
{
  "name": "My Documents",
  "type": "launcher",
  "command": "xdg-open ~/Documents"
}
```

## Tips

1. **Test commands first** - Run commands in terminal before adding to PyXMB
2. **Use full paths** - For reliability, use absolute paths for commands
3. **Check installed apps** - Make sure applications are installed and in PATH
4. **Backup config** - Keep a backup of your customized configuration
5. **Start simple** - Begin with a few items and expand gradually

## Troubleshooting

### "Command not found"
- Ensure the application is installed
- Check if the command is in your PATH
- Try using the full path to the executable

### Application doesn't launch
- Test the command in a terminal first
- Check for typos in the command
- Verify the application is installed

### PyXMB won't start
- Check Python version: `python --version` (need 3.8+)
- Reinstall pygame: `pip install --upgrade pygame`
- Check for error messages in terminal

## Next Steps

1. Explore the demo: `python demo.py`
2. Check the example config: `config.example.json`
3. Read the full README: `README.md`
4. Customize your experience!

## Getting Help

- Check CONTRIBUTING.md for guidelines
- Open an issue on GitHub
- Read the documentation in README.md

Enjoy PyXMB! 🎮
