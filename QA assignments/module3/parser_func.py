import re

def parse_ap_summary(output):
    ap_regex = re.compile(
        r'^(?P<ap_name>\S+)\s+'
        r'(?P<slots>\d+)\s+'
        r'(?P<ap_model>\S+)\s+'
        r'(?P<ethernet_mac>\S+)\s+'
        r'(?P<radio_mac>\S+)\s+'
        r'(?P<cc>\S+)\s+'
        r'(?P<rd>\S+)\s+'
        r'(?P<ip_address>\S+)\s+'
        r'(?P<state>\S+)\s+'
        r'(?P<location>.+)$'
    )

    aps = []
    start_parsing = False
    for line in output.splitlines():
        if 'AP Name' in line:
            start_parsing = True
            continue
        if start_parsing and line.strip() and not line.startswith('--'):
            match = ap_regex.match(line.strip())
            if match:
                ap_info = match.groupdict()
                aps.append(ap_info)

    return aps
