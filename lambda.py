from trimtr.trimmer import Trimmer
import json


def handler(event, context):
    source_text = event["body"]
    print("source_text:", source_text)
    trimmer = Trimmer.get_instance()
    result = trimmer.trim(source_text)
    print("result:", repr(result))
    return {
        "statusCode": 200,
        "body": json.dumps({"text": result}),
    }
