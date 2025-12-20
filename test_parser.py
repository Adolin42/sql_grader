#!/usr/bin/env python3
"""Test script to verify config_parser.py works correctly"""

from config_parser import load_config

# Test loading the config
config = load_config("test_config.json")

print("\N{CHECK MARK} Config loaded successfully!")
print(f"\nDatabase: {config['database']['database']}")
print(f"Modules: {len(config['modules'])}")
for module in config['modules']:
    print(f"  - {module['name']}: {len(module['tests'])} tests")
