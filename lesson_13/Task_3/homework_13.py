import xml.etree.ElementTree as ET
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def find_timing_incoming_by_group_number(xml_file, group_number):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == group_number:
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        logger.info(f"Found timingExbytes/incoming for group/number {group_number}: {incoming.text}")
                        return incoming.text

        logger.info(f"No matching group/number found for {group_number}")
        return None

    except ET.ParseError as e:
        logger.error(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None


xml_file_name = r'groups.xml'
group_number_to_search = '4'

find_timing_incoming_by_group_number(xml_file_name, group_number_to_search)
