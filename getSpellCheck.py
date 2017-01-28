import pandas as pd
import numpy as np
from utils import *

def spell_check_score(df,col):
        """
        We further use a spell-checker to identify misspelled 
        words in the request text [10]. In other contexts 
        (e.g. Kickstarter), spelling errors have been found to
        have a negative impact on funding success.
        
        Input is the column of request.
        Returns a list of spelling check score for each
        request
        """
        spell_errors,i = [],1
        for text in df[col]:
            print '{} requests parsed....'.format(i)
            pd.Series(spell_errors).to_csv('spellCheck.csv')
            print 'Saved to spellCheck.csv'
            i += 1
            spl_err = 0
            words = re.sub("["+'!"#$%&\'()*+.,-/:;<=>?@[\\]^_`{|}~'+"]", " ", text).split()
            if len(words):
                for word in words:
                    if word.startswith('@'):
                        continue
                    if correction(word)!= word: 
                        spl_err += 1
                spell_errors.append(float(spl_err)/len(words))
            else:
                spell_errors.append(0)
        return spell_errors
    
df_train = pd.read_csv('Data/training_set_rel3.tsv',delimiter='\t')
print df_train.shape

spell_check = spell_check_score(df_train,'essay')
pd.Series(spell_check).to_csv('spellCheck.csv')