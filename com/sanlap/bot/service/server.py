import argparse
import socket
import sys

import joblib
import yaml

from com.sanlap.bot.service.action.config import ACTION_BY_INTENT
from com.sanlap.bot.train.domain.query import get_model_by_name
from com.sanlap.bot.train.modeler.predictor import Predictor

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)


class SanlapService(object):

    def __init__(self, config_path):
        self._predictor = None
        self._connections = {}
        self._action_by_address = {}
        self._init_config(config_path)
        self._init_predictor()

    def start_receive(self):
        """ Starts the service """
        self._connect()
        self._poll()

    @staticmethod
    def _greet_user(connection):
        connection.sendall('Hi. How can I help you today?'.encode('utf-8'))

    def _on_data_received(self, connection, address, data):
        action = self._action_by_address.get(address)
        data = data.decode('utf-8')
        if not action:
            intent = self._predict_intent(data)[0]
            intent = intent or 'clueless'
            action = ACTION_BY_INTENT[intent]
            action = action()
            self._action_by_address[address] = action
        if action.is_in_ask_session():
            action.update_user_input(data)
        if action.is_ready_to_execute():
            response = action.start()
            connection.sendall(str(f'{response}').encode('utf-8'))
        else:
            ask_response = action.ask_for_user_input()
            connection.sendall(str(f'{ask_response}').encode('utf-8'))

    def _predict_intent(self, data):
        return self._predictor.predict(str(data))

    def _init_config(self, config_path):
        with open(config_path, 'r') as config_file:
            self._config = yaml.load(config_file)

    def _init_predictor(self):
        model_path = get_model_by_name('FirstModel', version=0.2, is_active=True)
        model = joblib.load(model_path)
        self._predictor = Predictor(model)

    def _connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, self._config['server']['port']))
            s.listen()
            connection, address = s.accept()
            self._connections[address] = connection
            SanlapService._greet_user(connection)

    def _poll(self):
        print(f'Connected to {len(self._connections)} clients')
        while True:
            for address, connection in self._connections.items():
                # with connection:
                print('Connected by', address)
                data = connection.recv(1024)
                self._on_data_received(connection, address, data)


if __name__ == '__main__':
    server_config_path = sys.argv[1]
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-config', help='The configuration file to be used to configure the service')
    args = arg_parser.parse_args()
    sanlap_service = SanlapService(args.config)
    sanlap_service.start_receive()