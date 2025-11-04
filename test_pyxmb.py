#!/usr/bin/env python3
"""Simple tests for PyXMB modules."""

import sys
import os

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    try:
        import pyxmb
        print(f"✓ pyxmb version: {pyxmb.__version__}")
        
        from pyxmb.config import Config
        print("✓ Config imported")
        
        from pyxmb.launcher import Launcher
        print("✓ Launcher imported")
        
        # These require pygame display, so just check import
        try:
            from pyxmb.renderer import XMBRenderer
            print("✓ XMBRenderer imported")
        except Exception as e:
            print(f"⚠ XMBRenderer import warning (expected without display): {e}")
        
        try:
            from pyxmb.input_handler import InputHandler
            print("✓ InputHandler imported")
        except Exception as e:
            print(f"⚠ InputHandler import warning (expected without display): {e}")
        
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_config():
    """Test configuration management."""
    print("\nTesting configuration...")
    try:
        from pyxmb.config import Config
        
        # Create config with test path
        test_path = "/tmp/test_pyxmb_config.json"
        if os.path.exists(test_path):
            os.remove(test_path)
        
        config = Config(test_path)
        
        # Check default config
        categories = config.get_categories()
        assert len(categories) > 0, "Should have default categories"
        print(f"✓ Default config has {len(categories)} categories")
        
        # Check category names
        category_names = [c["name"] for c in categories]
        expected_names = ["Configurações", "Fotos", "Músicas", "Vídeos", "Jogos"]
        for name in expected_names:
            assert name in category_names, f"Missing category: {name}"
        print(f"✓ All expected categories present: {', '.join(expected_names)}")
        
        # Check theme
        theme = config.get_theme()
        assert "background_color" in theme, "Theme should have background_color"
        assert "text_color" in theme, "Theme should have text_color"
        print("✓ Theme configuration valid")
        
        # Check controls
        controls = config.get_controls()
        assert "up" in controls, "Controls should have 'up'"
        assert "select" in controls, "Controls should have 'select'"
        print("✓ Control configuration valid")
        
        # Save config
        config.save()
        assert os.path.exists(test_path), "Config file should be saved"
        print(f"✓ Config saved to {test_path}")
        
        # Cleanup
        if os.path.exists(test_path):
            os.remove(test_path)
        
        return True
    except Exception as e:
        print(f"✗ Config test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_launcher():
    """Test launcher functionality."""
    print("\nTesting launcher...")
    try:
        from pyxmb.launcher import Launcher
        
        launcher = Launcher()
        print(f"✓ Launcher created for system: {launcher.system}")
        
        # Test action execution (safe actions that just print)
        test_item = {
            "name": "About",
            "type": "action",
            "action": "about"
        }
        
        result = launcher.launch_item(test_item)
        assert result == True, "About action should succeed"
        print("✓ Action execution works")
        
        return True
    except Exception as e:
        print(f"✗ Launcher test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("PyXMB Module Tests")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Config", test_config()))
    results.append(("Launcher", test_launcher()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
