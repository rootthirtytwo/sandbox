# importing library
import redis
import json

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

if __name__ == "__main__":
    test_object_inspection()


