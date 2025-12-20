import json
import sys

def load_config(config_path):
    """
    Load and validate the grading config file.
    
    Args:
        config_path (str): Path to config JSON file
        
    Returns: 
        dict: Validated config directory
    
    Raises: 
        SystemExit: If config is invalid
    """
    
    # Step 1: Read the JSON file
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file '{config_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{config_path}': {e}")
        sys.exit(1)
        
    # Step 2: Validate the config structure
    validate_config(config)
    
    return config



def validate_config(config):
    """
    Validate that the config has all required fields and correct structure.
    
    Args:
        config (dict): The config directory to validatek
        
    Raises:
        SystemExit: If config is invalid
    """
    
    # Check top-level keys
    if "database" not in config:
        print("Error: Missing 'database' key in config.")
        sys.exit(1)
        
    if "modules" not in config:
        print("Error: Missing 'modules' key in config.")
        sys.exit(1)
        
    # Validate database section
    database = config["database"]
    required_db_fields = ["host", "user", "password", "database"]
    
    for field in required_db_fields:
        if field not in database:
            print(f"Error: Missing 'database.{field}' in config")
            sys.exit(1)
            
    # Validate modules section
    modules = config["modules"]
    
    if not isinstance(modules, list) or len(modules) == 0:
        print("Error: 'modules' must be non-empty list.")
        sys.exit(1)
        
    test_ids = []
    
    for module_idx, module in enumerate(modules):
        # Check module has required fields
        if "name" not in module:
            print(f"Error: Module at index {module_idx} is missing 'name' field.")
            sys.exit(1)
            
        if "tests" not in module:
            print(f"Error: Module '{module['name']}' is missing 'tests' field.")
            sys.exit(1)
            
        tests = module["tests"]
        
        if not isinstance(tests, list) or len(tests) == 0:
            print(f"Error: Module '{module['name']}' must have a non-empty 'tests' list.")
            sys.exit(1)
            
        # Check each test has required fields
        for test_idx, test in enumerate(tests):
            required_test_fields = ["id", "name", "description", "expected_output_file"]
            
            for field in required_test_fields:
                if field not in test:
                    print(f"Error: Test at module '{module['name']}', test index {test_idx} is missing '{field}' field.")
                    sys.exit(1)
                    
            test_ids.append(test["id"])
            
        # Check for duplicate test IDs
        if len(test_ids) != len(set(test_ids)):
            duplicates = [id for id in test_ids if test_ids.count(id) > 1]
            print(f"Error: Duplicate test IDs found: {duplicates}")
            sys.exit(1)
            
        print("\N{CHECK MARK} Config validation passed.")

