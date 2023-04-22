import yaml
import time

from src.telegram.bot import TelegramClient
from src.postgres import connect
from yaml.loader import SafeLoader



if __name__ == "__main__":
    configurations = yaml.load(open('assets/configurations/run_configs.yml'), Loader=SafeLoader)
    time.sleep(1)
    connect(configurations)

    botObj = TelegramClient()
    botObj.run()
