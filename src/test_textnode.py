import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINKS, url="https://www.boot.dev")
        node2 = TextNode("This is another link node", TextType.LINKS, url="https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_italic_text(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        node2 = TextNode("This is an italic node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_empty(self):
        node = TextNode("This is an empty link node", TextType.LINKS, url="https://www.boot.dev")
        node2 = TextNode("This is an empty link node", TextType.LINKS, url=None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()