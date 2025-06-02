import logging
import os
import datetime

def get_log_file_path(base_dir: str, prefix: str = "log") -> str:
    """
    Generate a log file path based on the current date and a base directory.

    Args:
        base_dir (str): The base directory where the log file will be stored.
        prefix (str): The prefix for the log file name (default is "log").

    Returns:
        str: Full path to the log file.
    """
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    return os.path.join(base_dir, f"{prefix}_{date_str}.log")

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with the specified name and logging level.

    Args:
        name (str): The name of the logger.
        level (int): The logging level (default is logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger

if __name__ == "__main__":
    # Example usage
    log_file_path = get_log_file_path("logs")
    logger = setup_logger("example_logger")
    logger.info(f"Log file will be stored at: {log_file_path}")
    logger.info("This is an info message.")
    logger.error("This is an error message.")