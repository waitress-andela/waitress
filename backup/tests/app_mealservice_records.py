import datetime

import psycopg2

records = [
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            12,
            26,
            848255,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1275,
        "Amaka",
        "Mbaegbu",
        "staff",
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            24,
            41,
            501035,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1613,
        None,
        None,
        None,
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            1,
            18,
            828866,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        732,
        "LOS",
        "018",
        "LOS 018",
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            10,
            35,
            610977,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1126,
        "Chiagoziem",
        "Young Nwadike",
        "staff",
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            16,
            16,
            545402,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1560,
        None,
        None,
        None,
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            24,
            28,
            364384,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        814,
        "Onuchukwu",
        "Chika",
        "staff",
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            7,
            58,
            37,
            60525,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1247,
        "Odinakachukwu",
        "Ezeobika",
        "staff",
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            7,
            59,
            18,
            136991,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1130,
        "Adépòjù",
        "Olúwáségun",
        "staff",
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            2,
            18,
            282343,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1595,
        None,
        None,
        None,
        True,
        False,
    ),
    (
        "06-02-2020",
        datetime.datetime(
            2020,
            2,
            6,
            8,
            26,
            32,
            887446,
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=60, name=None),
        ),
        1514,
        None,
        None,
        None,
        True,
        False,
    ),
]
