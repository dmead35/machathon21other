from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_product(title, sku, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')

    try:
        response = table.get_item(Key={'sku': sku, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    product = get_product("The Big New product", 23434433,)
    if product:
        print("Get product succeeded:")
        pprint(product, sort_dicts=False)