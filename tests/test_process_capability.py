# This is straight codegen output with known mistake for Cpk rating? Need build up to do multiple input cases.

import unittest
from src.cpkmetrics.process_capability import ProcessCapability


class TestProcessCapability(unittest.TestCase):
    def setUp(self):
        """Set up common variables for each test."""
        self.mean = 9
        self.stddev = 0.2
        self.usl = 12.0
        self.lsl = 8.0
        self.pc = ProcessCapability(self.mean, self.stddev, self.usl, self.lsl)

    def test_Cp(self):
        """Test the Cp calculation."""
        expected_c_p = (self.usl - self.lsl) / (6 * self.stddev)
        self.assertAlmostEqual(self.pc.Cp(), expected_c_p, places=3)

    def test_Cpu(self):
        """Test the Cpu calculation."""
        expected_c_pu = (self.usl - self.mean) / (3 * self.stddev)
        self.assertAlmostEqual(self.pc.Cpu(), expected_c_pu, places=3)

    def test_Cpl(self):
        """Test the Cpl calculation."""
        expected_c_pl = (self.mean - self.lsl) / (3 * self.stddev)
        self.assertAlmostEqual(self.pc.Cpl(), expected_c_pl, places=3)

    def test_Cpk(self):
        """Test the Cpk calculation."""
        expected_c_pk = min(
            (self.usl - self.mean) / (3 * self.stddev),
            (self.mean - self.lsl) / (3 * self.stddev),
        )
        self.assertAlmostEqual(self.pc.Cpk(), expected_c_pk, places=3)

    def test_Cpa(self):
        """Test the Cpa calculation."""
        expected_c_pa = (self.mean - (self.usl + self.lsl) / 2) / (self.usl - self.lsl)
        self.assertAlmostEqual(self.pc.Cpa(), expected_c_pa, places=3)

    def test_Cpk_rating(self):
        """Test the Cpk rating."""
        self.assertEqual(self.pc.Cpk_rating(), "Good")

    def test_Cpa_rating(self):
        """Test the Cpa rating."""
        c_pa = self.pc.Cpa()
        if c_pa < 0:
            self.assertEqual(self.pc.Cpa_rating(), "Level A")
        elif c_pa < 0.125:
            self.assertEqual(self.pc.Cpa_rating(), "Level B")
        elif c_pa < 0.25:
            self.assertEqual(self.pc.Cpa_rating(), "Level C")
        else:
            self.assertEqual(self.pc.Cpa_rating(), "Level D")


if __name__ == "__main__":
    unittest.main()
