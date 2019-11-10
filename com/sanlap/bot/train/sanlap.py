import argparse
import logging

import yaml

from com.sanlap.bot.train.data.config import DATA_PIPE_BY_NAME
from com.sanlap.bot.train.modeler.modeler import Trainer


class Runner(object):

    def __init__(self, config_path):
        """
        Runs the framework to build and save the model
        :param config_path: the path to the YAML configuration file
        """
        self._initialize_config(config_path)

    def _initialize_config(self, config_path):
        with open(config_path, 'r') as config_file:
            self._config = yaml.load(config_file)
        logging.info(f'Successfully loaded configuration from {config_file}')

    def run(self):
        """ Entry point to the framework """
        for model_config in self._config:
            model_name = model_config['name']
            model_version = model_config['version']
            is_model_active = model_config['activate']
            logging.info(f'Starting model creation for {model_name}:{model_version}, is active? {is_model_active}')
            # Data phase
            data_config = model_config['data']
            data, labels = Runner._start_data_sourcing(data_config)
            # Train
            train_config = model_config['train']
            train_test_split_ratio = data_config['train_test_split_ratio']
            predictor = Runner._start_training(train_config, data, labels, train_test_split_ratio)
            # Persist
            path_to_save = model_config['predict']['path']
            predictor.save(model_version, model_name, is_model_active, path_to_save)

    @staticmethod
    def _start_data_sourcing(data_config):
        pipe_config = data_config['pipe']
        data_meta = data_config['meta']
        pipe_source = pipe_config['source']
        pipe_args = pipe_config['args']
        pipe_args['source'] = pipe_source
        pipe_args['data_column'] = data_meta['feature']
        pipe_args['label_columns'] = data_meta['label']
        data_pipe = DATA_PIPE_BY_NAME[pipe_source]
        data_pipe = data_pipe(**pipe_args)
        return data_pipe.get_cleaned_data()

    @staticmethod
    def _start_training(train_config, data, labels, train_test_split_ratio):
        classifier_name = train_config['model']['name']
        trainer = Trainer(classifier_name, train_test_split_ratio=train_test_split_ratio)
        predictor = trainer.train(data, labels)
        return predictor


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-config', help='The configuration file to be used to generate the model')
    args = arg_parser.parse_args()
    logging.info(f'Parsing the config file provided {args.config}')
    runner = Runner(args.config)
    runner.run()


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    logging.info('Starting the process to train a chat bot for you.')
    main()
