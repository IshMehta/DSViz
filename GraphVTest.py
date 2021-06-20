from DSViz.GraphV import GraphV

# test = GraphV(Directed=True)
# test.add('run', 'intr')
# test.add('intr', 'runbl')
# test.add('runbl', 'run')
# test.add('run', 'kernel')
# test.add('kernel', 'zombie')
# test.add('kernel', 'sleep')
# test.add('kernel', 'runmem')
# test.add('sleep', 'swap')
# test.add('swap', 'runswap')
# test.add('runswap', 'new')
# test.add('runswap', 'runmem')
# test.add('new', 'runmem')
# test.add('sleep', 'runmem')
# test.add('sleep',  "sleep")
# test.show

# test2 = GraphV()
# test2.add('new', ['runswap', 'runmem'])
# test2.add('runswap', ['runmem', 'new', 'swap'])
# test2.show

# test = GraphV()
# test.add('new', 'runmem')
# test.add('new',['runsawp'])
# test.add('runmem', 'runswap')
# test.add('runmem', ['sleep', 'kernel'])
# test.add('swap', ['sleep', 'runswap'])
# test.add('sleep','kernel')
# test.add('run',['kernel', 'runbl','intr'])
# test.add('runbl', 'intr')
# test.show