import json

class XAIF:
    @staticmethod
    def format(nodes, edges, locutions, schemefulfillments, descriptorfulfillments, participants, OVA, text_with_span,dialog=False, aif={}, x_aif={}):
        aif['nodes'] = nodes
        aif['edges'] =  edges
        aif['locutions'] =  locutions
        aif['schemefulfillments'] = schemefulfillments
        aif['descriptorfulfillments'] = descriptorfulfillments
        aif['participants'] =  participants
        x_aif['AIF'] = aif
        x_aif['ova'] =  OVA
        x_aif['dialog'] =  dialog
        x_aif['text'] =  {'txt':text_with_span}
        return json.dumps(x_aif)
