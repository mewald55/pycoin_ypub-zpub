import unittest

from pycoinzpub.ecdsa.secp256k1 import secp256k1_generator


class SigningTest(unittest.TestCase):
    def test_sign(self):
        PART1 = ["47f7616ea6f9b923076625b4488115de1ef1187f760e65f89eb6f4f7ff04b012"]
        PART2 = [x * 64 for x in "123456789abcde"]
        for se in PART1 + PART2:
            secret_exponent = int(se, 16)
            val = 28832970699858290
            sig = secp256k1_generator.sign(secret_exponent, val)

            public_pair = secp256k1_generator * secret_exponent

            v = secp256k1_generator.verify(public_pair, val, sig)
            self.assertTrue(v)

            sig1 = (sig[0] + 1, sig[1])
            v = secp256k1_generator.verify(public_pair, val, sig1)
            self.assertFalse(v)

            public_pairs = secp256k1_generator.possible_public_pairs_for_signature(val, sig)
            self.assertIn(public_pair, public_pairs)
            print(se)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
