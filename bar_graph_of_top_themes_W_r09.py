import pandas as pd
import matplotlib.pyplot as plt

# Load the sets.csv and themes.csv files into DataFrames
sets_file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\sets.csv'
themes_file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\themes.csv'

sets_df = pd.read_csv(sets_file_path)
themes_df = pd.read_csv(themes_file_path)

# Get the count of sets per theme_id
set_theme_count = sets_df["theme_id"].value_counts()

# Merge the set_theme_count with the themes_df to get theme names
merged_df = pd.DataFrame({'theme_id': set_theme_count.index, 'set_count': set_theme_count.values})
merged_df = merged_df.merge(themes_df[['id', 'name']], left_on='theme_id', right_on='id')

# Select the top 10 themes
top_10_themes = merged_df.head(10)

# Plot the data as a bar graph
plt.figure(figsize=(12, 8))
plt.bar(top_10_themes['name'], top_10_themes['set_count'], color='skyblue')
plt.title('Top 10 LEGO Themes by Number of Sets')
plt.xlabel('Theme Name')
plt.ylabel('Number of Sets')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()
