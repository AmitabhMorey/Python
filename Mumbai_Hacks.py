import requests

# Function to call the LLM API
def call_llm(prompt):
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',  # Replace with your actual API key
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': prompt,
        'max_tokens': 100,  # Adjust the token limit as needed
    }
    response = requests.post('YOUR_LLM_ENDPOINT', headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('choices')[0].get('text').strip()
    else:
        return "Error: Unable to fetch data from LLM"

def generate_recommendation(learning_style, performance):
    # Placeholder for your recommendation logic
    return f"Based on your learning style: {learning_style}, and performance: {performance}, here are some recommendations."

def optimize_study_schedule(subjects, study_times, performance):
    # Placeholder for your optimization logic
    return f"Optimized study schedule for subjects: {subjects} with times: {study_times}."

def main():
    name = input("Enter your name: ")
    learning_style = input("Enter your learning style: ")
    
    # Get performance metrics
    performance = {
        'math': int(input("Enter your performance in Math (0-100): ")),
        'science': int(input("Enter your performance in Science (0-100): ")),
        'history': int(input("Enter your performance in History (0-100): ")),
    }

    # Get subjects and their study times
    subjects = input("Enter subjects (comma-separated): ").split(',')
    study_times = input("Enter study times (comma-separated): ").split(',')

    # Generate recommendations and optimized schedule
    recommendation = generate_recommendation(learning_style, performance)
    schedule = optimize_study_schedule(subjects, study_times, performance)

    # Call the LLM to get additional insights
    llm_prompt = f"Generate a study plan for {name} who learns best through {learning_style}. Performance metrics: {performance}. Subjects: {subjects}. Study times: {study_times}."
    llm_insights = call_llm(llm_prompt)

    # Output the results
    print("\n--- Study Plan ---")
    print(f"Name: {name}")
    print(f"Recommendations: {recommendation}")
    print(f"Optimized Schedule: {schedule}")
    print(f"LLM Insights: {llm_insights}")

if __name__ == '__main__':
    main()