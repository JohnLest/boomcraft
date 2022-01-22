import sys
from tests.unit.test_entity import TestEntity
import unittest

print(f"Work with {sys.version}")


suite = unittest.TestLoader().loadTestsFromModule(TestEntity)
unittest.TextTestRunner(verbosity=2).run(suite)