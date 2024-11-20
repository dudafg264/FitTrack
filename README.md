# Workout Logger with Nutritionix API and Google Sheets Integration

This project allows users to log their workouts and store the details (exercise name, duration, and calories burned) in a Google Sheet. It integrates with the Nutritionix API to fetch exercise data and the Google Sheets API to store the workout logs.

## Features

- **Exercise Tracking**: Logs exercises performed by the user, including the name of the exercise, its duration, and calories burned.
- **Date and Time Recording**: Automatically records the date and time of the workout.
- **Google Sheets Integration**: Sends workout data to a Google Sheet for easy tracking and management.
- **Nutritionix API Integration**: Uses the Nutritionix API to fetch exercise details based on user input.

## Requirements

Before running this project, ensure you have the following:

- **Python 3.x** (recommended version 3.6 or higher)
- **Python Libraries**:
  - `requests`: For making HTTP requests to the Nutritionix API and Google Sheets API.
  - `os`: For managing environment variables.
  - `datetime`: For handling date and time.
  
You can install the required libraries by running:

```bash
pip install requests
```

## Setup and Configuration

1. **Clone the repository**:
   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/workout-logger.git
   ```

2. **Set up environment variables**:
   The project uses environment variables to securely store sensitive information such as API keys. Create a `.env` file in the root directory of the project and add the following lines:

   - **APP_ID**: Your Nutritionix App ID.
   - **API_KEY**: Your Nutritionix API Key.
   - **SHEET_API**: The API URL for your Google Sheets API (this URL is typically obtained when you set up the Google Sheets API).

   Example `.env` file:

   ```bash
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   SHEET_API=your_google_sheets_api_url

3. **Set up Google Sheets API**:
   To use the Google Sheets API, create a project in the Google Cloud Console and enable the Google Sheets API. Obtain the API credentials and configure them in your environment.

## Usage

1. **Run the script**:
   Run the Python script in your terminal:

   ```bash
   python workout_logger.py
   ```

2. **Enter your exercises**:
   The script will prompt you to input the exercises you performed. Type the exercises, and the script will make a request to the Nutritionix API to get the details, such as the exercise duration and calories burned.

3. **Workout data saved in Google Sheets**:
   The details of your workout, including the exercise name, duration, calories, date, and time, will be saved in your Google Sheet for tracking and analysis.

## Example

After running the script and inputting your exercises, you might see something like the following printed:

```bash
Your workout was added successfully!
```

This confirms that the data has been successfully recorded in your Google Sheets.

## Notes


- You can customize the Google Sheets integration to store the workout data in a specific sheet or modify the format to suit your needs.
- The Nutritionix API allows you to query a variety of exercises, so you can extend this project to track different types of activities.
