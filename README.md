# Word-Document-Reader
Python module that reads and extracts all text from a word document

Example of how to use:

    xml = extract_xml_from_word('./test.docx')
    paragraphs = extract_paragraphs(xml)
    text = extract_text(paragraphs)

Returns this:

    ['This is a normal paragraph', 'This is a bold paragraph', 'This is an italicized paragraph', 'This is an underlined paragraph', 'This is a bold, italicized, and underlined paragraph', 'The paragraph below is a blank paragraph', 'The paragraph below is a paragraph with just a space', ' ', 'The paragraph below is a pagebreak', '\n', 'The paragraph below is a tab', 'This word is bolded here', 'This word is italicized here', 'This word is underlined here', 'This word is bolded, italicized, and underlined here']