
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


dataset =[["milk","onion","nutmeg","kidney beans","eggs"," Yoguert"],
          ["Dill","onion","nutmeg","kidney beans","eggs"," Yoguert"],
          ["milk","Apple","kidney beans","eggs"],
          ["milk","Unicorn","corn","kidney beans","Yoguert"],
          ["corn","onion","onion","kidney beans","eggs"," icecream"],]

print(dataset)

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)

df = pd.DataFrame(te_ary,columns=te.columns_)
print(df)

from mlxtend.frequent_patterns import apriori

ft = apriori(df,min_support=0.6,use_colnames =True)
print(ft)

from mlxtend.frequent_patterns import association_rules

ac = association_rules(ft,metric="confidence",min_threshold =0.7)
print(ac)

ac1 = ac[["antecedents","consequents","support","confidence"]]
print(ac1)


ac2 =ac1[ac1["confidence"]>=1]
print(ac2)