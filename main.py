from utils import LoadData

data_path = './utils/data/gap-development.tsv'


def main():
    samples = LoadData(data_path).get_tuples()

    print(samples)
    
if __name__ == '__main__':
    main()
