from huggingface_hub import HfApi
import os
api = HfApi(token=os.getenv("TOKEN"))
api.upload_folder(
    folder_path="./outputs/train/example_piper",
    repo_id="gauravpradeep/bottle_task",
    repo_type="model",
)