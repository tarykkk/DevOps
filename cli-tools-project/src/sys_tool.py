#!/usr/bin/env python3
"""
CLI tool using sys.argv for command line argument parsing.
Prints 'командна строка' only when run directly from CLI.
"""

import sys


def main():
    """Main function that prints when script is run directly."""
    # Check for --help flag
    if len(sys.argv) > 1 and sys.argv[1] in ('--help', '-h'):
        print("Usage: python sys_tool.py [--help]")
        print("Prints 'командна строка' when run directly from CLI.")
        print("\\nOptions:")
        print("  --help, -h  Show this help message")
        return
    
    # Print the required message
    print("командна строка")


if __name__ == "__main__":
    # This block only executes when script is run directly
    main()