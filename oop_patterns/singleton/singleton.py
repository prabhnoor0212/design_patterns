class LoggerSingleton:
    _logger_instance = None

    def __init__(self):
        raise RuntimeError('Call create() instead')

    @classmethod
    def create(cls):
        if cls._logger_instance is None:
             cls._logger_instance = cls.__new__(cls)
        return cls._logger_instance
