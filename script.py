import google.generativeai as genai
from PIL import ImageGrab
import tkinter as tk

# --- 1. SETUP API ---
# REPLACE THIS with your actual API key
API_KEY = "AQ.Ab8RN6LK12Xm2J6acsx190SP2rQoBaYeZ3l02jaEDZhfQ_PJMA" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def show_transparent_popup(answer_text):
    """Creates a 7-second transparent popup with the answer."""
    root = tk.Tk()
    root.overrideredirect(True)  # Removes window borders
    root.attributes('-alpha', 0.85)  # 85% opacity
    root.attributes('-topmost', True)  # Always on top
    
    # Dark mode styling for the popup
    label = tk.Label(root, text=answer_text, font=("Arial", 14, "bold"), 
                     bg="#222222", fg="#00FFCC", padx=30, pady=20, wraplength=500)
    label.pack()
    
    # Center it on the screen
    root.eval('tk::PlaceWindow . center')

    # Self-destruct after 5000 milliseconds (5 seconds)
    root.after(5000, root.destroy)
    root.mainloop()

# --- 2. MAIN LOGIC ---
try:
    print("Taking screenshot...")
    screenshot = ImageGrab.grab()

    print("Asking Gemini...")
    prompt = "Read the question, text, or problem in this image. Provide an answer from the given suitable options."
    response = model.generate_content([prompt, screenshot])

    print("Showing popup...")
    show_transparent_popup(response.text)

except Exception as e:
    # If something breaks (like no internet), show the error in the popup!
    show_transparent_popup(f"Error: {e}")