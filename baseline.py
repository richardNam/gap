import argparse
import spacy

from baseline import unpack_spacy_doc
from utils import LoadData
from utils import logger


def main(args):
    nlp = spacy.load('en_coref_lg')
    data_loader = LoadData(args.file)
    data = data_loader.get_tuples()
    
    for sample in data:
        doc = nlp(sample.text)
        corefs = unpack_spacy_doc(doc)        
        if args.verbose:
            logger.info(corefs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Coreference Baseline')
    parser.add_argument('-f', dest='file', type=str,
        default='/home/richard/documents/gap/utils/data/gap-validation.tsv',
        help='The path to the gap-validation/tsv')
    parser.add_argument('-v', dest='verbose', action='store_true',
        help='Turn of verbose logging')


    args = parser.parse_args()
    main(args)
    
