from com.sanlap.bot.service.action.base import BaseAction

THANKS_RESPONSES = [
    'You are welcome!',
    'Awesome. Have a great day!',
    'Glad to help.',
]


class ThankAction(BaseAction):
    def intent(self):
        return 'thank'

    def user_inputs_needed(self):
        return list()

    def perform_action(self, **kwargs):
        return
