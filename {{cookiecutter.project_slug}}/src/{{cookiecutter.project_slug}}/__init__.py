"""Top-level package for {{ cookiecutter.project_name }}."""
import logging
import pathlib

from .config import configure_logger

# configure logging
logger = logging.getLogger(__name__)
configure_logger(logger)

logger.info(f'Logger initialized for the {__name__} package')

# default dir locations
SCRIPTS_DIR = pathlib.Path(__file__).parents[2] / 'scripts'
DATA_DIR = pathlib.Path(__file__).parents[2] / 'data'

# check they exist
DIRS = (SCRIPTS_DIR, DATA_DIR)
missing_dirs = [d for d in DIRS if not d.exists()]
if missing_dirs:
    logger.warning(f'Missing the following dirs: {missing_dirs}')