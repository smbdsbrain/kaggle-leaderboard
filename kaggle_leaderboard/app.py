import pathlib

import aioworkers_aiohttp.app
from kaggle.api_client import ApiClient
from kaggle.configuration import Configuration
from kaggle.api.kaggle_api_extended import KaggleApi


class NoAuthKaggleApi(KaggleApi):
    api_client = None

    def authenticate(self):
        pass


class Application(aioworkers_aiohttp.app.Application):
    def __init__(self, config, *, context, **kwargs):
        super(Application, self).__init__(config, debug=config.debug, context=context, **kwargs)

        main_html = pathlib.Path(__file__).parent / 'templates' / 'main.html'
        self.main_html = main_html.read_text(encoding='utf-8')

        configuration = Configuration()
        configuration.username = self.context.config.kaggle.user
        configuration.password = self.context.config.kaggle.key
        self.api_client = ApiClient(configuration)

        self.kaggle_api = NoAuthKaggleApi(self.api_client)

