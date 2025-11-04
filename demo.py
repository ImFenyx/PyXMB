#!/usr/bin/env python3
"""
Demo script for PyXMB that can run in headless mode for testing.
This demonstrates the configuration and structure without requiring a display.
"""

import os
import sys


def demo_configuration():
    """Demonstrate configuration loading and structure."""
    print("=" * 70)
    print("PyXMB Configuration Demo")
    print("=" * 70)
    
    from pyxmb.config import Config
    
    # Create a demo config
    config = Config("/tmp/pyxmb_demo_config.json")
    
    print("\n📋 Categories and Items:")
    print("-" * 70)
    
    categories = config.get_categories()
    for i, category in enumerate(categories, 1):
        print(f"\n{i}. 📁 {category['name']}")
        items = category.get('items', [])
        for j, item in enumerate(items, 1):
            item_type = item.get('type', 'unknown')
            if item_type == 'launcher':
                detail = f"Command: {item.get('command', 'N/A')}"
            elif item_type == 'action':
                detail = f"Action: {item.get('action', 'N/A')}"
            else:
                detail = "Unknown type"
            print(f"   {i}.{j} • {item['name']} ({detail})")
    
    print("\n" + "-" * 70)
    print("\n🎨 Theme Configuration:")
    print("-" * 70)
    
    theme = config.get_theme()
    print(f"Background Color: RGB{tuple(theme['background_color'])}")
    print(f"Wave Color:       RGB{tuple(theme['wave_color'])}")
    print(f"Text Color:       RGB{tuple(theme['text_color'])}")
    print(f"Selected Color:   RGB{tuple(theme['selected_color'])}")
    print(f"Icon Size:        {theme['icon_size']}px")
    
    print("\n" + "-" * 70)
    print("\n🎮 Control Mapping:")
    print("-" * 70)
    
    controls = config.get_controls()
    for action, keys in controls.items():
        print(f"{action.capitalize():12} → {', '.join(keys)}")
    
    print("\n" + "=" * 70)


def demo_navigation_simulation():
    """Simulate navigation through the menu structure."""
    print("\n" + "=" * 70)
    print("Navigation Simulation")
    print("=" * 70)
    
    from pyxmb.config import Config
    
    config = Config("/tmp/pyxmb_demo_config.json")
    categories = config.get_categories()
    
    print("\nSimulating user navigation through the XMB interface:\n")
    
    # Simulate browsing categories
    print("📍 Starting at category: Configurações")
    print("➡️  Moving right...")
    print("📍 Now at category: Fotos")
    print("➡️  Moving right...")
    print("📍 Now at category: Músicas")
    print("⬇️  Entering category (pressing Enter)...")
    
    # Simulate browsing items in Music category
    music_category = next((c for c in categories if c['name'] == 'Músicas'), None)
    if music_category:
        items = music_category.get('items', [])
        if items:
            print(f"\n   ▶️  Selected: {items[0]['name']}")
            print(f"   📝 Type: {items[0].get('type', 'unknown')}")
            print(f"   💻 Command: {items[0].get('command', 'N/A')}")
    
    print("\n⬆️  Moving up (staying in same category)")
    print("◀️  Going back to categories (pressing ESC)")
    print("➡️  Moving right to Vídeos...")
    print("➡️  Moving right to Jogos...")
    print("⬇️  Entering Jogos category...")
    
    games_category = next((c for c in categories if c['name'] == 'Jogos'), None)
    if games_category:
        items = games_category.get('items', [])
        if items:
            print(f"\n   ▶️  Selected: {items[0]['name']}")
            print(f"   💻 Would launch: {items[0].get('command', 'N/A')}")
    
    print("\n🚪 Exiting application (pressing ESC at top level)")
    print("\n" + "=" * 70)


def demo_ascii_interface():
    """Show an ASCII representation of the XMB interface."""
    print("\n" + "=" * 70)
    print("ASCII Representation of XMB Interface")
    print("=" * 70)
    
    print("""
    ╔════════════════════════════════════════════════════════════════════╗
    ║                          PyXMB Launcher                            ║
    ╚════════════════════════════════════════════════════════════════════╝
    
         ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
        ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
       ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
    
             ┌─────┐      ┌─────┐      ╔═════╗      ┌─────┐      ┌─────┐
             │     │      │     │      ║     ║      │     │      │     │
             │ ⚙️  │      │ 🖼️  │      ║ 🎵  ║      │ 🎬  │      │ 🎮  │
             │     │      │     │      ║     ║      │     │      │     │
             └─────┘      └─────┘      ╚═════╝      └─────┘      └─────┘
          Configurações   Fotos       Músicas      Vídeos       Jogos
                                         ▲
                                         │
                                    (Selected)
    
                                   ▸ Reprodutor de Música
                                     (Player available)
    
    ────────────────────────────────────────────────────────────────────
    ← → Navegar | ↑ ↓ Selecionar | Enter Confirmar | ESC Voltar/Sair
    ────────────────────────────────────────────────────────────────────
    """)
    
    print("=" * 70)


def demo_features():
    """List key features of PyXMB."""
    print("\n" + "=" * 70)
    print("PyXMB Features")
    print("=" * 70)
    
    features = [
        ("🎨 XMB-Style Interface", "Horizontal categories with vertical items"),
        ("🌊 Animated Waves", "Smooth wave animations in the background"),
        ("⌨️  Keyboard Support", "Full keyboard navigation (arrows, WASD)"),
        ("🎮 Gamepad Support", "Compatible with most game controllers"),
        ("🚀 Application Launcher", "Launch external apps and games"),
        ("⚙️  Configurable", "JSON-based configuration system"),
        ("🎨 Customizable Themes", "Adjust colors to your preference"),
        ("📦 Modular Design", "Clean, maintainable code structure"),
    ]
    
    for title, description in features:
        print(f"\n{title}")
        print(f"  └─ {description}")
    
    print("\n" + "=" * 70)


def main():
    """Run all demos."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 20 + "PyXMB DEMONSTRATION" + " " * 29 + "║")
    print("╚" + "═" * 68 + "╝")
    
    demo_configuration()
    demo_navigation_simulation()
    demo_ascii_interface()
    demo_features()
    
    print("\n" + "=" * 70)
    print("To run PyXMB with GUI:")
    print("  $ pyxmb")
    print("\nTo run with custom config:")
    print("  $ pyxmb --config /path/to/config.json")
    print("\nFor more information, see README.md")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
