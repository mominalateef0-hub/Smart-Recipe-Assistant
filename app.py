import streamlit as st
import google.generativeai as genai
import os

# Page Configuration
st.set_page_config(page_title="Smart Mess & Recipe Assistant", page_icon="🍳", layout="centered")

st.title("🍳 Smart Mess & Pantry Recipe Assistant")
st.write("Got random ingredients in your fridge/pantry? Type them below, and AI will give you delicious local recipe options!")

# Get API key from Environment Variable, fallback to sidebar input
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.info("💡 Enter your Gemini API key in the sidebar to get started.", icon="🔑")
    api_key = st.sidebar.text_input("Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # User Inputs
    ingredients = st.text_area(
        "List your available ingredients (e.g., eggs, potatoes, tomatoes, rice, onions):",
        height=120
    )
    meal_type = st.selectbox(
        "Select Meal Type:",
        ["Any", "Quick Breakfast", "Lunch/Dinner", "Hostel/Mess Special (Budget & Fast)"]
    )

    if st.button("Find Recipes 👨‍🍳", use_container_width=True):
        if not ingredients.strip():
            st.warning("Please enter at least a few ingredients!")
        else:
            with st.spinner("Cooking up recipe ideas..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")

                    # System prompt guiding the AI's behavior
                    system_prompt = """
                    You are an expert chef specializing in simple, budget-friendly South Asian
                    household and hostel/mess meals.

                    Given a list of ingredients and a meal type preference, return exactly 2
                    realistic local recipes that can be made primarily using the provided
                    ingredients (assuming basic spices, oil, and water are available).

                    For each recipe, provide:
                    - ⏱️ Prep & Cooking Time
                    - 🧂 Additional Basic Staples Needed (if any)
                    - 📝 Step-by-step, simple cooking instructions
                    - 💡 A quick chef's tip for better taste

                    Format the entire response cleanly using Markdown.
                    """

                    full_prompt = (
                        f"{system_prompt}\n\n"
                        f"Ingredients: {ingredients}\n"
                        f"Meal Type: {meal_type}"
                    )
                    response = model.generate_content(full_prompt)

                    st.markdown("---")
                    st.markdown(response.text)

                except Exception as e:
                    st.error(f"Something went wrong: {e}")
else:
    st.warning("Please provide a Gemini API key to use this app.")
