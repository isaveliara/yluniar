import re

#methods
def detect_device(user_agent):
    if re.search(r'Mobile|Android|iP(hone|od|ad)', user_agent):
        return 'mobile'
    elif re.search(r'Tablet', user_agent):
        return 'tablet'
    else:
        return 'desktop'