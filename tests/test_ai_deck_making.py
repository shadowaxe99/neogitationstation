```python
import unittest
from src.ai_deck_making import createDeck
from src.utils import validatePresentationContent, validatePresentationStructure

class TestAIDeckMaking(unittest.TestCase):

    def setUp(self):
        self.presentation_content = {
            "title": "AI Presentation",
            "slides": [
                {"title": "Slide 1", "content": "Content for slide 1"},
                {"title": "Slide 2", "content": "Content for slide 2"},
                {"title": "Slide 3", "content": "Content for slide 3"}
            ]
        }
        self.presentation_structure = {
            "slide_order": [1, 2, 3],
            "theme": "Professional"
        }

    def test_validatePresentationContent(self):
        result = validatePresentationContent(self.presentation_content)
        self.assertTrue(result)

    def test_validatePresentationStructure(self):
        result = validatePresentationStructure(self.presentation_structure)
        self.assertTrue(result)

    def test_createDeck(self):
        deck = createDeck(self.presentation_content, self.presentation_structure)
        self.assertIsNotNone(deck)
        self.assertEqual(len(deck), len(self.presentation_content["slides"]))

if __name__ == '__main__':
    unittest.main()
```