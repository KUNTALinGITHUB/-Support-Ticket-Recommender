# -Support-Ticket-Recommender
An intelligent ticket recommendation system that uses Sentence-BERT to semantically match incoming customer complaints with historical support data. Perfect for improving resolution time, auto-routing, and enriching agent decision-making.


🧠 Support Ticket Recommendation System
An intelligent ticket recommendation system that uses Sentence-BERT to semantically match incoming customer complaints with historical support data. Perfect for improving resolution time, auto-routing, and enriching agent decision-making.


🧠 Benefits for Support Associates

1. Faster Ticket Resolution
Associates can instantly view similar past complaints and how they were resolved.
Reduces time spent searching through old tickets manually.
2. Smart Auto-Triage
The system suggests relevant categories and channels based on the complaint.
Helps route tickets to the right team or department automatically.
3. Improved Decision-Making
Associates get context from historical data, making it easier to decide on the next steps.
Reduces guesswork and improves consistency in responses.
4. Real-Time Suggestions
As the associate types a complaint, the system autocompletes and suggests similar issues.
Speeds up data entry and ensures standardized language.
5. Contextual Matching
Complaints are matched not just by keywords but by semantic meaning using SBERT.
This means even if the wording is different, similar issues are still identified.
6. Multi-Channel & Product Awareness
Associates can filter or view tickets based on product category or support channel.
Adds context to the complaint and helps tailor responses.

📊 Use Case Examples
Call Center Agents: Quickly find similar tickets while on a call.
Email Support Teams: Auto-suggest responses based on past emails.
Internal IT Helpdesks: Categorize and resolve internal employee issues faster.
BPOs: Train new agents with examples of past resolutions.

🚀 Features
🔍 Suggests similar past support tickets for faster triaging

🧠 Uses pre-trained SBERT embeddings for semantic matching

📦 Pre-trained model saved as .pkl for instant inference

🖥️ Flask-based API with real-time response

🌐 Frontend: HTML interface with autocomplete and selection

📁 Supports product categories and channels for contextual tuning

📊 Use Cases
Customer support portals 🧑‍💻

Helpdesk automation 🔧

Agent assist tools for BPOs 🤖

Internal triaging and categorization workflows 📋

⚙️ Tech Stack
Component	Details
Model	SBERT (all-MiniLM-L6-v2)
Language	Python
Backend	Flask
Frontend	HTML, JS (vanilla), CSS
Dataset	CSV (Customer_support_data.csv)
Embedding Storage	Pickle (recommender.pkl)
📁 Project Structure
recommendation_system/
├── app.py                     # Flask API and routing
├── run_model.py              # Generates and saves SBERT model
├── ticket_recommender.py     # Core class for matching
├── recommender.pkl           # Saved model for inference
├── Customer_support_data.csv # Support ticket dataset
└── static/
    └── index.html            # Interactive frontend
🔧 Setup & Installation

~bash
git clonehttps://github.com/KUNTALinGITHUB/-Support-Ticket-Recommender.git
cd -Support-Ticket-Recommender.git
pip install -r requirements.txt
Make sure you have Python ≥ 3.7 and install dependencies like Flask, pandas, scikit-learn, and sentence-transformers.

🛠️ Generate Model
~bash
python run_model.py
This will read your dataset and generate recommender.pkl using SBERT embeddings.

🌐 Run the Flask Server
~bash
python app.py
Visit: http://127.0.0.1:5000/ You’ll see the user interface where users can input a complaint and get matched suggestions.

📨 API Endpoints
/recommend POST
json
{
  "customer_remark": "unable to connect to WiFi",
  "Product_category": "Electronics",
  "top_n": 5
}
Returns a list of similar tickets in JSON format.

/autocomplete POST
Used by the frontend to fetch real-time suggestions.

json
{ "query": "can't login" }
Returns a list of 5 similar ticket remarks.

💻 Frontend Demo
Type a remark → Get live suggestions

Select category and result count

View recommended remarks and categories

Smooth interaction powered by JS and Flask

🧪 Sample Categories
LifeStyle

Electronics

Mobile

Home Appliances

Furniture

Books & General merchandise

GiftCard

Affiliates

🏁 Roadmap Ideas
[ ] Add resolution notes & ticket status

[ ] Include time-based filtering

[ ] Deploy via Docker & serve with Gunicorn

[ ] UI dashboard (Streamlit or React)

🤝 Contributing
Pull requests are welcome! For major changes, open an issue to discuss what you’d like to modify. Contributions to frontend polish or model tuning are especially appreciated!


https://github.com/user-attachments/assets/a821a19e-fe7b-49dd-bff1-f94ae03289ee

