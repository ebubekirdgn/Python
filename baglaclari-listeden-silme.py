
baglaclar=['açıkçası','ama','ancak','bile','oysa','oysaki','öyleyse','üstelik','ve','veya','veyahut','yahut','yalnız','hatta','yine','yoksa','zira','ile','hâlbuki']
kelimeler = ['ve','veya','Karpuz','Karpuz','Karpuz','Elma','hatta','ile','hâlbuki']
 
 
def func(words, conjunctions):
    res = []
    for word in words:
        if word not in conjunctions:
            res.append(word)
    return res

print(func(kelimeler, baglaclar))