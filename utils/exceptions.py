__all__ = [
    'PredictionsNotSameLengthError',
]


class PredictionsNotSameLengthError(Exception):
    """ Y list and Y_hat list are not the same length"""
    pass

