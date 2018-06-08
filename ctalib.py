from urllib import parse
from enum import Enum

OP_COMPONENTS_NUM = 13

error_table = {
    100: "Missing OP",
    101: "Invalid OP",
    102: "Mismatching offer tag and product family",
    103: "Unknown offer tag",
    104: "Mismatching offer tag and product identifier",
    105: "Consecutive Y exist in op components",
    106: "Unknown campaign code",
    107: "Unknown recipe code"
}
# FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-GMAC-DIR-XXXXXX-XXXXXX-PHAS2


class OPComponent(Enum):
    PRODUCT_FAMILY = 0
    PRODUCT_ID = 3
    PLACEMENT = 4
    CAMPAIGN = 5
    RECIPE = 6

class OPError(Enum):
    MISSING_OP = 100
    INVALID_OP = 101
    MISMATCH_OFFERTAG_PRODUCTFAMILY = 102
    UNKNNOW_OFFERTAG = 103
    MISMATH_OFFERTAG_PRODUCTID = 104
    CONSECUTIVE_Y = 105
    UNKNOWN_CAMPAIGN = 106
    UNKNOWN_RECIPE = 107

    def msg(self):
        return error_table[self.value]


offer_table = {
    'at_frsas102': 'FRSC',
    'at_frsas103': 'FRSI',
    'at_fcras100': 'FRCR',
    'at_fcras105': 'FRRI',
    'at_fcras102': 'FRCD',
    'at_ltdreg100': 'FRLR',
    'at_eiwt100': 'WPTC',
    'at_eiwt109': 'WPTC',
    'at_eiwt110': 'WPTC',
    'at_eiwd100': 'WPDC',
    'at_eiwb105': 'WPMC',
    'at_eiwmbg100': 'G1TC',
    'at_eiwmbg101': 'G1TC',
    'at_eiwa104': 'WPAC',
    'at_eiwambg100': 'G1AC',
    'at_eiwpt104': 'W3TC',
    'at_eiwpt103': 'W3TC',
    'at_eiwpt101': 'W3TC',
    'at_eiwpd102': 'W3DC',
    'at_eiwp104': 'W3MC',
    'at_eiwpmbg100': 'G3TC',
    'at_eiwpa106': 'W3AC',
    'at_eiwpambg100': 'G3AC',
    'at_eiwl100': 'WCMI',
    'at_eiwla100': 'WCAI',
    'at_eiwt103': 'W1TI',
    'at_eiwt104': 'W1TI',
    'at_eiwb103': 'W1MI',
    'at_eiwb102': 'W1MI',
    'at_eiwmbg102': 'G1TI',
    'at_eiwmbg103': 'G1TI',
    'at_eiwa103': 'W1AI',
    'at_eiwa102': 'W1AI',
    'at_eiwambg101': 'G1AI',
    'at_eiwambg102': 'W1AG',
    'at_eiwct100': 'W1TK',
    'at_eiwbc100': 'W1MK',
    'at_eiwcmbg100': 'G1TK',
    'at_eiwac100': 'W1AK',
    'at_eiwacmbg100': 'G1AK',
    'at_eiwft100': 'W1TF',
    'at_eiwbf100': 'W1MF',
    'at_eiwfmbg100': 'G1TF',
    'at_eiwaf100': 'W1AF',
    'at_eiwafmbg100': 'G1AF',
    'at_eiwpt102': 'W3TI',
    'at_eiwpd101': 'W3DI',
    'at_eiwpd103': 'W3DI',
    'at_eiwp103': 'W3MI',
    'at_eiwp102': 'W3MI',
    'at_eiwpmbg101': 'W3MG',
    'at_eiwpa104': 'W3AI',
    'at_eiwpa103': 'W3AI',
    'at_eiwpambg101': 'G3AI',
    'at_eiwpambg102': 'G3AI',
    'at_eiwpct100': 'W3TK',
    'at_eiwpbc100': ': W3MK',
    'at_eiwpcmbg100': ': G3MK',
    'at_eiwpac100': ': W3AK',
    'at_eiwpacmbg100': ': G3AK',
    'at_eiwpft100': ': W3TF',
    'at_eiwpbf100': ': W3MF',
    'at_eiwpfmbg100': ': G3MF',
    'at_eiwpaf100': ': W3AF',
    'at_eiwpafmbg100': 'G3AF',
    'at_1b1s108': '1B1S',
    'at 1b1s109': '1B1S',
    'at_1b1s109': '1B1S',
    'at_3b3s109': '3B3S',
    'at_3b3s102': '3B3S',
    'at_3b3s113': '3B3S',
    'at_3b3s100': '3B3S',
    'at_3b3s110': '3B3S'
}

campaigns_table = ["RNSCOMP"]
recipes_table = ["A0", "B0"]

def errorComponent(cta, errorCode):
    if errorCode == OPError.INVALID_OP:
        return cta["op"]
    elif errorCode == OPError.MISMATCH_OFFERTAG_PRODUCTFAMILY:
        return "[" + cta["offer"] + ", " + opComponent(cta, OPComponent.PRODUCT_FAMILY) + "] should be [" + cta["offer"] + ", " + offer_table[cta["offer"]] + "]"
    elif errorCode == OPError.MISMATH_OFFERTAG_PRODUCTID:
        return cta["offer"] + ", " + opComponent(cta, OPComponent.PRODUCT_ID)
    elif errorCode == OPError.CONSECUTIVE_Y:
        return cta["op"]
    elif errorCode == OPError.UNKNNOW_OFFERTAG:
        return cta["offer"]
    elif errorCode == OPError.UNKNOWN_CAMPAIGN:
        return opComponent(cta, OPComponent.CAMPAIGN)
    elif errorCode == OPError.UNKNOWN_RECIPE:
        return opComponent(cta, OPComponent.RECIPE)
    else:
        return ""

def opComponent(cta, opc):
    return cta["op"].split("-")[opc.value]

def parseCTALink(link):
    url = link.get_attribute("href")
    cta_data = {}
    if url and "?" in url:
        a = url.split('?')
        cta_data = dict(parse.parse_qsl(a[1]))
        cta_data["url"] = url
        cta_data["title"] = link.get_attribute("innerText")
        cta_data["hidden"] = not link.is_displayed()
    return cta_data


def getCTAListFromLinks(links):
    cta_list = []
    for link in links:
        cta_data = parseCTALink(link)
        if "offer" in cta_data:
            cta_list.append(cta_data)
    return cta_list


def checkOp(cta):
    errors = set()
    if not "op" in cta:
        errors.add(OPError.MISSING_OP)
        return errors

    opcomponents = cta["op"].split("-")
    # check op length, must be 13
    if len(opcomponents) != OP_COMPONENTS_NUM:
        errors.add(OPError.INVALID_OP)

    # check YYYY
    for opcomponent in opcomponents:
        if opcomponent == "Y" * len(opcomponent):
            errors.add(OPError.CONSECUTIVE_Y)

    # check offer and product
    if not cta["offer"] in offer_table:
        errors.add(OPError.UNKNNOW_OFFERTAG)
    else:
        product_family = offer_table[cta["offer"]]
        if product_family != opComponent(cta, OPComponent.PRODUCT_FAMILY):
            errors.add(OPError.MISMATCH_OFFERTAG_PRODUCTFAMILY)
        if opComponent(cta, OPComponent.PRODUCT_ID) != cta["offer"][-3:]:
            errors.add(OPError.MISMATH_OFFERTAG_PRODUCTID)

    # check campaign
    if not opComponent(cta, OPComponent.CAMPAIGN) in campaigns_table:
        errors.add(OPError.UNKNOWN_CAMPAIGN)

    # check recipe
    if not opComponent(cta, OPComponent.RECIPE) in recipes_table:
        errors.add(OPError.UNKNOWN_RECIPE)

    return errors
