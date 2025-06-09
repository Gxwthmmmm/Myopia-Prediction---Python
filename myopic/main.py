<<<<<<< HEAD
import gradio as gr
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Initialize a simple model (in a real application, you would train this with actual data)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Function to predict myopia rating
def predict_myopia(patient_id, patient_name, age, sex, screen_time, sun_exposure, sun_time, parent_vision):
    # Convert inputs to numerical values
    age = float(age)
    screen_time = float(screen_time)
    sun_time = float(sun_time) if sun_exposure == "Yes" else 0
    parent_vision = float(parent_vision)
    
    # Create feature array
    features = np.array([[age, screen_time, sun_time, parent_vision]])
    
    # Make prediction (in a real application, this would use the trained model)
    # For demonstration, we'll use a simple rule-based approach
    if screen_time > 6 or (sun_exposure == "No" and screen_time > 4):
        rating = 2
    elif screen_time > 4 or (sun_exposure == "No" and screen_time > 2):
        rating = 3
    elif screen_time > 2 or (sun_exposure == "No" and screen_time > 1):
        rating = 4
    else:
        rating = 5
    
    # Adjust rating based on parent's vision
    if parent_vision <= 3:
        rating = max(1, rating - 1)
    
    # Adjust rating based on sun exposure
    if sun_exposure == "Yes" and sun_time >= 2:
        rating = min(6, rating + 1)
    
    # Determine status
    status = "Myopic" if rating <= 3 else "Normal"
    
    return f"""
    Patient Details:
    ID: {patient_id}
    Name: {patient_name}
    Age: {age}
    Sex: {sex}
    
    Vision Rating: {rating}/6
    Status: {status}
    
    Analysis:
    - Screen Time: {screen_time} hours
    - Sun Exposure: {sun_exposure}
    - Parent Vision Rating: {parent_vision}/6
    """

# Create Gradio interface
with gr.Blocks(title="MYOPIC PREDICTION SYSTEM") as demo:
    gr.Markdown("# MYOPIC PREDICTION SYSTEM")
    gr.Markdown("Enter the details to know you risk:")
    
    with gr.Row():
        with gr.Column():
            patient_id = gr.Textbox(label="Patient ID")
            patient_name = gr.Textbox(label="Patient Name")
            age = gr.Number(label="Age", minimum=0, maximum=100)
            sex = gr.Radio(["Male", "Female"], label="Sex")
            screen_time = gr.Number(label="Screen Time (hours per day)", minimum=0, maximum=24)
            sun_exposure = gr.Radio(["Yes", "No"], label="Sun Exposure")
            sun_time = gr.Number(label="Sun Exposure Time (hours per day)", minimum=0, maximum=24)
            parent_vision = gr.Number(label="Parent's Vision Rating (1-6)", minimum=1, maximum=6)
            
            submit_btn = gr.Button("Predict")
        
        with gr.Column():
            output = gr.Textbox(label="Prediction Results", lines=10)
    
    submit_btn.click(
        fn=predict_myopia,
        inputs=[patient_id, patient_name, age, sex, screen_time, sun_exposure, sun_time, parent_vision],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch() 
=======
print("Hello worldddd")
print("hello Gowtham")
>>>>>>> 36b349cc6e44924b79be1dc9d9dae34ac54ff5f8
