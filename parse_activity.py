from collections import namedtuple

ParsedActivityFields = ["activity_name", "life_aspect", "more_info"]
ParsedActivity = namedtuple("ParsedActivity", ParsedActivityFields)

def parse_activity(line: str) -> ParsedActivity:
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
    
    return ParsedActivity(activity_name, life_aspect, more_info)

if __name__ == "__main__":
    activity_line1 = "developing my habit tracker; Career | Working on the more info feature"
    activity1 = parse_activity(activity_line1)
    print(f"{activity1.activity_name};{activity1.life_aspect};{activity1.more_info}")
    activity_line2 = "developing my habit tracker; Career"
    activity2 = parse_activity(activity_line2)
    print(f"{activity2.activity_name};{activity2.life_aspect};{activity2.more_info}")
    activity_line3 = "developing my habit tracker | Working on the more info feature"
    activity3 = parse_activity(activity_line3)
    print(f"{activity3.activity_name};{activity3.life_aspect};{activity3.more_info}")
    activity_line4 = "developing my habit tracker"
    activity4 = parse_activity(activity_line4)
    print(f"{activity4.activity_name};{activity4.life_aspect};{activity4.more_info}")
