from py2cfg import CFGBuilder

cfg = CFGBuilder().build_from_file('example', 'calculate.py')
cfg.build_visual('calculateCFG', 'pdf')