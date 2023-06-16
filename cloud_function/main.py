def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print("HOLAAA FUNCIONAAA VAMOSSS!!!!")
    file = event
    print(f"Processing file: {file['name']}.")
