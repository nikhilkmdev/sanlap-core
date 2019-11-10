from com.sanlap.bot.service.action.base import BaseAction


class NoOpAction(BaseAction):

    def intent(self):
        return 'noop'

    def user_inputs_needed(self):
        return list()

    def perform_action(self, **kwargs):
        return ''
