import os
from google.cloud import storage

def get_gcp_dataset(project_name, bucket_name, source_path, destination_filename):
    # project_name = "your-project-name"
    # bucket_name = "your-bucket-name"
    # source_path = "storage-object-name"
    # destination_filename = "file-name"
    destination_path = os.path.join('data', destination_filename)

    if not os.path.exists('data'):
        os.makedirs('data')

    if os.path.isfile(destination_path):
        print("[PROJECT INFO] {} already exists, skipping download...".format(destination_path))
        return

    client = storage.Client(project_name)
    bucket = client.get_bucket(bucket_name)

    bucket.get_blob(source_path).download_to_filename(destination_path)

    print("[PROJECT INFO] Blob {} downloaded to {}.".format(source_path, destination_path))

    return 0
