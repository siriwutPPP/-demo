import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    try:
        z = zipfile.ZipFile(docx_path)
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        text = [node.text for node in tree.iterfind('.//w:t', ns) if node.text]
        return ' '.join(text)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    path = sys.argv[1]
    print(extract_text_from_docx(path)[:1000])
