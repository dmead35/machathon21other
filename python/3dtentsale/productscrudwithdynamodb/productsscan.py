from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def scan_products(title_range, display_products, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')
    scan_kwargs = {
        'FilterExpression': Key('title').between(*title_range),
        'ProjectionExpression': "#sku, title, info.price",
        'ExpressionAttributeNames': {"#sku": "sku"}
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        display_products(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    def print_products(products):
        for product in products:
            print(f"\n{product['title']}")

    query_range = ("B", "Z")
    print(f"Scanning for products with titles from {query_range[0]} to {query_range[1]}...")
    scan_products(query_range, print_products)