import logging
import logging.config
import yaml

def setup_logging():
    with open('log_config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
