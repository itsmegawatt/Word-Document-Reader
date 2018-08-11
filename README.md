# Word-Document-Reader
Python module that reads and extracts all text from a word document

Example of how to use:

    xml = extract_xml_from_word('./lorem.docx')
    paragraphs = extract_paragraphs(xml)
    text = extract_text(paragraphs)
    print(text)

or (this does exactly the same as above):

    text = extract_text_from_path('./lorem.docx')
    print(text)

Returns this:

['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas egestas magna velit, a interdum dui fringilla et. Duis nulla arcu, tempus ut ex id, suscipit dignissim ipsum. Praesent elementum elementum justo, ut luctus turpis iaculis nec. Cras ornare iaculis urna ut pulvinar. Vivamus a euismod nisi, in euismod ex. Aliquam pretium neque leo, eu laoreet felis fermentum ac. Nam dignissim accumsan enim, ac ullamcorper sem posuere quis. Sed luctus nisi a velit sodales, a accumsan sapien consequat. Phasellus efficitur tellus et iaculis imperdiet.',

'Vivamus maximus nisl molestie condimentum viverra. Sed volutpat blandit eros, nec lacinia nulla pharetra nec. Nullam volutpat eget purus luctus eleifend. Nullam sed interdum diam, id dignissim purus. Aenean neque mauris, pulvinar non nunc in, pretium fermentum ligula. Proin tristique lobortis ipsum quis tincidunt. Donec tincidunt eget risus et venenatis. Donec tempus auctor sem ut commodo. Aliquam id quam eu nibh tincidunt tempus ac eget tellus. Integer in lectus purus. Etiam tincidunt ligula est, vel vulputate ipsum placerat elementum. Proin luctus lacus velit, vel venenatis mi malesuada ut. Donec sed sollicitudin est. Phasellus quis venenatis ipsum, vel blandit arcu. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Integer ipsum est, volutpat eu arcu et, imperdiet mollis enim.',

'Fusce vel enim quis eros tincidunt porttitor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in ante et tellus dictum commodo. Donec ultricies dapibus leo, id aliquet tellus sodales at. Suspendisse sit amet velit sem. Mauris pulvinar faucibus mauris bibendum dictum. Morbi in condimentum turpis. Donec eget sapien non tellus interdum egestas. Nam a eros a ex vulputate fermentum sit amet et neque. Morbi facilisis bibendum justo sit amet porta. Sed dignissim nisi eget arcu malesuada maximus. Quisque elementum lacus vel lacinia pretium. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce a vulputate justo. Vivamus et iaculis quam. Mauris ut lacus metus.',

'Integer ut quam bibendum sapien semper pulvinar ac sit amet libero. In varius massa non velit iaculis, at gravida turpis posuere. Vestibulum quis mollis nunc. Vestibulum venenatis lorem quis erat pulvinar, quis tincidunt elit pulvinar. Aenean vulputate nisl at orci egestas ultrices. Pellentesque tortor purus, blandit et lorem at, rhoncus mollis ante. Vestibulum orci velit, porta eget auctor in, aliquam a mi. Integer faucibus libero quis augue laoreet blandit. Donec finibus nibh at nisl sagittis, sit amet mollis nisi malesuada. Maecenas enim nulla, dignissim a tincidunt eget, feugiat a justo. Fusce mollis tempor nibh quis finibus. Vestibulum rutrum dictum nibh sed porta. Aenean pharetra dui dolor, nec ullamcorper orci tristique eget.']