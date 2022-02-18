import logging

class Logger(object):
    '''日志工具类

    '''
    def __init__(self, log_file_name):
        # 创建一个logger
        self.__logger = logging.getLogger()

        # 指定日志的最低输出级别，默认为WARN级别
        self.__logger.setLevel(logging.INFO)

        # 创建一个handler用于写入日志文件
        file_handler = logging.FileHandler(log_file_name)

        # 创建一个handler用于输出控制台
        console_handler = logging.StreamHandler()

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.__logger.addHandler(file_handler)
        self.__logger.addHandler(console_handler)

    def get_log(self):
        return self.__logger
