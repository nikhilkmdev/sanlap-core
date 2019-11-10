import itertools
import logging

import pandas
import sklearn.feature_extraction.text
import sklearn.metrics
import sklearn.pipeline
import sklearn.svm

from com.sanlap.bot.train.modeler.predictor import Predictor

MODEL_BY_CLASSIFIER = {
    'svc': sklearn.svm.LinearSVC,
    'svm': sklearn.svm.LinearSVC,
}


class Trainer(object):

    def __init__(self, classifier, train_test_split_ratio=0.25):
        """
        Responsible for training a model
        :param classifier: the classifier to be used
        :param train_test_split_ratio: ratio in which we want to slit the data for training and testing
        """
        self._classifier = MODEL_BY_CLASSIFIER[classifier]
        self._train_test_split_ratio = train_test_split_ratio

    def train(self, data, labels):
        """
        Holds the business logic for training the relevant model for the given data
        :param data: instance of the pandas data frame from the pipe
        :param labels: the labels to be used for classification
        :return: a predictor instance
        """
        return self._get_model(data, labels)

    def _get_model(self, data, labels):
        logging.info(f'Splitting the data for training and testing. Split at ratio: {self._train_test_split_ratio}')
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            data,
            labels,
            test_size=self._train_test_split_ratio,
        )
        model = sklearn.pipeline.Pipeline([
            ('tfidf', sklearn.feature_extraction.text.TfidfVectorizer()),
            ('clf', self._classifier()),
        ])
        model.fit(x_train, y_train)
        Trainer._compute_model_stats(model, x_test, y_test, set(itertools.chain.from_iterable(labels.values)))
        return Predictor(model)

    @staticmethod
    def _compute_model_stats(model, x_test, y_test, label_values):
        predictions = model.predict(x_test)
        logging.debug('Confusion Metrics:')
        confusion_metrics = pandas.DataFrame(sklearn.metrics.confusion_matrix(y_test, predictions))
        logging.debug(f'{confusion_metrics}')
        logging.debug('Classification Report:')
        logging.debug(f'{sklearn.metrics.classification_report(y_test, predictions)}')
        logging.debug('Accuracy Score:')
        logging.debug(f'{sklearn.metrics.accuracy_score(y_test, predictions)}')
