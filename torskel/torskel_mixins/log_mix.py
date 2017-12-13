
import tornado.log

LOG_MSG_DEBUG_TMPL = '%s %s'


class TorskelLogMixin(object):

    def __init__(self):
        self.logger = tornado.log.gen_log
        self.log_msg_tmpl = LOG_MSG_DEBUG_TMPL

    # ################### #
    #  Logging functions  #
    # ################### #

    def get_log_msg(self, msg, grep_label=''):
        """
        Make message by template
        :param msg: message
        :param grep_label: label for grep
        :return: compiled message
        """
        try:
            res = self.log_msg_tmpl % (grep_label, msg)
        except:
            res = msg
        return res

    def log_debug(self, msg, grep_label=''):
        """
        Log debug message
        :param msg: message
        :param grep_label: label for grep
        :return:
        """
        self.logger.debug(self.get_log_msg(msg, grep_label))

    def log_err(self, msg, grep_label=''):
        """
        Log error
        :param msg: message
        :param grep_label: label for grep
        :return:
        """
        self.logger.error(self.get_log_msg(msg, grep_label))

    def log_exc(self, msg, grep_label=''):
        """
        Log exception
        :param msg: message
        :param grep_label: label for grep
        :return:
        """
        self.logger.exception(self.get_log_msg(msg, grep_label))