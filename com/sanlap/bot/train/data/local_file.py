import pandas

from com.sanlap.bot.train.data.base import BasePipe, Source


class DelimitedLocalFilePipe(BasePipe):

    def __init__(
            self,
            file_path,
            delimiter=',',
            source=Source.LOCAL_FILE,
            data_column=None,
            label_columns=None,
    ):
        """
        Can be used to load the data from a local file which is delimited is a known format
        :param file_path: the path of the file
        :param delimiter: the delimiter separating the data in file content, defaults to ','
        :param source: the name of the source pipe
        :param data_column: the column consisting of the data
        :param label_columns: the columns consisting of the classifications/labels
        """
        super(DelimitedLocalFilePipe, self).__init__(
            source=source,
            data_column=data_column,
            label_columns=label_columns,
        )
        self._file_path = file_path
        self._delimiter = delimiter

    def _get_data(self):
        """ Gets the data from a local file with delimited content

        :return data: pandas.DataFrame instance with data from the file
        """
        return pandas.read_csv(self._file_path, delimiter=self._delimiter)
