input_path="data/raw_data.txt"
output_path="data/processed_data.txt"

with open(input_path, 'r') as f:
    lines = f.readlines()


    processed= [line.upper() for line in lines]


    with open (output_path, "w") as f:
        f.writelines(processed)

        print("Processing complete. Processed data saved to", output_path)