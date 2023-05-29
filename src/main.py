#
# __main__.py
#

from topoCollection import topoCollect
from graphCreation import graphCreate
from graphEnricher import graphEnrich
from prepareVariation import prepareVariants
from testSensitivity import testSensi
# from prepareSolutionSpace import buildSpace

if __name__ == "__main__":
    
    # topoCollect()
    # graphCreate()
    # graphEnrich()
    prepareVariants(set_dup_rvt=True)
    # testSensi(build_design=True, calc_index=True, plot_index=True)


# to do 
# 1. develop an automated Error/Warning handler.
# 1.1 too hard with Python for an automated handler. 
# 1.2 continue to test with test-handler-paramed.rvt and test-handler.dyn
# -> first conflict nr .38.
# 1.2 [first test] try with activating the workset during the generation
# slightly faster for generation. slower for checking.
# 1.3 [second test] remove windows/doors before the duplication.
# desgin overwrite completed.
# how to automatically save??

# 2. add more advanced locational parameters on doors and windows.
# 2.1 ground floor -> [already succeed.]
# 2.2 upper floors -> [not successful yet.]
# solution 1 - > refer to different grids per floor.
# solution 2 - > find exact aligned dimension command.
