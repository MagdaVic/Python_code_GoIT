from collections import Counter


def get_count_visits_from_ip(ips):
    ips_dict=Counter(ips)
    return ips_dict
    


def get_frequent_visit_from_ip(ips):
    return get_count_visits_from_ip(ips).most_common(1)[0]



    