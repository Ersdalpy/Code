# Import the XML library for parsing and working with XML documents
import xml.etree.ElementTree as ET

def find_broken_attributes_recursive(element):
    """
    Recursively goes through an XML tree and checks if any attributes are broken.
    A "broken" attribute here means it has an empty value (e.g., age="").
    
    Args:
        element (xml.etree.ElementTree.Element): The current XML element being inspected.
    """
    # Check all attributes of the current element
    for attr_name, attr_value in element.attrib.items():  
        # If the attribute value is empty, we consider it broken
        if attr_value == "":
            # Print the attribute name, its (empty) value, and the tag it's part of
            print(f"Broken attribute: '{attr_name}' (value: '{attr_value}') in element <{element.tag}>")
    
    # Now check the child elements of the current element
    for child in element:  
        # Call this function on each child to keep searching for broken attributes
        find_broken_attributes_recursive(child)

# Here's some example XML data for testing the function
# Tarzan and Jane are living in the jungle with incomplete data for demonstration purposes.
xml_data = """
<root>
    <person name="Tarzan" age="" location="Deep Jungle">
        <address street="123 Jungle Tree" city="" zip="00000"/>
        <contact phone="" email="tarzan@jungle.com"/>
    </person>
    <person name="Jane" age="28" location="">
        <address street="" city="Jungle City" zip=""/>
        <contact phone="123-456-789" email=""/>
    </person>
</root>
"""

# Parse the XML string into a tree structure
# This turns the raw XML into something Python can process element by element
root = ET.fromstring(xml_data)

# Start searching for broken attributes from the root of the XML
print("Looking for broken attributes in the XML data:")
find_broken_attributes_recursive(root)