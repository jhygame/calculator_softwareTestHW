from py2cfg import CFGBuilder

cfg = CFGBuilder().build_from_file('example', 'UI.py')
cfg.build_visual('uiCFG', 'pdf')