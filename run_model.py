import pandas as pd
import pickle
from ticket_recommender import TicketRecommender

# 📥 Step 1: Load your dataset
df = pd.read_csv('Customer_support_data.csv')

# 🧠 Step 2: Create model instance with enriched context
recommender = TicketRecommender(
    data=df,
    text_column='Customer Remarks',
    context_columns=['Product_category'],  # These must match actual column names in your CSV
    output_columns=['Customer Remarks', 'Sub-category']     # You can add more columns if you want richer output
)

# 💾 Step 3: Save the model as pickle for use in Flask or other services
with open("recommender.pkl", "wb") as f:
    pickle.dump(recommender, f)

print("✅ Model training and saving complete.")
