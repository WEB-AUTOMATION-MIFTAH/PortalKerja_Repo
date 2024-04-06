import datetime
from _pytest.config import Config

def pytest_configure(config: Config):
    config.html_report_title = f"Report generated on {datetime.datetime.now() + datetime.timedelta(hours=7):%d-%b-%Y at %H:%M:%S} (UTC+7) by pytest-html {config.pluginmanager.get_plugin('pytest-html').version}"
