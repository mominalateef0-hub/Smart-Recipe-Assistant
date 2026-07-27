# Smart-Recipe-Assistant
A Smart Recipe Assistant App
# 🍳 Smart Mess & Pantry Recipe Assistant

An AI-powered web application that turns whatever ingredients you have on hand into simple, ready-to-cook local recipes — built for students, hostel/mess residents, and home cooks who want to avoid extra grocery runs.

---

## 🌐 Live Demo
[Click Here to Try the App](https://mb5y2n476qqmnb55.streamlit.app)

---

## 📌 Problem & Solution

**Problem:**
Students living in hostels or mess accommodations — and home cooks in general — frequently end up with a random, limited set of ingredients in their fridge or pantry. Figuring out what to actually cook with what's available, without buying more groceries, is a repetitive daily hassle. Search engines and generic recipe sites are built around specific dish names, not around "here's what I have, what can I make?"

**Target Audience:**
University students, hostel/mess residents, budget-conscious home cooks, and anyone who wants a quick meal plan built around leftover ingredients.

**Solution:**
This app lets a user simply list the ingredients they currently have and pick a meal type. An AI model then generates two realistic, locally-relevant recipes tailored to those exact ingredients, including timing, any extra basic staples needed, clear step-by-step instructions, and a chef's tip — all in one click.

---

## ✨ Features

- **Ingredient-based input** — type ingredients in plain, free-form text (e.g., "eggs, potatoes, tomatoes, rice").
- **Meal type filter** — choose from Any, Quick Breakfast, Lunch/Dinner, or Hostel/Mess Special.
- **AI-generated recipes** — returns exactly 2 recipes matched to the given ingredients.
- **Structured recipe output** — each recipe includes prep/cooking time, extra staples required, numbered instructions, and a chef's tip.
- **Clean Markdown formatting** — results are easy to read directly in the browser.
- **Secure key handling** — the Gemini API key is read from an environment variable, never hard-coded into the source.
- **Graceful fallback** — if no environment variable is set, the app prompts for the key via a sidebar input instead of crashing.

---

## 🤖 AI Integration & System Prompt

This app is powered by **Google's Gemini API**, currently configured to use `gemini-3.5-flash`.

**System Prompt Used:**
> "You are an expert chef specializing in simple, budget-friendly South Asian household and hostel/mess meals. Given a list of ingredients and a meal type preference, return 2 realistic recipes that use primarily those ingredients (assuming basic spices, oil, and water are available). For each recipe, include prep and cooking time, any additional basic staples needed, step-by-step instructions, and a quick chef's tip — formatted cleanly in Markdown."

This prompt was written to keep the AI's output focused, practical, and locally relevant rather than generic — it constrains the recipes to what's realistically achievable with a typical hostel/mess kitchen setup.

---

## 🛠️ Tech Stack & Tools

| Layer | Technology |
|---|---|
| Frontend & Backend | Python, Streamlit |
| AI Model / API | Google Gemini API (`gemini-3.5-flash`) |
| Deployment | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

## 📸 Screenshots

<img width="1024" height="588" alt="image" src="https://github.com/user-attachments/assets/b3d6cec8-567f-4226-a5bd-b4a3ed48b5f4" />
<img width="512" height="334" alt="image" src="https://github.com/user-attachments/assets/1f4b54e0-bf49-4e99-ab32-eacd37721f61" />
<img width="1024" height="863" alt="image" src="https://github.com/user-attachments/assets/a68cbc42-6cc7-40a3-a9e8-7d8186994bfe" />

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-mess-recipe-assistant.git
   cd smart-mess-recipe-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Gemini API key as an environment variable:
   ```bash
   export GEMINI_API_KEY=your_key_here
   ```
   *(On Windows, use `set GEMINI_API_KEY=your_key_here`)*

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the local URL Streamlit prints in your terminal (usually `http://localhost:8501`).

---

## ☁️ Deployment Notes

The app is deployed on **Streamlit Community Cloud**:
1. Repository connected via GitHub.
2. Main file set to `app.py`.
3. `GEMINI_API_KEY` added as a secret under **Advanced Settings** — never committed to the repository itself.

---

## 🔒 Security Note

The API key is never stored in the codebase. It is read via `os.getenv("GEMINI_API_KEY")`, and on Streamlit Cloud it is stored securely as a secret/environment variable rather than in `app.py` or any config file pushed to GitHub.

---

## 📄 Project Structure

```
smart-mess-recipe-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation (this file)
└── screenshots/        # App screenshots for documentation
```

---

## 🙋 Author

Built as a course project demonstrating AI integration into a working, deployed web application using a custom system prompt.
