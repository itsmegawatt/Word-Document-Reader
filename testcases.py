import unittest
import xml.etree.ElementTree
import worddocumentreader as wdr

class TestOpenAndReadDocument(unittest.TestCase):

    def setUp(self):
        self.docx_path = r'test.docx'
        self.xml = wdr.extract_xml_from_word(self.docx_path)

    def test_open_document(self):
        self.assertEqual(xml.etree.ElementTree.Element, type(self.xml))

    def test_extracting_paragraphs(self):
        self.paragraphs = wdr.extract_paragraphs(self.xml)

    def test_extracting_text(self):
        self.paragraphs = wdr.extract_paragraphs(self.xml)
        self.text = wdr.extract_text(self.paragraphs)
        self.assertEqual(['This is a normal paragraph',
                        'This is a bold paragraph',
                        'This is an italicized paragraph',
                        'This is an underlined paragraph',
                        'This is a bold, italicized, and underlined paragraph',
                        'The paragraph below is a blank paragraph',
                        'The paragraph below is a paragraph with just a space',
                        ' ',
                        'The paragraph below is a pagebreak',
                        '\n',
                        'The paragraph below is a tab',
                        'This word is bolded here', 'This word is italicized here',
                        'This word is underlined here',
                        'This word is bolded, italicized, and underlined here'
                        ], self.text)
        self.text2 = wdr.extract_text_from_path(self.docx_path)
        self.assertEqual(self.text, self.text2)


if __name__ == '__main__':
    unittest.main()