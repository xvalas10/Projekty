"""
IPP - Project 2. - Interpret of IPPCODE21
Author - Samuel Valaštín <xvalas10@stud.fit.vutbr.cz> 
All possible EXIT CODES for interpret
"""

class Exit_Codes:
    OK = 0
    INVALID_COMMAND_LINE_ERR = 10
    INVALID_INPUT_FILE_ERR = 11
    INVALID_OUTPUT_FILE_ERR = 12
    INVALID_XML_FORMAT_ERR = 31
    INVALID_XML_STRUCT_ERR = 32
    SEMANTIC_ERR = 52
    INVALID_OP_TYPES_ERR = 53
    INVALID_VAR_ACCESS_ERR = 54
    INVALID_FRAME_ERR = 55
    INVALID_VAR_VALUE_ERR = 56
    INVALID_OP_VAL_ERR = 57         #division by 0, invalid EXIT value
    INVALID_STR_OP_ERR = 58 
    INTERNAL_ERR = 99

