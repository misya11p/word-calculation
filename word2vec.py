import pandas as pd
import re
from gensim.models import KeyedVectors

model = KeyedVectors.load('keyword.kv', mmap='r')

def word_calculation(add, subtract, n, df=True):
    add = re.sub('\s+', '', add).split(',') if add else []
    subtract = re.sub('\s+', '', subtract).split(',') if subtract else []
    try:
        result = model.most_similar(positive=add, negative=subtract, topn=n)
    except Exception as e:
        return e
    if df:
        df = pd.DataFrame(result, columns=['単語', 'cos類似度'])
        return df.set_index('単語')
    else:
        return result