import unittest

from seo_meta import (DESC_MAX, DESC_MIN, TITLE_MAX, TITLE_MIN, generate,
                      gen_description, gen_title, validate)


class TestGen(unittest.TestCase):
    def test_title_contains_keyword(self):
        t = gen_title("空气炸锅选购")
        self.assertIn("空气炸锅选购", t)

    def test_title_length_compliant(self):
        for kw in ["Python 教程", "咖啡", "家庭装修风格效果图大全推荐"]:
            t = gen_title(kw)
            self.assertLessEqual(len(t), TITLE_MAX)

    def test_description_contains_keyword(self):
        d = gen_description("空气炸锅选购")
        self.assertIn("空气炸锅选购", d)

    def test_description_length(self):
        d = gen_description("空气炸锅选购")
        self.assertLessEqual(len(d), DESC_MAX)

    def test_empty_keyword_raises(self):
        with self.assertRaises(ValueError):
            gen_title("  ")

    def test_truncate_very_long_keyword(self):
        kw = "超长关键词" * 30
        t = gen_title(kw)
        self.assertLessEqual(len(t), TITLE_MAX)


class TestValidate(unittest.TestCase):
    def test_generate_validation(self):
        res = generate("空气炸锅选购")
        v = res["validation"]
        self.assertIn("title_ok", v)
        self.assertIn("description_ok", v)
        self.assertTrue(v["title_ok"])
        self.assertTrue(v["description_ok"])

    def test_validate_short(self):
        v = validate("短", "短")
        self.assertFalse(v["title_ok"])
        self.assertFalse(v["description_ok"])


if __name__ == "__main__":
    unittest.main()
