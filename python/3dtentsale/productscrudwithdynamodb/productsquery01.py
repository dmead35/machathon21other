import boto3
from boto3.dynamodb.conditions import Key


def query_products(sku, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')
    response = table.query(
        KeyConditionExpression=Key('sku').eq(sku)
    )
    return response['Items']


if __name__ == '__main__':
    query_sku = 23474089
    print(f"products from sku {query_sku}")
    products = query_products(query_sku)
    for product in products:
        print(product['sku'], ":", product['title'])