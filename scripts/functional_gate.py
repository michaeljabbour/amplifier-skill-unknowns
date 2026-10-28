#!/usr/bin/env python3
"""Meaningful local functional checks; no provider calls or production activation."""
import asyncio
import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

class Gate(unittest.TestCase):
    def test_installed_map_survives_add_and_triage_without_engine(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'map.dot';base=[sys.executable,'-m','unknowns_map.cli']
            def run(args):
                r=subprocess.run(base+args,cwd=d,capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr);return r.stdout
            run(['seed','Fictional migration','--map',str(p)])
            run(['add','ku','Fictional compatibility remains untested','--map',str(p)])
            self.assertIn('Fictional compatibility remains untested',p.read_text())
            self.assertTrue(run(['triage','--map',str(p)]).strip())

if __name__=='__main__':unittest.main(verbosity=2)
