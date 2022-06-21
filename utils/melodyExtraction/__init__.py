try:
    from melodyExtraction_NS import *
    from model import *

except ModuleNotFoundError or ImportError:
    from melodyExtraction.model import *
    from melodyExtraction.melodyExtraction_NS import * 