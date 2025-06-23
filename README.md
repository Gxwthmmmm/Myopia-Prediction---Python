MYOPIC PREDICTION SYSTEM - PROJECT REPORT
Project Title: MYOPIC PREDICTION SYSTEM
Objective: To develop an interactive web-based tool that predicts a patient's risk of myopia (nearsightedness) based on
input factors like screen time, sun exposure, and parental vision history using rule-based logic within a Gradio
interface.
Technologies Used:
- Python
- Gradio
- NumPy
- Scikit-learn (for future use)
- Pandas (currently unused)
System Design:
Inputs:
- Patient ID, Name, Age, Sex
- Screen Time (in hours/day)
- Sun Exposure (Yes/No)
- Sun Time (in hours/day)
- Parent's Vision Rating (1-6)
Backend Logic:
- Rule-based logic estimates risk
- High screen time or low sun exposure increases risk
- Parental vision improves/reduces rating
Output:
MYOPIC PREDICTION SYSTEM - PROJECT REPORT
- Vision rating out of 6
- Status: Myopic or Normal
- Summary Analysis
Sample Output
Patient Details:
ID: 123
Name: John Doe
Age: 12
Sex: Male
Vision Rating: 2/6
Status: Myopic
Analysis:
- Screen Time: 7 hours
- Sun Exposure: No
- Parent Vision Rating: 3/6
Strengths
- Simple and intuitive UI
- Fast prototyping using Gradio
- Extendable logic
Limitations
- No real ML used yet
- Static rule-based logic
- No input error validation
MYOPIC PREDICTION SYSTEM - PROJECT REPORT
Future Enhancements
- Train and use ML model
- Save reports
- Add login system
- Visual analytics
- Mobile-friendly UI
References
- https://www.gradio.app
- https://scikit-learn.org
- https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment
