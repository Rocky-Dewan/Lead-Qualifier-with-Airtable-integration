# Lead-Qualifier-with-Airtable-integration
This project is an AI-driven lead classification and entity extraction tool designed to streamline real estate workflows. It uses Cohere's  (LLMs) to classify leads and extract structured information (location, intent, budget) from free-text messages. The processed leads are saved in a CSV file and automatically pushed to an Airtable base.


# 🧠 AI-Powered Lead Qualifier with Airtable Integration

This project is an AI-driven lead classification and entity extraction tool designed to streamline real estate workflows. It uses Cohere's large language models (LLMs) to classify leads (`hot`, `warm`, `cold`) and extract structured information (location, intent, budget) from free-text messages. The processed leads are saved in a CSV file and automatically pushed to an Airtable base.

---

## 📌 Features

- 🔍 Classifies real estate leads based on message content
- 🧠 Extracts structured entities: location, budget, intent
- 📤 Saves qualified leads to `qualified_leads.csv`
- 📊 Syncs results directly to an Airtable table using the Airtable API (with PAT support)
- 🌐 Uses Cohere's `generate()` API for natural language tasks

---

## 🎯 Goal

To automate the initial lead triage process in real estate marketing using AI and push structured data to Airtable for easy tracking, filtering, and follow-up.

---

## 🛠️ Technologies Used

- [Python 3.10+](https://www.python.org/)
- [Cohere API](https://docs.cohere.com/)
- [Airtable (with Personal Access Token)](https://airtable.com/developers/web/api/introduction)
- [Pandas](https://pandas.pydata.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [pyairtable](https://github.com/gtalarico/pyairtable)

---

## 📁 Folder Structure
lead_qualifier/
├── main.py
├── leads.json
├── qualified_leads.csv (auto-generated)
├── .env
├── requirements.txt
└── README.md

## 📦 Setup Instructions

1. **Clone the repository**


git clone https://github.com/your-username/lead-qualifier.git
cd lead-qualifier


Set up environment variables

Create a .env file in the root directory with:

.env

COHERE_API_KEY=your_cohere_key
AIRTABLE_PAT=your_airtable_pat
AIRTABLE_BASE_ID=your_airtable_base_id
AIRTABLE_TABLE_NAME=Your Airtable name 

Run the project
bash

python main.py

Sample Output
qualified_leads.csv: Contains structured leads with extracted insights

<img width="1940" height="881" alt="image" src="https://github.com/user-attachments/assets/d60b27b0-3795-4837-b00a-a99652ee3c58" />


Airtable: Your configured base will be updated with each lead record
<img width="1740" height="631" alt="image" src="https://github.com/user-attachments/assets/99b254e8-8803-4041-a49e-da03f7794f9c" />



🐛 Known Issues
Issue	Description
INVALID_MULTIPLE_CHOICE_OPTIONS	Airtable column is a dropdown (Single Select) and does not include the value (e.g., "Melbourne"). Make sure the field options match exactly.
Field cannot accept the value	Happens when a column like "Budget" expects a number but gets a string ("$500,000"). Convert to Single line text in Airtable.
Model not found	Use command-xlarge-nightly for Cohere models, and ensure your API key has access.

✅ Airtable Field Type Suggestions
Field	Type	Required Options (if dropdown)
Name	Single line text	-
Budget	Single line text	-
Message	Long text	-
Classification	Single select	hot, warm, cold
Location	Single select	Melbourne, Sydney, Perth, etc.
Intent	Single line text	-
Extracted Budget	Single line text	-

🤝 Contributing
Feel free to fork, modify, or contribute pull requests to improve this tool for other real estate and marketing teams.

📄 License
This project is licensed under the MIT License. See LICENSE for details.

🙋‍♂️ Contact
Made by [Rocky Dewan]
Email: [dewanrocky250@gmail.com]
Portfolio: [[yourwebsite.com](http://rocky-dewan.github.io/-Rockyfolio/)]
