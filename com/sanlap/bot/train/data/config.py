from com.sanlap.bot.train.data.base import Source
from com.sanlap.bot.train.data.local_file import DelimitedLocalFilePipe

DATA_PIPE_BY_NAME = {
    Source.LOCAL_FILE.value: DelimitedLocalFilePipe,
}
