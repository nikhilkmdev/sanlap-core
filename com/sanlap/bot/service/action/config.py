from com.sanlap.bot.service.action.clueless import CluelessBotAction
from com.sanlap.bot.service.action.greet import GreetAction
from com.sanlap.bot.service.action.java import DownloadJavaAction
from com.sanlap.bot.service.action.noop import NoOpAction
from com.sanlap.bot.service.action.thank import ThankAction

ACTION_BY_INTENT = {
    'clueless': CluelessBotAction,
    'download_java': DownloadJavaAction,
    'greet': GreetAction,
    'no_op': NoOpAction,
    'thank': ThankAction,
}
