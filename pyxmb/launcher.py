"""Application launcher for PyXMB."""

import subprocess
import platform
import os
from typing import Dict, Any


class Launcher:
    """Handles launching applications and actions."""
    
    def __init__(self):
        """Initialize launcher."""
        self.system = platform.system()
    
    def launch_item(self, item: Dict[str, Any]) -> bool:
        """Launch an item (application or action).
        
        Args:
            item: Item dictionary with type and action/command.
            
        Returns:
            True if successful, False otherwise.
        """
        item_type = item.get("type", "")
        
        if item_type == "launcher":
            return self._launch_command(item.get("command", ""))
        elif item_type == "action":
            return self._execute_action(item.get("action", ""))
        
        return False
    
    def _launch_command(self, command: str) -> bool:
        """Launch an external command.
        
        Args:
            command: Command to execute.
            
        Returns:
            True if successful, False otherwise.
        """
        if not command:
            return False
        
        try:
            # Parse command (handle shell expansion)
            expanded_command = os.path.expanduser(command)
            
            # Launch in background
            if self.system == "Windows":
                subprocess.Popen(expanded_command, shell=True)
            else:
                # Unix-like systems
                subprocess.Popen(expanded_command, shell=True, 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
            return True
        except Exception as e:
            print(f"Error launching command '{command}': {e}")
            return False
    
    def _execute_action(self, action: str) -> bool:
        """Execute a built-in action.
        
        Args:
            action: Action name.
            
        Returns:
            True if successful, False otherwise.
        """
        if action == "system_info":
            self._show_system_info()
            return True
        elif action == "about":
            self._show_about()
            return True
        
        return False
    
    def _show_system_info(self):
        """Show system information."""
        info = f"""
Sistema: {platform.system()}
Versão: {platform.version()}
Arquitetura: {platform.machine()}
Processador: {platform.processor()}
Python: {platform.python_version()}
"""
        print("=== Informações do Sistema ===")
        print(info)
    
    def _show_about(self):
        """Show about information."""
        about = """
PyXMB - Desktop Launcher
Versão: 0.1.0

Um launcher desktop que emula a experiência XMB
(XrossMediaBar) da PlayStation.

Navegação:
- Setas Esquerda/Direita ou A/D: Trocar categoria
- Setas Cima/Baixo ou W/S: Navegar itens
- Enter ou Espaço: Selecionar
- ESC: Voltar/Sair

Suporte para gamepad incluído!
"""
        print(about)
