from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_product(title, sku, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')

    try:
        response = table.delete_item(
            Key={
                'sku': sku,
                'title': title
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("Attempting a delete...")
    delete_response = delete_product("The Big New product", 23434433)
    if delete_response:
        print("Delete product succeeded:")
        pprint(delete_response, sort_dicts=False)