import abc
import logging
import random

ASK_USER_INPUT_QUESTS_TEMPLATE = [
    "Can you please provide '{user_input}'?",
    "Can you give me the value for '{user_input}' that you are looking for?",
    "I would need '{user_input}' to help you with that.",
]


class BaseAction(object):

    def __init__(self):
        self._user_inputs = {}
        self._cur_user_input = None

    def is_ready_to_execute(self):
        """
        Checks if the action is ready to be performed
        :return: true if it is, false otherwise
        """
        is_ready_to_execute = len(self.user_inputs_needed()) == len(self._user_inputs)
        self._cur_user_input = None if is_ready_to_execute else self._cur_user_input
        logging.info(f'Is action ready to execute? {is_ready_to_execute}')
        return is_ready_to_execute

    def is_in_ask_session(self):
        """
        Checks if we hve asked for user inputs
        :return: true if it is, false otherwise
        """
        logging.info(f'Are we in the session of asking for user inputs? {bool(self._cur_user_input)}')
        return bool(self._cur_user_input)

    def ask_for_user_input(self):
        """
        Asks the user for the necessary inputs for performing the task
        :return: a question asking for an input
        """
        ask_response = None
        for user_input in self.user_inputs_needed():
            if user_input not in self._user_inputs:
                quest_index = random.randint(0, len(ASK_USER_INPUT_QUESTS_TEMPLATE) - 1)
                ask_response = ASK_USER_INPUT_QUESTS_TEMPLATE[quest_index]
                ask_response = ask_response.format(user_input=user_input)
                self._cur_user_input = user_input
        return ask_response

    @abc.abstractmethod
    def intent(self):
        """
        The intent to which the action is attached to
        :return: the intent for the action
        """

    def start(self):
        """ Starts the action execution """
        logging.info(f'Starting the perform action - {str(self)}')
        action_response = self.perform_action(**self._user_inputs)
        self._cur_user_input = None
        return action_response

    @abc.abstractmethod
    def user_inputs_needed(self):
        """
        List of user inputs which would be needed for the action
        :return: list of user inputs
        """

    @abc.abstractmethod
    def perform_action(self, **kwargs):
        """
        Logic to perform the action
        :param kwargs: the keyword arguments needed
        :return: human friendly response once the action is done, None otherwise
        """

    def update_user_input(self, user_input):
        """ Updates the user input for the currently requested """
        self._user_inputs.update({self._cur_user_input: user_input})

    def __str__(self):
        return f'{self.__module__} - Intent [{self.intent()}]'
