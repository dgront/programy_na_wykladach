import re

#cyp_regex = "hits from CYP\d+[A-Z]+ family \(e-value: [\d\.]+e-\d+\)"
cyp_regex = "hits from (CYP\d+[A-Z]+) family \(e-value: ([\d\.]+e-\d+)\)"
inputs = """
--- hits from CYP631B family (e-value: 8.1e-268):
--- hits from CYP603E family (e-value: 6.8e-53):
--- hits from CYP65AH family (e-value: 0.0):
--- hits from CYP617F family (e-value: 6.3e-289):
--- hits from CYP51597A family (e-value: 3.1e-270):
--- hits from CYP627A family (e-value: 1.5e-294):
--- hits from CYP51597A family (e-value: 3e-192):
--- hits from CYP51406A family (e-value: 0.0):
--- hits from CYP59H family (e-value: 2.1e-66):
--- hits from CYP71BT family (e-value: 5.4e-270):
--- hits from CYP71AY family (e-value: 6.6e-286):
--- hits from CYP76A family (e-value: 6.2e-255):
--- hits from CYP81C family (e-value: 2.8e-249):
--- hits from CYP71D family (e-value: 1.3e-225):
--- hits from CYP81AX family (e-value: 5.7e-281):
--- hits from CYP76T family (e-value: 1.3e-250):
--- hits from CYP72A family (e-value: 9.8e-259):
--- hits from CYP71AX family (e-value: 1e-235):
--- hits from CYP71BZ family (e-value: 1.5e-251):
--- hits from CYP71CA family (e-value: 4.8e-284):
--- hits from CYP71CB family (e-value: 0.0):
--- hits from CYP71BL family (e-value: 0.0):
"""

import glob

zliczenia = {}
for nazwa_pliku in glob.glob("/Users/dgront/work.runs/SwissProt_P450/OUTPUTS/hits_out/*.stdout"):
    print(nazwa_pliku)
    for inp_line in open(nazwa_pliku):
        m = re.findall(cyp_regex, inp_line)
        if len(m) > 0:
            cyp_id = m[0][0]
            if not cyp_id in zliczenia:
                zliczenia[cyp_id] = 1
            else:
                zliczenia[cyp_id] += 1
print(zliczenia)