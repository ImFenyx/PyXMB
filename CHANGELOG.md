# Changelog

All notable changes to PyXMB will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-11-04

### Added

#### Core Features
- XMB-style desktop launcher with horizontal category navigation
- Vertical sub-item navigation within categories
- Animated wave background effects for visual appeal
- Smooth transitions and scaling effects between menu items
- Breadcrumb navigation display showing current location

#### Input Support
- Full keyboard support (Arrow keys, WASD)
- Gamepad/controller support (D-pad, analog sticks, buttons)
- Input debouncing for smooth navigation (200ms delay)
- Configurable key mappings via JSON

#### Application Launcher
- Launch external applications and commands
- Execute built-in actions (system info, about)
- Cross-platform command execution (Windows, Linux, macOS)
- Background process launching

#### Configuration System
- JSON-based configuration files
- Default configuration auto-generation
- User config location (~/.pyxmb/config.json)
- Customizable categories and items
- Theme customization (colors, icon size)

#### Default Categories
- Configurações (Settings) - System info and about
- Fotos (Photos) - Image viewer
- Músicas (Music) - Music player
- Vídeos (Videos) - Video player
- Jogos (Games) - Game launcher (Steam)

#### Developer Tools
- Module test suite (`test_pyxmb.py`)
- Interactive demo script (`demo.py`)
- Visual demo launcher (`run_demo.py`)
- Configuration generator utility (`generate_config.py`)
- Example configuration file (`config.example.json`)

#### Documentation
- Comprehensive README in Portuguese
- Installation and usage instructions
- Keyboard and gamepad control reference
- Configuration guide with examples
- Contributing guidelines (`CONTRIBUTING.md`)
- MIT License

#### Package Management
- pip installable package
- Entry point console script (`pyxmb` command)
- Requirements specification (pygame >= 2.5.0)
- Python 3.8+ support

### Technical Details

#### Architecture
- Modular design with separate concerns:
  - `main.py` - Application loop and state management
  - `config.py` - Configuration loading and persistence
  - `renderer.py` - UI rendering and animations
  - `input_handler.py` - Input handling and mapping
  - `launcher.py` - Application launching

#### Rendering Features
- 60 FPS rendering loop
- Multiple animated wave layers (3 waves)
- Dynamic scaling based on selection
- Alpha blending for depth effect
- Text rendering with multiple fonts

#### Input Features
- Joystick/gamepad auto-detection
- Analog stick deadzone (0.5)
- D-pad and hat switch support
- Button mapping (A/Cross = Select, B/Circle = Back)

[0.1.0]: https://github.com/ImFenyx/PyXMB/releases/tag/v0.1.0
