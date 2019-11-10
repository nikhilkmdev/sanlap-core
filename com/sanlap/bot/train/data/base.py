import abc
import enum
import logging


class Source(enum.Enum):
    LOCAL_FILE = 'local'


class BasePipe(object):

    def __init__(self, source, data_column, label_columns):
        """
        The base pipe for all the sources we would get the corpus from
        :param source: the name of the source pipe
        :param data_column: the column consisting of the data
        :param label_columns: the columns consisting of the classifications/labels
        """
        self._source = source
        self._data_column = data_column
        self._label_columns = label_columns

    def get_cleaned_data(self):
        """
        Gets data cleaned up with obvious necessities
        :return: cleaned data as a tuple of pandas data frame, with data and label columns
        """
        data = self._get_data()
        logging.info(f'Received data frame. Num of rows: {len(data)}')
        data = self._clean_data(data)
        logging.info(f'Cleaning data frame completed. Num of rows: {len(data)}')
        labels = data[self._label_columns]
        data = data[self._data_column]
        return data, labels

    @abc.abstractmethod
    def _get_data(self):
        """
        Gets the data from a relevant source
        :return: a data frame consisting of the training data
        """

    def _clean_data(self, data):
        logging.info(f'Number of null found in data sourced {data.isnull().sum()}')
        data.dropna(inplace=True)
        logging.info(f'Removing {self._data_column} rows with empty strings')
        # data = data[not data[self._data_column].isspace()]
        return data
