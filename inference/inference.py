from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-r", "--retrievers",
                        type=list,
                        nargs="+",
                        default=["BM25"],
                        help="list of retrievers",
                        required=True)
    parser.add_argument("-n", "--num_results",
                        type=int,
                        default=5,
                        help="number of documents retrieved during inference",
                        required=False)
    
    args = parser.parse_args()

    retrievers = None