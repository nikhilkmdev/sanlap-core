from com.sanlap.bot.service.action.base import BaseAction


class DownloadJavaAction(BaseAction):

    def __init__(self):
        super(DownloadJavaAction, self).__init__()
        self._download_url_by_version = {
            '8': 'http://download.java.com/version=1.8',
            '1.8': 'http://download.java.com/version=1.8',
            '11': 'http://download.java.com/version=11',
        }

    def intent(self):
        return 'java'

    def user_inputs_needed(self):
        return ['version']

    def perform_action(self, version=None):
        download_url = self._download_url_by_version.get(version)
        if download_url:
            response = f'You can download Java from URL - {download_url}'
        else:
            response = f'Sorry. I do not have all the information with me to help you. Can I help with any other thing?'
        return response
