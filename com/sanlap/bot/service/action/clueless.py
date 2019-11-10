from com.sanlap.bot.service.action.base import BaseAction


class CluelessBotAction(BaseAction):

    def intent(self):
        return 'clueless'

    def user_inputs_needed(self):
        # Nothing to be input from user
        return list()

    def perform_action(self, **kwargs):
        return '''I have no clue about this. But I am learning and hope to have the skill soon.
        You can help me learn. Would you mind reaching out to my creators?
        '''
