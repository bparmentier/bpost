#!/usr/bin/env python3

import argparse
import json

import requests

TRANSLATIONS_URL = "https://track.bpost.be/btr/api/translations?v=1459286845418&lang={}"
ITEMS_URL = "https://track.bpost.be/btr/api/items?itemIdentifier={}"
LANG = ['en', 'fr', 'nl']


def main(parcel_id):
    response = requests.get(ITEMS_URL.format(parcel_id))

    items = json.loads(response.text)
    #print(json.dumps(items, indent=4))
    item = items[0]
    activeStep = item['processOverview']['activeStepTextKey']
    print("Parcel state:", activeStep)


if __name__ == '__main__':
    parser = argparse.parser = argparse.ArgumentParser(description="Track bpost parcel")
    parser.add_argument('tracking_nb', help="Tracking number")

    args = parser.parse_args()

    main(args.tracking_nb)
