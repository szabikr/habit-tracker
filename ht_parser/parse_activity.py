from ht_models.raw_models import RawActivity

def parse_activity(line: str) -> RawActivity:
    activity_parts = line.split("|")
    raw_activity_props = activity_parts[0]
    try:
        more_info = activity_parts[1].strip()
    except IndexError:
        more_info = None
    
    activity_props = raw_activity_props.split(";")
    activity_name = activity_props[0].strip()
    try:
        life_aspect = activity_props[1].strip()
    except IndexError:
        life_aspect = None
    
    return RawActivity(activity_name, life_aspect, more_info)

if __name__ == "__main__":
    activity_line1 = "developing my habit tracker; Career | Working on the more info feature"
    activity1 = parse_activity(activity_line1)
    print(activity1)
    activity_line2 = "developing my habit tracker; Career"
    activity2 = parse_activity(activity_line2)
    print(activity2)
    activity_line3 = "developing my habit tracker | Working on the more info feature"
    activity3 = parse_activity(activity_line3)
    print(activity3)
    activity_line4 = "developing my habit tracker"
    activity4 = parse_activity(activity_line4)
    print(activity4)
