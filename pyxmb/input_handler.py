"""Input handling for PyXMB."""

import pygame
from typing import Dict, List, Set


class InputHandler:
    """Handles keyboard and gamepad input."""
    
    def __init__(self, controls: Dict[str, List[str]]):
        """Initialize input handler.
        
        Args:
            controls: Dictionary mapping actions to key names.
        """
        self.controls = controls
        self.key_map = self._build_key_map()
        
        # Initialize joystick support
        pygame.joystick.init()
        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.joysticks.append(joystick)
    
    def _build_key_map(self) -> Dict[int, str]:
        """Build mapping from pygame key codes to actions."""
        key_map = {}
        for action, keys in self.controls.items():
            for key_name in keys:
                # Get pygame key constant
                key_code = getattr(pygame, f"K_{key_name}", None)
                if key_code is not None:
                    key_map[key_code] = action
        return key_map
    
    def get_action(self, event: pygame.event.Event) -> str:
        """Get action from event.
        
        Args:
            event: Pygame event.
            
        Returns:
            Action name or None.
        """
        if event.type == pygame.KEYDOWN:
            return self.key_map.get(event.key)
        
        elif event.type == pygame.JOYBUTTONDOWN:
            # Map common gamepad buttons
            if event.button == 0:  # A/Cross button
                return "select"
            elif event.button == 1:  # B/Circle button
                return "back"
        
        elif event.type == pygame.JOYHATMOTION:
            # D-pad motion
            x, y = event.value
            if y == 1:
                return "up"
            elif y == -1:
                return "down"
            elif x == -1:
                return "left"
            elif x == 1:
                return "right"
        
        elif event.type == pygame.JOYAXISMOTION:
            # Analog stick motion (with deadzone)
            deadzone = 0.5
            if abs(event.value) > deadzone:
                if event.axis == 0:  # Left stick horizontal
                    return "right" if event.value > 0 else "left"
                elif event.axis == 1:  # Left stick vertical
                    return "down" if event.value > 0 else "up"
        
        return None
