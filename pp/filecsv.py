import csv

csv_filename = 'example.csv'

# Writing to a CSV file
csv_file = open(csv_filename, 'w', newline='')  # Open the file in write mode
csv_writer = csv.writer(csv_file)


csv_writer.writerow(['Name', 'Age', 'City'])

# Write data
csv_writer.writerow(['Test', 30, 'City1'])
csv_writer.writerow(['New', 25, 'City2'])
csv_writer.writerow(['One', 35, 'City1'])

csv_file.close()  

# Reading from a CSV file
csv_file = open(csv_filename, 'r')  
csv_reader = csv.reader(csv_file)

print("Content of the CSV file:")
for row in csv_reader:
    print(row)  # Print each row

csv_file.close()  # Close the file