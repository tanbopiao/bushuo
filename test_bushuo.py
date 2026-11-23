"""布朔（BUSHUO）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from bushuo import Bushuo


class TestBushuo(unittest.TestCase):
    def setUp(self):
        self.op = Bushuo()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "bushuo")
        self.assertEqual(d["code"], "BUSHUO")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_release(self):
        rid = self.op.release("v2", ["批一", "批二"])
        self.assertTrue(rid.startswith("BS-"))
        with self.assertRaises(ValueError):
            self.op.release("v3", [])

    def test_status(self):
        self.op.release("v2", ["批一", "批二"])
        s = self.op.status("v2")
        self.assertEqual(s["batches_total"], 2)
        self.assertEqual(s["state"], "rolling")
        with self.assertRaises(KeyError):
            self.op.status("vX")


if __name__ == "__main__":
    unittest.main()
