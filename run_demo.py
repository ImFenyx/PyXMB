#!/usr/bin/env python3
"""
Visual demonstration script for PyXMB.
Run this to see the XMB interface in action.

Usage:
    python run_demo.py
    
Controls:
    Arrow Keys or WASD - Navigate
    Enter/Space - Select
    ESC - Back/Exit
"""

import os
import sys

# Set SDL to use a dummy video driver if no display is available
# This allows the script to run in headless environments
if os.environ.get('DISPLAY') is None:
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

def main():
    print("=" * 70)
    print("PyXMB Visual Demo")
    print("=" * 70)
    print()
    print("Starting PyXMB launcher...")
    print()
    print("Controls:")
    print("  ← → or A D : Navigate categories (horizontal)")
    print("  ↑ ↓ or W S : Navigate items (vertical)")
    print("  Enter/Space: Select item")
    print("  ESC        : Back/Exit")
    print()
    print("Features you'll see:")
    print("  • Animated wave background")
    print("  • Smooth category transitions")
    print("  • Highlighted selection")
    print("  • Breadcrumb navigation")
    print("  • Help text at bottom")
    print()
    print("=" * 70)
    print()
    
    try:
        from pyxmb.main import main as pyxmb_main
        pyxmb_main()
    except Exception as e:
        print(f"Error running PyXMB: {e}")
        print()
        print("If you're in a headless environment, try running:")
        print("  DISPLAY=:0 python run_demo.py")
        print()
        print("Or run the demo script instead:")
        print("  python demo.py")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
