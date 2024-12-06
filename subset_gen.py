import json
import random
import os
import argparse

def main(input_file, output_dir, dividing_factor):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r') as f:
        data = json.load(f)

    grouped_data = {}
    for entry in data:
        image_id = entry['image_id']
        if image_id not in grouped_data:
            grouped_data[image_id] = []
        grouped_data[image_id].append(entry)

    unique_image_ids = list(grouped_data.keys())
    sample_size = max(1, len(unique_image_ids) // dividing_factor)
    selected_image_ids = random.sample(unique_image_ids, sample_size)

    subset_data = []
    for image_id in selected_image_ids:
        subset_data.extend(grouped_data[image_id])

    # output file name
    input_file_name = os.path.basename(input_file)
    input_file_base, input_file_ext = os.path.splitext(input_file_name)
    subset_file_name = f"{input_file_base}_{1}_{dividing_factor}th{input_file_ext}"
    subset_file_path = os.path.join(output_dir, subset_file_name)

    # save ot new json
    with open(subset_file_path, 'w') as f:
        json.dump(subset_data, f, indent=2)

    print(f"Subset data saved to: {subset_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a subset of a JSON file grouped by 'image_id'.")
    parser.add_argument("--input_file", help="Path to the input JSON file.")
    parser.add_argument("--output_dir", default = "./subset_jsons/", help="Path to the directory where the output JSON file will be saved.")
    parser.add_argument("--dividing_factor", type=int, default=10,
                        help="The dividing factor for the subset size (default is 10, resulting in a 1/10th subset).")
    args = parser.parse_args()

    main(args.input_file, args.output_dir, args.dividing_factor)
