import os
import json

def filter_annotation_by_folder(annotation_dict, video_folder):
    filtered_annotation = {video_name: data for video_name, data in annotation_dict.items() if os.path.exists(os.path.join(video_folder, f"{video_name}.mp4"))}
    return filtered_annotation

# Example Usage:
annotation_path = 'dataset/annotation_dict.json'  # Replace with the actual path to your annotation file
video_folder = 'dataset/examples'  # Replace with the actual path to your video folder

# Load existing annotation data
with open(annotation_path, 'r') as f:
    annotation_dict = json.load(f)

# Filter annotation data based on video presence
filtered_annotation = filter_annotation_by_folder(annotation_dict, video_folder)

# Save the filtered annotation back to the file
filtered_annotation_path = 'dataset/filtered_annotation.json'  # Replace with the desired path for the filtered annotation file
with open(filtered_annotation_path, 'w') as f:
    json.dump(filtered_annotation, f, indent=2)

print(f"Filtered annotation data saved to {filtered_annotation_path}")
