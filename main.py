# This is a sample Python script.
from pyserini.search.lucene import LuceneSearcher
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.

def bm25(dataset_name, question):
    search = LuceneSearcher.from_prebuilt_index(dataset_name)
    hits = search.search(question,k=20)

    for i in range(0,20):
        print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f}')
    return hits

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LuceneSearcher.list_prebuilt_indexes()
    #docs = bm25('msmarco-v1-passage', 'Brazil')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
