import pandas as pd

from .types import Sample

__all__ = [
    'LoadData',
]


class LoadData(object):
    def __init__(self, path):
        self.path = path
    
    def get_dataframe(self):
        """ Returns a panda dataframe.

        Returns: pd.DataFrame

        """

        return pd.read_csv(self.path, delimiter='\t')

    def get_tuples(self):
        """ Returns a list of Sample data types.

        Returns: List[Sample]

        """

        df = self.get_dataframe()
        df = df.where((pd.notnull(df)), None)
        data_list = []
        for _, row in df.iterrows():
            sample_dict = row.to_dict()
            sample_dict = {k.lower().replace('-', '_'): v for k, v 
                    in sample_dict.items()}
            data_list.append(Sample(**sample_dict))
        
        return data_list


