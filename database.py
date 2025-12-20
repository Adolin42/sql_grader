import pymysql
from pymysql.cursors import DictCursor

class DatabaseConnection:
    """Handle MySQL database connections and query execution."""
    
    def __init__(self, host, user, password, database):
        """
        Initialize a database connection
        
        Args:
            host (str): MySQL server hostname
            user (str): MySQL username
            password (str): MySQL password
            database (str): Database name
            
        Raises:
            pymysql.Error: If connection fails
        """
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset='utf8mb4',
                cursorclass=DictCursor
            )
        except pymysql.Error as e:
            raise Exception(f"Failed to connect to database: {e}")
    
    def execute_query(self, query):
        """
        Execute a SQL query and return results as a list of dicts.
        
        Args:
            query (str): SQL query to execute
            
        Returns:
            list: List of dicts, where each dict is a row
            
        Raises:
            Exception: If query execution fails
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                # Fetch all results as list of dicts
                results = cursor.fetchall()
            return results
        except pymysql.Error as e:
            raise Exception(f"Query execution failed: {e}")
    
    def close(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - ensures connection is closed."""
        self.close()