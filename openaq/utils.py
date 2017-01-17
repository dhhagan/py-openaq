import dateutil

def to_naive_timestamp(timestamp):
    """
        Convert a timezone aware timestamp (as a string) and return the
        python datetime in the local timezone, but without the tzinfo attribute
    """
    return dateutil.parser.parse(timestamp).replace(tzinfo=None).isoformat()
