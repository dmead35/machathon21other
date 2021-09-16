from decimal import Decimal
from pprint import pprint
import boto3


def update_product(title, sku, price, description, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')

    response = table.update_item(
        Key={
            'sku': sku,
            'title': title
        },
        UpdateExpression="set info.price=:p, info.description=:d",
        ExpressionAttributeValues={
            ':p': Decimal(price),
            ':d': description
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_product(
        "The Big New product", 23434433, 47.0, "Everything happens all at once.")
    print("Update product succeeded:")
    pprint(update_response, sort_dicts=False)