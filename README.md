\# 📚 Smart Study Generator Agent



An AI-powered, agentic study assistant that transforms study materials into personalized, structured, and exam-ready learning resources.



\---



\## 🎯 Problem Statement



Students today have study materials scattered across lecture notes, textbooks, research papers, and online resources. This makes it difficult to:



\* Understand large amounts of content

\* Identify important exam topics

\* Create effective revision materials

\* Plan study time efficiently

\* Identify weak areas

\* Track learning progress



The \*\*Smart Study Generator Agent\*\* addresses this problem by analyzing uploaded study material and generating personalized learning resources while providing an interactive study-progress dashboard.



\---



\## 💡 Solution



The system combines \*\*Langflow\*\*, \*\*Google Gemini\*\*, and \*\*Streamlit\*\* to create an AI-powered study assistant.



The system analyzes uploaded study material and generates:



\* 📚 Simple Summary

\* 🔑 Key Concepts

\* ⭐ Important Topics

\* 📝 Important Exam Questions with Answers

\* 🧠 Flashcards

\* 📅 Personalized 3-Day Study Plan

\* 🎯 Weak-Area Check

\* ⚡ Quick Revision Points

\* 🧪 Practice Quiz

\* 📊 Self-Assessment

\* 📈 Performance Forecast

\* 🤖 AI Study Recommendations



A separate Streamlit dashboard allows students to visualize their study progress, topic performance, revision priorities, quiz performance, and study recommendations.



\---



\## ✨ Key Features



\### 📖 AI Study Material Generation



Upload a study PDF and automatically generate structured learning resources.



\### 🧠 Personalized Learning



The agent organizes the material according to exam importance and recommends a study sequence.



\### 📝 Exam Preparation



Generates important questions, answers, flashcards, practice quizzes, and quick-revision points.



\### 🎯 Weak-Area Detection



Identifies topics that require additional revision based on the provided material and dashboard performance data.



\### 📅 Study Planning



Creates a personalized 3-day study plan with prioritized topics and revision activities.



\### 📊 Interactive Progress Dashboard



The Streamlit dashboard provides:



\* Overall progress

\* Topics completed

\* Quiz score

\* Study hours

\* Confidence level

\* Topic performance

\* Weak areas

\* Revision priority

\* 3-day study plan

\* Quiz performance

\* AI recommendations

\* Study streak



\---



\## 🔄 Langflow Workflow



```text

Study Material / PDF

&#x20;       ↓

&#x20;   Read File

&#x20;       ↓

&#x20;     Prompt

&#x20;       ↓

&#x20;Google Gemini

&#x20;       ↓

&#x20;  Chat Output

&#x20;       ↓

Structured Study Resources

```



\---



\## 🏗️ System Architecture



```text

&#x20;                ┌─────────────────────┐

&#x20;                │   Study Material    │

&#x20;                │       PDF           │

&#x20;                └──────────┬──────────┘

&#x20;                           ↓

&#x20;                ┌─────────────────────┐

&#x20;                │      Langflow       │

&#x20;                │    Read File        │

&#x20;                └──────────┬──────────┘

&#x20;                           ↓

&#x20;                ┌─────────────────────┐

&#x20;                │   Study Generator   │

&#x20;                │       Prompt        │

&#x20;                └──────────┬──────────┘

&#x20;                           ↓

&#x20;                ┌─────────────────────┐

&#x20;                │    Google Gemini    │

&#x20;                │      LLM Model      │

&#x20;                └──────────┬──────────┘

&#x20;                           ↓

&#x20;                ┌─────────────────────┐

&#x20;                │  Study Resources    │

&#x20;                │ Summary / Questions │

&#x20;                │ Flashcards / Plan   │

&#x20;                │ Quiz / Revision     │

&#x20;                └──────────┬──────────┘

&#x20;                           ↓

&#x20;                ┌─────────────────────┐

&#x20;                │ Streamlit Dashboard │

&#x20;                │ Progress \& Analysis │

&#x20;                └─────────────────────┘

```



\---



\## 🛠️ Technology Stack



| Technology    | Purpose                     |

| ------------- | --------------------------- |

| Langflow      | AI workflow orchestration   |

| Google Gemini | Large Language Model        |

| Streamlit     | Interactive study dashboard |

| Python        | Dashboard development       |

| PDF           | Study material input        |

| Git \& GitHub  | Version control             |



\---



\## 📁 Project Structure



```text

Smart-Study-Generator/

│

├── dashboard/

│   └── app.py

│

├── flow/

│   └── smart-study-generator.json

│

├── screenshots/

│   ├── langflow-workflow.png

│   ├── langflow-workflow-output1.png

│   ├── langflow-workflow-output2.png

│   ├── langflow-workflow-output3.png

│   ├── langflow-workflow-output4.png

│   ├── langflow-workflow-output5.png

│   ├── langflow-workflow-output6.png

│   ├── langflow-workflow-output7.png

│   ├── dashboard1.png

│   ├── dashboard2.png

│   ├── dashboard3.png

│   ├── dashboard4.png

│   └── dashboard5.png

│

├── .gitignore

└── README.md

```



\---



\## 🚀 How to Run



\### 1. Run the Langflow Agent



Start Langflow and open the Langflow interface.



Open the \*\*Smart Study Generator\*\* flow.



Upload a study PDF through the \*\*Read File\*\* component and run the flow.



The generated study resources will appear through the Chat Output.



\### 2. Run the Dashboard



Activate the Python virtual environment:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



Set the following environment variables to reduce resource usage:



```powershell

$env:OPENBLAS\_NUM\_THREADS="1"

$env:OMP\_NUM\_THREADS="1"

$env:MKL\_NUM\_THREADS="1"

```



Start Streamlit:



```powershell

streamlit run dashboard\\app.py

```



The interactive study dashboard will open in the browser.



\---



\## 🔐 API Key Security



The Google Gemini API key is \*\*not stored in this repository\*\*.



Users should configure their own API key inside their Langflow environment.



Never commit API keys, passwords, or other credentials to GitHub.



\---



\## 📸 Screenshots



\### Langflow Workflow



!\[Langflow Workflow](screenshots/langflow-workflow.png)



\### Langflow Generated Output



!\[Study Output 1](screenshots/langflow-workflow-output1.png)



!\[Study Output 2](screenshots/langflow-workflow-output2.png)



\### Study Dashboard



!\[Dashboard Overview](screenshots/dashboard1.png)



!\[Dashboard Performance](screenshots/dashboard2.png)



!\[Dashboard Revision](screenshots/dashboard3.png)



!\[Dashboard Study Plan](screenshots/dashboard4.png)



!\[Dashboard Recommendations](screenshots/dashboard5.png)



\---



\## 🎓 Example Generated Resources



For a provided study material, the agent can generate:



1\. Simple explanation of the material

2\. Important concepts

3\. High/Medium/Low priority topics

4\. Exam questions and answers

5\. Flashcards

6\. Personalized study plan

7\. Weak-area analysis

8\. Quick revision points

9\. Practice MCQ quiz

10\. Self-assessment checklist

11\. Revision priority recommendations



\---



\## 🔮 Future Enhancements



The project can be extended with:



\* 🎤 Voice-based study queries

\* 🖼️ Image and textbook-page understanding

\* 📚 Multiple document upload

\* 🔎 Retrieval-Augmented Generation (RAG)

\* 🗺️ Automatic concept-map generation

\* 📈 Persistent student progress tracking

\* 🧠 Adaptive difficulty levels

\* 📊 Historical performance analysis

\* 🔔 Exam-focused predictive alerts

\* 🎯 Syllabus and previous-year-question analysis



\---



\## 👩‍💻 Project Goal



The goal of the \*\*Smart Study Generator Agent\*\* is to make exam preparation more organized, personalized, and efficient by combining generative AI with interactive learning analytics.



\---



\## 📌 Project Status



\*\*Current Status:\*\* Working Prototype



\*\*Core AI Workflow:\*\* Implemented



\*\*Study Dashboard:\*\* Implemented



\*\*GitHub Repository:\*\* Complete



