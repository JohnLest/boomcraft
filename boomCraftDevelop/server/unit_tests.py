import sys
from server.tests.unit.test_entity import TestEntity
import unittest

print(f"Work with {sys.version}")


suite = unittest.TestLoader().loadTestsFromModule(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)