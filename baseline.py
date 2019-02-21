import spacy

from baseline import unpack_spacy_doc
from utils import LoadData


F = '/Users/richard/Documents/gap/utils/data/gap-validation.tsv'


def main():
    nlp = spacy.load('en_coref_lg')
    data_loader = LoadData(F)
    data = data_loader.get_tuples()
    
    for sample in data:
        doc = nlp(sample.text)
        corefs = unpack_spacy_doc(doc)        
        print(doc)
        print(corefs)

if __name__ == '__main__':
    main()
    
