# importing library
import redis
import json
import hashlib


# creating an Redis instance
r = redis.Redis(host='localhost', port=6379, db=0)


events = [
    {
        'sku':"123-ABC-723",
        'name': "Men's 100m Final",
        'disabled_access': True,
        'medal_event': True,
        'venue':'Olympic Stadium',
        'category': "Track & Field"
    },
    {
        'sku':"737-DEF-911",
        'name': "Wommen's 4x100m Heats",
        'disabled_access': True,
        'medal_event': False,
        'venue':'Olympic Stadium',
        'category': "Track & Field"
    },
    {
        'sku':"320-GHI-921",
        'name': "Womens Judo Qualifying",
        'disabled_access': False,
        'medal_event': False,
        'venue':'Nippon Budokan',
        'category': "Martial Arts"
    }
]

filter_key = ['disabled_access','medal_event','venue']

def create_events(e_array):

    for i in range(len(e_array)):
        key = "event:" + e_array[i]['sku']
        r.set(key, json.dumps(e_array[i]))

def print_event_name(event_sku):

    key = "event:" + event_sku
    event = json.loads(r.get(key))

    print(event['name']) if ('name' in event) else event['sku']

def match_by_inspection(*keys):
    matches = []
    key = "event:" + "*"
    for key in r.scan_iter(key):
        match = False
        event = json.loads(r.get(key))
        for keyval in keys:
            key, val = keyval
            if key in event and event[key] == val:
                match = True
            else:
                match = False
                break
        if match:
            matches.append(event['sku'])
    return matches

def test_object_inspection():
    print("Method 1: Object Inspection..")
    create_events(events)

    print("\nDisabled access == True", sep="\n")
    matches = match_by_inspection(('disabled_access', True))
    for match in matches:
        print_event_name(match)

    print("\nDisabled access == True, medal_event=False", sep="\n")
    matches = match_by_inspection(('disabled_access', True), ('medal_event', False))
    for match in matches:
        print_event_name(match)

    print("\nDisabled access == True, medal_event=False, venue='Nippon Budokan'", sep="\n")
    matches = match_by_inspection(('disabled_access', True), ('medal_event', False), ('venue', 'Nippon Budokan'))
    for match in matches:
        print_event_name(match)

def create_set(e_array):
    for i in range(len(e_array)):
        key = "event:" + e_array[i]['sku']
        r.set(key, json.dumps(e_array[i]))

        for k in range(len(filter_key)):
            if filter_key[k] in e_array[i]:
                att_name = str(e_array[i][filter_key[k]])
                fs_key = "fs:" + filter_key[k] + ":" + att_name

                r.sadd(fs_key, e_array[i]['sku'])


def match_by_faceted_search(*keys):
    facets =[]
    for keyval in keys:
        key, val = keyval
        fs_key = "fs:" + str(key) + ":" + str(val)
        facets.append(fs_key)
    return r.sinter(facets)

def test_faceted_search():
    print("\nMethod 2: Faceted Search..", sep="\n")
    create_set(events)

    print("\nDisabled access == True", sep="\n")
    matches = match_by_faceted_search(('disabled_access', True))
    # print(matches)
    for match in matches:
        print_event_name(match.decode("utf-8"))

    print("\nDisabled access == True, medal_event=False", sep="\n")
    matches = match_by_faceted_search(('disabled_access', True), ('medal_event', False))
    for match in matches:
        print_event_name(match.decode("utf-8"))

    print("\nDisabled access == True, medal_event=False, venue='Nippon Budokan'", sep="\n")
    matches = match_by_faceted_search(('disabled_access', True), ('medal_event', False), ('venue', 'Nippon Budokan'))
    for match in matches:
        print_event_name(match.decode("utf-8"))

def create_hash(e_array):
    for i in range(len(e_array)):
        key = "event:" + e_array[i]['sku']
        r.set(key, json.dumps(e_array[i]))
        hfs = []
        for key in range(len(filter_key)):
            if filter_key[key] in e_array[i]:
                hfs.append((filter_key[key],e_array[i][filter_key[key]]))
            # print(hfs)
            hashed_val = hashlib.sha256(str(hfs).encode("Utf-8")).hexdigest()
            # print(hashed_val)
            hfs_key = "hfs:" + hashed_val

            r.sadd(hfs_key, e_array[i]['sku'])

def match_by_hashed_faceted(*keys):
    matchs = []
    hfs = []

    for i in range(len(filter_key)):
        key = [x for x in keys if x[0] == filter_key[i]]
        if key:
            hfs.append(key[0])
            # print(key[0])
    hashed_val = hashlib.sha256(str(hfs).encode("Utf-8")).hexdigest()
    hashed_key = "hfs:" + hashed_val

    for found_key in r.sscan_iter(hashed_key):
        matchs.append(found_key)

    return matchs

def test_hashed_faceted_search():
    print("\nMethod 3: Hashed Faceted Search..", sep="\n")
    create_hash(events)

    print("\nDisabled access == True", sep="\n")
    matches = match_by_hashed_faceted(('disabled_access', True))
    # print(matches)
    for match in matches:
        print_event_name(match.decode("utf-8"))

    print("\nDisabled access == True, medal_event=False", sep="\n")
    matches = match_by_hashed_faceted(('disabled_access', True), ('medal_event', False))
    for match in matches:
        print_event_name(match.decode("utf-8"))

    print("\nDisabled access == True, medal_event=False, venue='Nippon Budokan'", sep="\n")
    matches = match_by_hashed_faceted(('disabled_access', True), ('medal_event', False), ('venue', 'Nippon Budokan'))
    for match in matches:
        print_event_name(match.decode("utf-8"))



if __name__ == "__main__":
    test_object_inspection()
    test_faceted_search()
    test_hashed_faceted_search()
