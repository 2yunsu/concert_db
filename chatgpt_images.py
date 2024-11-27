from openai import OpenAI
import csv
import re

client = OpenAI(
    api_key="",
)

# File paths
input_csv_file = "concert_db.csv"  # Replace with your input CSV file path
output_csv_file = "concert_db_added.csv"  # Replace with your desired output CSV file path

def clean_quotes(field):
    """
    Cleans up extra or nested quotes in a string and ensures only one pair of double quotes around the field.
    """
    # Remove leading/trailing spaces and extra quotes
    field = field.strip().strip('"').replace('"""', '"')
    # Ensure the field is wrapped with a single pair of quotes
    return f'{field}'

def parse_response(content):
    try:
        # Strip leading and trailing whitespace
        content = content.strip()

        # Remove the wrapping backticks and newlines
        if content.startswith("```") and content.endswith("```"):
            content = content[3:-3].strip()

        # Split the content by commas and trim whitespace from each field
        fields = [field.strip() for field in content.split(",", maxsplit=3)]

        # Ensure there are exactly 4 fields (공연자, 공연 장소, 공연 시기, 공연 내용)
        if len(fields) == 4:
            performer, venue, date, description = fields
            # Clean up quotes in each field
            performer = clean_quotes(performer)
            venue = clean_quotes(venue)
            date = clean_quotes(date)
            description = clean_quotes(description)

            return performer, venue, date, description
    except Exception as e:
        print(f"Error parsing response: {e}")
    
    # Return None for all fields if parsing fails
    return None, None, None, None

# Open the input CSV file and prepare the output CSV
with open(input_csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row

    # Add new columns to the header for the parsed response details
    output_header = header + ["공연자", "공연 장소", "공연 시기", "공연 내용"]

    # Open the output CSV file for writing
    with open(output_csv_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(output_header)  # Write the updated header

        # Iterate through each row in the input CSV
        for row in reader:
            if len(row) < 2:
                continue  # Skip rows with insufficient columns
            
            image_url = row[1]  # Assuming the URL is in the second column

            try:
                # Make the API request
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "포스터의 공연자, 공연 장소, 공연 시기, 공연 내용만 csv 파일 형식으로 ""를 각 내용 양 끝에 붙여 순서대로 나열하고 다른 말은 하지마."},
                                {
                                    "type": "image_url",
                                    "image_url": {"url": image_url},
                                },
                            ],
                        }
                    ],
                    max_tokens=100,
                )
                # Extract the response content
                response_content = response.choices[0].message.content
                print("response_content: ", response_content)
                # Parse the content to extract details
                performer, venue, date, description = parse_response(response_content)
            except Exception as e:
                # Handle errors gracefully and log the issue
                performer, venue, date, description = None, None, None, None
                print(f"Error processing URL {image_url}: {e}")

            # Append the extracted details to the current row
            output_row = row + [performer, venue, date, description]
            # Write the updated row to the output CSV
            # breakpoint()
            writer.writerow(output_row)

print(f"Responses have been saved to {output_csv_file}")