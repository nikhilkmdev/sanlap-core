from com.sanlap.bot.service.action.clueless import CluelessBotAction
from com.sanlap.bot.service.action.java import DownloadJavaAction

ACTION_BY_INTENT = {
    'clueless': CluelessBotAction,
    'java': DownloadJavaAction,
}
