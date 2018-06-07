from urllib import parse

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

def parseCTALink(link):
        url = link.get_attribute("href")
        cta_data = {}
        if url and "?" in url:
            a = url.split('?')
            cta_data = dict(parse.parse_qsl(a[1]))
            cta_data["url"] = url
            cta_data["title"] = link.get_attribute("innerText")
            cta_data["hidden"] = not link.is_displayed()
            if "op" in cta_data:
                opComponents = cta_data["op"].split("-")
                cta_data["op_product_family"] = "-".join(opComponents[0:1])
                cta_data["op_product_identifier"] = "-".join(opComponents[3:4])
                cta_data["op_placement_identifier"] = "-".join(opComponents[4:5])
                cta_data["op_campaign"] = "-".join(opComponents[5:6])
                cta_data["op_recipe"] = "-".join(opComponents[6:7])
                cta_data["op_brand"] = "-".join(opComponents[7:8])
                cta_data["op_platform"] = "-".join(opComponents[8:9])
        return cta_data

def getCTAListFromLinks(links):
    cta_list = []
    for link in links:
        cta_data = parseCTALink(link)
        if "offer" in cta_data:
            cta_list.append(cta_data)
    return cta_list

def checkMissingOp(cta):
    if "op" in cta:
        return ""
    else:
        return "\tMissing op"


def checkOpOffer(cta):
    if ("op_product_family" in cta) and ("op_product_identifier" in cta) and (cta["offer"] in offer_table):
        product_family = offer_table[cta["offer"]]
        if(product_family == cta["op_product_family"] and cta["op_product_identifier"] == cta["offer"][-3:]):
            return ""
        else:
            return "\tUnmatch offer tag and product: " + cta["offer"] + " " + cta["op_product_family"] + "-" + cta["op_product_identifier"]
    else:
        return "\tMissing or invalid product family, or product identifier: " + cta["offer"] + " " + cta["op_product_family"] + "-" + cta["op_product_identifier"]

def checkCampaign(cta):
    if ("op_campaign" in cta) and cta["op_campaign"] in campaigns_table:
        return ""
    else:
        return "\tInvalid campaign ID: " + cta["op_campaign"]

def checkRecipe(cta):
    if ("op_recipe" in cta) and cta["op_recipe"] in recipes_table:
        return ""
    else:
        return "\tInvalid recipe: " + cta["op_recipe"]
