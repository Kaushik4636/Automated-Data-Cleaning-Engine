from cleaner import DataCleaner

# Initialize with your CSV file
engine = DataCleaner('titanic.csv')

# Run the Titanic-specific clean
engine.clean_titanic()

# Save the final file
engine.save_data('titanic_cleaned_v2.csv')