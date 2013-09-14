def count(word):
    vogais = u'aeiouãâáàêéíóõôúÃÁÉÍÓÕÔÊÂÚ'
    ditongos = u'ia ua uo ai ei oi ou ae au ao éi ei ui oi ói ou ãi ãe ão iu eu õe ui'.split()
    v = sum((word.count(s) for s in vogais))
    d = sum((word.count(s) for s in ditongos))
    return v-d
