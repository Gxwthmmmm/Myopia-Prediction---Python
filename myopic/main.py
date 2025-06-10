import gradio as gr
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Initialize a dummy model (optional, not used here)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Function to predict myopia rating
def predict_myopia(patient_id, patient_name, age, sex, screen_time, sun_exposure, sun_time, parent_vision):
    # Convert inputs
    age = float(age)
    screen_time = float(screen_time)
    sun_time = float(sun_time) if sun_exposure == "Yes" else 0
    parent_vision = float(parent_vision)
    
    # Dummy feature array (not used for rule-based logic)
    features = np.array([[age, screen_time, sun_time, parent_vision]])
    
    # Rule-based logic for rating
    if screen_time > 6 or (sun_exposure == "No" and screen_time > 4):
        rating = 2
    elif screen_time > 4 or (sun_exposure == "No" and screen_time > 2):
        rating = 3
    elif screen_time > 2 or (sun_exposure == "No" and screen_time > 1):
        rating = 4
    else:
        rating = 5
    
    # Adjustments
    if parent_vision <= 3:
        rating = max(1, rating - 1)
    if sun_exposure == "Yes" and sun_time >= 2:
        rating = min(6, rating + 1)
    
    # Determine status
    status = "Myopic" if rating <= 3 else "Normal"
    
    # Recommendation based on vision rating
    if rating == 3:
        recommendation = "Recommendation: Your eyesight is at the borderline.Try reducing screen time to improve vision."
    elif rating > 3:
        recommendation = "Recommendation: You have good eyesight.Maintain healthy habits!"
    else:  # rating < 3
        recommendation = "Recommendation: Vision is deteriorating. Consider consulting an eye specialist and follow medication if prescribed."

    return f"""
    PATIENT DETAILS:
    ID:  {patient_id}
    Name:  {patient_name}
    Age:  {age}
    Sex:  {sex}

    GIVEN DETAILS:
    Screen Time: {screen_time} hours/day
    Sun Exposure: {sun_exposure}
    Parent Vision Rating: {parent_vision}/5

    VISION DETAILS:
    Vision Rating: {rating}/5
    Status: {status}
    
    {recommendation}
    """

# Function to reset all inputs
def reset_inputs():
    return "", "", None, None, None, None, None, None, ""

# Function to toggle sun time visibility
def toggle_sun_time(sun_exposure):
    return gr.update(visible=(sun_exposure == "Yes"))

# Gradio Interface
with gr.Blocks(title="MYOPIC PREDICTION SYSTEM") as demo:
    gr.Markdown("# MYOPIC PREDICTION SYSTEM")
    gr.Markdown("Enter the details to know your risk:")
    
    with gr.Row():
        with gr.Column():
            patient_id = gr.Textbox(label="Patient ID")
            patient_name = gr.Textbox(label="Patient Name")
            age = gr.Number(label="Age", minimum=0, maximum=100)
            sex = gr.Radio(["Male", "Female"], label="Sex")
            screen_time = gr.Number(label="Screen Time (hours per day)", minimum=0, maximum=24)
            sun_exposure = gr.Radio(["Yes", "No"], label="Sun Exposure")
            sun_time = gr.Number(label="Sun Exposure Time (hours per day)", minimum=0, maximum=24, visible=False)
            parent_vision = gr.Number(label="Parent's Vision Rating (1-5)", minimum=1, maximum=5)
            
            with gr.Row():
                submit_btn = gr.Button("Enter")
                reset_btn = gr.Button("Reset")
                 
        with gr.Column():
            output = gr.Textbox(label="Prediction Results", lines=14)
    
    # Update sun time visibility when sun exposure changes
    sun_exposure.change(
        fn=toggle_sun_time,
        inputs=[sun_exposure],
        outputs=[sun_time]
    )
    
    submit_btn.click(
        fn=predict_myopia,
        inputs=[patient_id, patient_name, age, sex, screen_time, sun_exposure, sun_time, parent_vision],
        outputs=output
    )
    
    reset_btn.click(
        fn=reset_inputs,
        outputs=[patient_id, patient_name, age, sex, screen_time, sun_exposure, sun_time, parent_vision, output]
    )

if __name__ == "__main__":
<<<<<<< HEAD
    demo.launch() 
=======
    demo.launch() 
>>>>>>> 4397aafa1c223630ac5d4018486b9225bc11f51f
