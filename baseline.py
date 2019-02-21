import spacy

from utils import LoadData

def main():
    nlp = spacy.load('en_coref_lg')
    data_loader = LoadData('/Users/richard/Documents/gap/utils/data/gap-validation.tsv')
    data = data_loader.get_tuples()
    sample_idx = 0
    for sample in data:
        doc = nlp(sample.text)
        print(sample_idx)
        print(sample_idx, doc._.has_coref)
        print(sample_idx, doc._.coref_clusters)

        sample_idx += 1

if __name__ == '__main__':
    main()

