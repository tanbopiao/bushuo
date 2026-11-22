"""布朔（BUSHUO）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_release_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.release(None, None)

    def test_status_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.status(None)


if __name__ == "__main__":
    unittest.main()
