import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, file_path):
        """Load data and treat 'Unknown' as missing."""
        self.df = pd.read_csv(file_path)
        # Convert any 'Unknown' strings to actual NaN so Python can fix them
        self.df.replace('Unknown', np.nan, inplace=True)
        print(f"Loaded {len(self.df)} passengers for processing.")

    def clean_titanic(self):
        """Custom cleaning sequence for your specific columns."""
        
        # 1. Handle missing Age (fill with median)
        self.df['Age'] = self.df['Age'].fillna(self.df['Age'].median())
        
        # 2. Drop Cabin (too many 'Unknowns' to be useful)
        if 'Cabin' in self.df.columns:
            self.df.drop(columns=['Cabin'], inplace=True)
            
        # 3. Handle Embarked (fill missing with most common, then convert to numbers)
        self.df['Embarked'] = self.df['Embarked'].fillna(self.df['Embarked'].mode()[0])
        embarked_mapping = {'S': 0, 'C': 1, 'Q': 2}
        self.df['Embarked'] = self.df['Embarked'].map(embarked_mapping)

        # 4. Convert Sex to binary (male=0, female=1)
        self.df['Sex'] = self.df['Sex'].map({'male': 0, 'female': 1})

        # 5. Remove 'Identifer' columns that aren't useful for math
        cols_to_remove = ['PassengerId', 'Name', 'Ticket']
        self.df.drop(columns=[c for c in cols_to_remove if c in self.df.columns], inplace=True)
        
        print("Cleaning complete: Text converted to numbers and noise removed.")

    def save_data(self, output_name="titanic_ready.csv"):
        self.df.to_csv(output_name, index=False)
        print(f"Saved to {output_name}. Ready for Data Science models!")