from collections import namedtuple

__all__ = [
    'Sample',
    'PredictedClass',
]


class Sample(namedtuple(
    'Sample', 
    [
        'id', 
        'text', 
        'pronoun', 
        'pronoun_offset', 
        'a', 
        'a_offset', 
        'a_coref', 
        'b', 
        'b_offset', 
        'b_coref', 
        'url'
    ])):
    """ A wrapper for the raw input data (training and validation set). The
    data source is located at: 
        https://github.com/google-research-datasets/gap-coreference

    Args:
        id (str):
        text (str):
        pronoun (str):
        pronoun_offset (int):
        a (str):
        a_offset (int):
        a_coref (bool):
        b (str):
        b_offset (int):
        b_coref (bool):
        url (str):

    """
    pass

class PredictedClass(namedtuple(
    'PredictedClass',
    [
        'index',
        'label',
        'predicted_label',
        'outcome',
    ])):
    """ A tuple for evaluating model performance. Wraps a model predicition with
    its true label and other meta data.

    Args:
        index (int): The index of the text from which the prediction is
            associated with.
        label (int): The ground truth class of the input text.
        predicted_label (int): The predicted class from the model. The 
            class should be a hard assignment.
        outcome (str): Acronym for the evaluated prediction ie. TP, TN, FP, FN.

    """
    pass

