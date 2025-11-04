"""XMB UI rendering for PyXMB."""

import pygame
import math
from typing import List, Dict, Any, Tuple


class XMBRenderer:
    """Renders the XMB interface."""
    
    def __init__(self, screen: pygame.Surface, theme: Dict[str, Any]):
        """Initialize renderer.
        
        Args:
            screen: Pygame screen surface.
            theme: Theme configuration.
        """
        self.screen = screen
        self.theme = theme
        self.width, self.height = screen.get_size()
        
        # Animation parameters
        self.wave_offset = 0.0
        self.wave_speed = 0.02
        
        # Fonts
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 48)
        self.item_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Colors from theme
        self.bg_color = tuple(theme.get("background_color", [0, 20, 40]))
        self.wave_color = tuple(theme.get("wave_color", [100, 150, 200]))
        self.text_color = tuple(theme.get("text_color", [255, 255, 255]))
        self.selected_color = tuple(theme.get("selected_color", [255, 200, 100]))
    
    def update_animation(self):
        """Update animation parameters."""
        self.wave_offset += self.wave_speed
        if self.wave_offset > 2 * math.pi:
            self.wave_offset -= 2 * math.pi
    
    def draw_background(self):
        """Draw animated background with waves."""
        self.screen.fill(self.bg_color)
        
        # Draw wave effect
        wave_height = self.height // 3
        num_waves = 3
        
        for wave_idx in range(num_waves):
            points = []
            amplitude = 30 + wave_idx * 10
            frequency = 0.01 + wave_idx * 0.002
            phase = self.wave_offset + wave_idx * math.pi / 3
            
            for x in range(0, self.width + 10, 10):
                y = wave_height + amplitude * math.sin(frequency * x + phase)
                points.append((x, y))
            
            # Draw wave line
            if len(points) > 1:
                alpha = 50 - wave_idx * 15
                wave_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                pygame.draw.lines(wave_surface, (*self.wave_color, alpha), False, points, 2)
                self.screen.blit(wave_surface, (0, 0))
    
    def draw_categories(self, categories: List[Dict[str, Any]], selected_idx: int):
        """Draw horizontal category menu.
        
        Args:
            categories: List of category dictionaries.
            selected_idx: Index of selected category.
        """
        num_categories = len(categories)
        if num_categories == 0:
            return
        
        # Calculate positions
        center_x = self.width // 2
        center_y = self.height // 2 - 50
        spacing = 200
        
        for i, category in enumerate(categories):
            offset = (i - selected_idx) * spacing
            x = center_x + offset
            y = center_y
            
            # Calculate scale based on distance from center
            distance = abs(i - selected_idx)
            scale = max(0.6, 1.0 - distance * 0.2)
            
            # Draw category icon (placeholder box for now)
            icon_size = int(64 * scale)
            icon_rect = pygame.Rect(x - icon_size // 2, y - icon_size // 2, icon_size, icon_size)
            
            # Color based on selection
            if i == selected_idx:
                color = self.selected_color
            else:
                color = self.text_color
            
            # Draw icon placeholder
            pygame.draw.rect(self.screen, color, icon_rect, 2)
            
            # Draw category name
            font = self.title_font if i == selected_idx else self.item_font
            text = font.render(category["name"], True, color)
            text_rect = text.get_rect(center=(x, y + icon_size // 2 + 30))
            self.screen.blit(text, text_rect)
    
    def draw_items(self, items: List[Dict[str, Any]], selected_idx: int, category_name: str):
        """Draw vertical item menu.
        
        Args:
            items: List of item dictionaries.
            selected_idx: Index of selected item.
            category_name: Name of current category.
        """
        if not items:
            return
        
        # Draw items vertically
        center_x = self.width // 2
        start_y = self.height // 2 + 80
        spacing = 50
        
        for i, item in enumerate(items):
            y = start_y + (i - selected_idx) * spacing
            
            # Skip items too far from view
            if y < 0 or y > self.height:
                continue
            
            # Calculate scale and alpha based on distance
            distance = abs(i - selected_idx)
            scale = max(0.7, 1.0 - distance * 0.15)
            alpha = max(100, 255 - distance * 50)
            
            # Color based on selection
            if i == selected_idx:
                color = (*self.selected_color, 255)
            else:
                color = (*self.text_color, alpha)
            
            # Draw item name
            font = self.item_font if i == selected_idx else self.small_font
            text = font.render(item["name"], True, color[:3])
            text.set_alpha(color[3])
            text_rect = text.get_rect(center=(center_x, y))
            self.screen.blit(text, text_rect)
            
            # Draw selection indicator
            if i == selected_idx:
                indicator_x = center_x - text_rect.width // 2 - 20
                pygame.draw.polygon(self.screen, self.selected_color, [
                    (indicator_x, y),
                    (indicator_x - 10, y - 8),
                    (indicator_x - 10, y + 8)
                ])
    
    def draw_breadcrumb(self, category_name: str, item_name: str = None):
        """Draw breadcrumb navigation.
        
        Args:
            category_name: Current category name.
            item_name: Current item name (optional).
        """
        breadcrumb = category_name
        if item_name:
            breadcrumb += f" > {item_name}"
        
        text = self.small_font.render(breadcrumb, True, self.text_color)
        self.screen.blit(text, (20, 20))
    
    def draw_help(self):
        """Draw help text at bottom of screen."""
        help_text = "← → Navegar | ↑ ↓ Selecionar | Enter Confirmar | ESC Voltar/Sair"
        text = self.small_font.render(help_text, True, self.text_color)
        text_rect = text.get_rect(center=(self.width // 2, self.height - 30))
        self.screen.blit(text, text_rect)
