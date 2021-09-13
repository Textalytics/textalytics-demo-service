import uvicorn
from fastapi import FastAPI, HTTPException
from textalytics_aws.aws_entity_recognition import AwsEntityRecognizer
from textalytics_azure.azure_entity_recognition import AzureEntityRecognizer
from textalytics_core import resources
from textalytics_gcp.gcp_entity_recognition import GcpEntityRecognizer
from textalytics_hosted.textalytics_entity_recognition import TextalyticsEntityRecognizer

app = FastAPI(
    title="Textalytics",
    description="Text Analytics APIs",
    version="v1.0",
)

PROVIDERS = ['gcp', 'aws', 'azure', 'textalytics']

@app.post("/extract-entities", response_model=resources.EntityRecognizerOutput)
async def extract_entities(text_input: resources.TextInput):
    provider = text_input.provider
    if provider in PROVIDERS:
        entity_recognizer = None
        if provider == "gcp":
            entity_recognizer = GcpEntityRecognizer()
        elif provider == "aws":
            entity_recognizer = AwsEntityRecognizer()
        elif provider == "azure":
            entity_recognizer = AzureEntityRecognizer()
        elif provider == "textalytics":
            entity_recognizer = TextalyticsEntityRecognizer()
        else:
            raise HTTPException(status_code=404, detail="provider needs to be one of " + ",".join(PROVIDERS))

        return entity_recognizer.recognize_entities(text_input)
    else:
        raise HTTPException(status_code=404, detail="provider needs to be one of " + ",".join(PROVIDERS))


if __name__ == "__main__":
    uvicorn.run(app)
