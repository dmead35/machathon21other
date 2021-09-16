from decimal import Decimal
import json
import boto3


def load_products(products, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')
    for product in products:
        sku = int(product['sku'])
        title = product['title']
        print("Adding product:", sku, title)
        table.put_item(Item=product)


if __name__ == '__main__':
    with open("productdata.json") as json_file:
        product_list = json.load(json_file, parse_float=Decimal)
    load_products(product_list)