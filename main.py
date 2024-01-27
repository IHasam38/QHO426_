
import csv

def read_disneyland_reviews():
    file_path = "/Users/macbook/Downloads/project_template (3)/data/disneyland_reviews.csv"
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None

# Example usage
disneyland_reviews_data = read_disneyland_reviews()

if disneyland_reviews_data is not None:
    # Display or use the data as needed
    for row in disneyland_reviews_data[:200]:  # Display the first few rows
        print(row)
else:
    print(f"Failed to read '{file_path}'.")
