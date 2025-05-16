import logging

def setup_logging():
    """
    Configure application logging
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    
    # Return logger for main module
    return logging.getLogger("main")