from pprint import pprint
import boto3


def put_product(title, sku, description, price, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')
    response = table.put_item(
       Item={
            'sku': sku,
            'title': title,
            'info': {
                'description': description,
                'price': price
            }
        }
    )
    return response


if __name__ == '__main__':
    product_resp = put_product("The Big New product", 23434433,
                           "Nothing happens at all.", 54)
    print("Put product succeeded:")
    pprint(product_resp, sort_dicts=False)