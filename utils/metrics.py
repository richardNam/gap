import numpy as np

from .exceptions import PredictionsNotSameLengthError
from .types import PredictedClass


__all__ = [
    'Score',
]

class Score(object):
    def __init__(self, y, yhat):
        """ Create an object with ground truth labels and predicted classes.
        
        Args:
            y List[int]: List of ground truth labels.
            yhat List[int]: List of predicted labels.

        """
        self.y = np.array(y)
        self.yhat = np.array(yhat)

        if self.y.shape[0] != self.yhat.shape[0]:
            raise PredictionsNotSameLengthError()

        self.predictions = self.create_predictions(self.y, self.yhat)
        self.counter = self.get_counts()

    def create_predictions(y, yhat, target_class=None):
        """ Creates a list of PredictedClass data types.

        Args:
            y List[int]: List of ground truth labels.
            yhat List[int]: List of predicted labels.
            target_class (int): the target class that should be
                considered a positive. Default 1, useful when you want
                to compute the p/r/f1 in a multiclass problem.

        Returns: List[types.PredictedClass]

        """
        if target_class is None:
            target_class = 1
        evaluation = self.y == self.yhat
        total = []
        for i in range(evaluation.shape[0]):
            if evaluation[i]:
                if self.yhat == target_class:
                    outcome = 'tp'
                else:
                    outcome = 'tn'
            else:
                if self.yhat == target_class:
                    outcome = 'fp'
                else:
                    outcome = 'fn'

            total.append(
                PredictedClass(
                    index=i,
                    label=self.y[i],
                    predicted_label=self.yhat[i]
                    outcome=outcome
                )
            )
        
        return total

    def get_counts(self):
        counter = {'tp': 0., 'tn': 0., 'fp': 0., 'fn': 0.}
        for prediction in self.predictions:
            counter[prediction.outcome] += 1
        
        return counter

    def recall_score(self):
        return self.counter.get('tp') / (self.counter.get('tp') + \
                self.counter.get('fn'))

    def precision_score(self):
        return self.counter.get('tp') / (self.counter.get('tp') + \
                self.counter.get('tn'))

    def fbeta_score(self, beta=1): 
        numerator = self.precision_score() * self.recall_score()
        denominator = self.precision_score() + self.recall_score()

        return (1.0 + beta) * (numerator / denominator)

    def f1_score(self):
        return self.fbeta_score()

