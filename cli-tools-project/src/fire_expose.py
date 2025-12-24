#!/usr/bin/env python3
"""
CLI tool using Python Fire library.
Exposes utility functions (greet, goodbye) via command line interface.
"""

import fire
from utils import greet, goodbye


class CLITools:
    """Collection of CLI tools exposed via Fire."""
    
    def greet(self, name):
        """
        Greet a person by name.
        
        Usage:
            python fire_expose.py greet Alice
        """
        return greet(name)
    
    def goodbye(self, name):
        """
        Say goodbye to a person by name.
        
        Usage:
            python fire_expose.py goodbye Bob
        """
        return goodbye(name)


if __name__ == "__main__":
    fire.Fire(CLITools)