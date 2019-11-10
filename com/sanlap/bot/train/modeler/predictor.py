import logging
import os

import joblib

from com.sanlap.bot.train.domain.query import add_model


class Predictor(object):

    def __init__(self, trained_model):
        """
        The wrapper for predicting using generated model by the modeler
        :param trained_model the trained model
        """
        self._model = trained_model

    def predict(self, input_text):
        """
        Predicts the label for the given text input
        :param input_text: the input text to predict
        :return: the label identified
        """
        return self._model.predict([input_text])

    def save(self, model_version, model_name, is_active, path_to_save):
        """ Saves the model to be reused again
        :param model_version the model version
        :param model_name the name of the model
        :param is_active is the model supposed to be active
        :param path_to_save the directory to save the model
        """
        logging.info(f'Save the model to {path_to_save} with the name {model_name}_{model_version}')
        object_name = Predictor._get_object_name(model_name, model_version)
        full_object_path = os.path.join(path_to_save, object_name)
        joblib.dump(self._model, full_object_path)
        add_model(model_name, model_version, full_object_path, is_active=is_active)

    @staticmethod
    def _get_object_name(model_name, model_version):
        return f'{model_name}_{model_version}.joblib'
