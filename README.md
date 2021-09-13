# About

FastAPI based implementation of a simple demo service that invokes textalytics adapters based on "provider"

`python main.py`

This runs the service on port 8000

# Docs

* http://localhost:8000/docs: OpenAPI interface
* http://localhost:8000/redocs: ReDocs interface

# Example Invocation

    curl -X 'POST' \
      'http://localhost:8000/extract-entities' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "source_text": "Dr. Levy, a research associate at the University of Texas at Austin’s Institute for Geophysics, is studying the climate history of the dry valleys of Antarctica by analyzing buried ice sheets that have been frozen since the last ice age and are beginning to thaw.",
      "source_language": "en",
      "provider": "gcp"
    }'