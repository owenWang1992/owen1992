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


class OP:
    # FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-GMAC-DIR-XXXXXX-XXXXXX-PHAS2
    def __init__(self, op):
        self.value = op
        self.components = self.value.split("-")
        self.is_valid = True if len(
            self.components) == OP_COMPONENTS_NUM else False
        try:
            self.product_family = self.components[0]
            self.product_id = self.components[3]
            self.placement = self.components[4]
            self.campaign = self.components[5]
            self.recipe = self.components[6]
            self.brand = self.components[7]
            self.platform = self.components[8]
            self.source = self.components[8]
        except:
            self.is_valid = False

    def has_components_with_consecutive_chars(self, consecutive_char):
        for opcomponent in self.components:
            if opcomponent == consecutive_char * len(opcomponent):
                return True
        return False

    def has_matched_product_family(self, offer):
        return True if self.product_family and offer in offer_table and self.product_family == offer_table[offer] else False

    def has_matched_product_id(self, offer):
        return True if self.product_id and offer in offer_table and self.product_id == offer[-3:] else False

    def has_valid_campaign(self):
        return True if self.campaign and self.campaign in campaigns_table else False

    def has_valid_recipe(self):
        return True if self.recipe and self.recipe in recipes_table else False


class CTA:
    def __init__(self, cta_link):
        self.url = cta_link.get_attribute("href")
        self.title = cta_link.get_attribute("innerText")
        self.hidden = not cta_link.is_displayed()
        self.query = self.url.split(
            "?")[1] if self.url and "?" in self.url else ""
        self.query_data = dict(parse.parse_qsl(self.query))
        self.op = OP(self.query_data["op"]) if "op" in self.query else None
        self.offer = self.query_data["offer"] if "offer" in self.query else ""

    def has_known_offer(self):
        return True if self.offer and self.offer in offer_table else False

    def checkOP(self):
        errors = set()
        if not self.op:
            errors.add(OPError.MISSING_OP)
            return errors
        if not self.op.is_valid:
            errors.add(OPError.INVALID_OP)

        if self.op.has_components_with_consecutive_chars("Y"):
            errors.add(OPError.CONSECUTIVE_Y)

        if not self.has_known_offer():
            errors.add(OPError.UNKNNOW_OFFERTAG)
        else:
            if not self.has_known_offer():
                errors.add(OPError.UNKNNOW_OFFERTAG)
            if not self.op.has_matched_product_family(self.offer):
                errors.add(OPError.MISMATCH_OFFERTAG_PRODUCTFAMILY)
            if not self.op.has_matched_product_id(self.offer):
                errors.add(OPError.MISMATH_OFFERTAG_PRODUCTID)

        if not self.op.has_valid_campaign():
            errors.add(OPError.UNKNOWN_CAMPAIGN)
        if not self.op.has_valid_recipe():
            errors.add(OPError.UNKNOWN_RECIPE)
        return errors       

    def errorInfo(self, error_code):
        if error_code == OPError.INVALID_OP:
            return self.op.value
        elif error_code == OPError.MISMATCH_OFFERTAG_PRODUCTFAMILY:
            return "[" + self.offer + ", " + self.op.product_family + "] should be [" + self.offer + ", " + offer_table[self.offer] + "]"
        elif error_code == OPError.MISMATH_OFFERTAG_PRODUCTID:
            return self.offer + ", " + self.op.product_id
        elif error_code == OPError.CONSECUTIVE_Y:
            return self.op.value
        elif error_code == OPError.UNKNNOW_OFFERTAG:
            return self.offer
        elif error_code == OPError.UNKNOWN_CAMPAIGN:
            return self.op.campaign
        elif error_code == OPError.UNKNOWN_RECIPE:
            return self.op.recipe
        else:
            return ""


def getCTAListFromLinks(links):
    cta_list =[]
    for link in links:
        cta = CTA(link)
        if cta.offer:
            cta_list.append(cta)
    return cta_list

