'''
    glmark: System 3d benchmark
    test: Perf_3d
'''
import os
from runtest import RunTest
from common import *

class DoTest(RunTest):
    def __init__(self, testtoolget, testargs, homepath):
        self.homepath = homepath
        self.tool = testtoolget
        self.args = testargs
    
    def _setup(self):
        '''
         Setup before starting test
         Deepend: gcc make expect gcc-c++
        '''
        RunTest._depend('gcc', 'make', 'gcc-c++', ) 
        srcdir = RunTest._pretesttool('glmarksta', 'GLMarksta.tar.gz', self.tool, self.homepath)
        os.chdir(srcdir)
        self._make('')

    def _runtest(self):
        print "test is %s" % self.args
        argt= self.args["argt"]
        RunTest._dotest("glmark.sh", argt, 1)
