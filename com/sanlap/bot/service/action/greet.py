import random

from com.sanlap.bot.service.action.base import BaseAction

GREET_MESSAGES = [
    'How can I help?',
    'How can I help you today?',
    'Hello. How can I help you today?',
    'Yo! How can I help you today?',
]


class GreetAction(BaseAction):

    def intent(self):
        return 'greet'

    def user_inputs_needed(self):
        return list()

    def perform_action(self, **kwargs):
        return GREET_MESSAGES[random.randint(0, len(GREET_MESSAGES))]
