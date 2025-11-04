"""Main XMB application."""

import pygame
import sys
from typing import Optional
from .config import Config
from .renderer import XMBRenderer
from .input_handler import InputHandler
from .launcher import Launcher


class XMBApp:
    """Main XMB application."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize XMB application.
        
        Args:
            config_path: Path to configuration file.
        """
        # Initialize pygame
        pygame.init()
        
        # Load configuration
        self.config = Config(config_path)
        
        # Setup display
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PyXMB - Desktop Launcher")
        
        # Initialize components
        self.renderer = XMBRenderer(self.screen, self.config.get_theme())
        self.input_handler = InputHandler(self.config.get_controls())
        self.launcher = Launcher()
        
        # Navigation state
        self.categories = self.config.get_categories()
        self.category_index = 0
        self.item_index = 0
        self.in_category = False  # False = browsing categories, True = browsing items
        
        # Timing
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Input debouncing
        self.last_action_time = 0
        self.action_delay = 200  # milliseconds
    
    def run(self):
        """Run the main application loop."""
        running = True
        
        while running:
            # Handle events
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue
                
                # Get action from input
                action = self.input_handler.get_action(event)
                
                # Debounce input
                if action and (current_time - self.last_action_time) > self.action_delay:
                    self.last_action_time = current_time
                    
                    if action == "back":
                        if self.in_category:
                            # Go back to category browsing
                            self.in_category = False
                            self.item_index = 0
                        else:
                            # Exit application
                            running = False
                    
                    elif action == "select":
                        if self.in_category:
                            # Launch selected item
                            current_items = self._get_current_items()
                            if current_items and 0 <= self.item_index < len(current_items):
                                item = current_items[self.item_index]
                                success = self.launcher.launch_item(item)
                                if success:
                                    print(f"Launched: {item['name']}")
                                else:
                                    print(f"Failed to launch: {item['name']}")
                        else:
                            # Enter category (show items)
                            if self._get_current_items():
                                self.in_category = True
                                self.item_index = 0
                    
                    elif action == "up":
                        if self.in_category:
                            current_items = self._get_current_items()
                            if current_items:
                                self.item_index = (self.item_index - 1) % len(current_items)
                    
                    elif action == "down":
                        if self.in_category:
                            current_items = self._get_current_items()
                            if current_items:
                                self.item_index = (self.item_index + 1) % len(current_items)
                    
                    elif action == "left":
                        if not self.in_category and self.categories:
                            self.category_index = (self.category_index - 1) % len(self.categories)
                            self.item_index = 0
                    
                    elif action == "right":
                        if not self.in_category and self.categories:
                            self.category_index = (self.category_index + 1) % len(self.categories)
                            self.item_index = 0
            
            # Update animations
            self.renderer.update_animation()
            
            # Render
            self.renderer.draw_background()
            
            if self.categories:
                # Draw categories
                self.renderer.draw_categories(self.categories, self.category_index)
                
                # Draw items if in category
                if self.in_category:
                    current_items = self._get_current_items()
                    category_name = self.categories[self.category_index]["name"]
                    self.renderer.draw_items(current_items, self.item_index, category_name)
                    
                    # Draw breadcrumb
                    if current_items and 0 <= self.item_index < len(current_items):
                        item_name = current_items[self.item_index]["name"]
                        self.renderer.draw_breadcrumb(category_name, item_name)
                    else:
                        self.renderer.draw_breadcrumb(category_name)
                else:
                    category_name = self.categories[self.category_index]["name"]
                    self.renderer.draw_breadcrumb(category_name)
            
            # Draw help
            self.renderer.draw_help()
            
            # Update display
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        # Cleanup
        pygame.quit()
    
    def _get_current_items(self):
        """Get items for current category."""
        if self.categories and 0 <= self.category_index < len(self.categories):
            return self.categories[self.category_index].get("items", [])
        return []


def main():
    """Entry point for PyXMB."""
    import argparse
    
    parser = argparse.ArgumentParser(description="PyXMB - Desktop Launcher")
    parser.add_argument("--config", type=str, help="Path to configuration file")
    args = parser.parse_args()
    
    app = XMBApp(config_path=args.config)
    app.run()


if __name__ == "__main__":
    main()
