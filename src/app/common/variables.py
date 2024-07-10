import os
import yaml

from src.app.common.settings import ROOT_DIR, Settings

settings = Settings()  # get_settings()


LOG_CONF_FILE = f"resources/config/log/{settings.env}.yaml"

with open(os.path.join(ROOT_DIR, LOG_CONF_FILE), "r") as log:
    config_log = yaml.load(log, Loader=yaml.FullLoader)

# LOG SETTINGS
if settings.is_test:
    log_dir = os.path.join(ROOT_DIR, "logs")
    os.makedirs(log_dir, exist_ok=True)

    filename = config_log['handlers']['logfile']['filename']
    config_log['handlers']['logfile']['filename'] = os.path.join(log_dir, filename)


# LOG SETTINGS
if settings.is_test:
    LOG_DIR = os.path.join(ROOT_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)

    filename = config_log['handlers']['logfile']['filename']
    config_log['handlers']['logfile']['filename'] = os.path.join(LOG_DIR, filename)

