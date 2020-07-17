import json
import io

def saveOverrideFile(data, filename = "config_override.json"):
    """Save the JSON to a file directory in textfiles/
    
    Arguments:
        data dictionary -- keyvalue pairs for the JSON file
    
    Keyword Arguments:
        filename {str} -- the file directory location (default: {"config_override.json"})
    """
    with io.open('text_files/config_override.json', 'w', encoding='utf-8') as settings:
        json.dump(data,settings,ensure_ascii=False, indent=4)