# AI-Powered Test Case Generator for Mobile Apps

This project leverages **OpenAI's GPT-4 multimodal API** to generate detailed, structured **test cases** based on screenshots and optional context provided by the user. The tool is specifically designed to generate test cases for mobile app features such as bus ticket booking, seat selection, and offers/filters.

## Overview

This repository hosts an AI-powered web tool that allows users to:
- Upload multiple screenshots of a mobile app feature.
- Provide optional context to tailor the test cases.
- Receive detailed test cases, including:
  - **Description of the feature**.
  - **Pre-conditions** for testing.
  - **Step-by-step testing instructions**.
  - **Expected results**.

## Hosted Links

- **Web Interface**: [Visit the Web App](https://myracle.vercel.app)
- **API Endpoint**: The backend is hosted on Heroku. The POST endpoint for generating test cases is:
https://myracle-api-53a8b39a3558.herokuapp.com/describe

## Features

- Multi-image upload for screenshots.
- Context input to guide test case generation.
- Outputs detailed test cases in a structured format (description, pre-conditions, steps, expected results).

## Use Case

This tool is particularly useful for **QA testers** or **developers** looking to automatically generate comprehensive test cases for mobile app features. For example, the tool can generate a test case for the **bus booking flow** on travel apps such as RedBus, MakeMyTrip, or Goibibo. By providing screenshots of the app interface and optional context, the tool can automatically generate the following:

- **Description**: A brief overview of the feature.
- **Pre-conditions**: What needs to be set up before testing.
- **Testing Steps**: Step-by-step instructions for testing.
- **Expected Results**: What the expected outcome should be if the feature works as intended.

# Prompt Example:
```
"Based on the uploaded screenshots and the provided context, generate a detailed test case for feature testing. Ensure the output includes the following structure:
- Description of the feature
- Pre-conditions for testing
- Step-by-step testing instructions
- Expected result after testing the feature"
```
This allows the model to create a well-organized test case covering all necessary aspects of the feature to be tested.

## Example Output

### Test Case for Bus Ticket Booking Feature

---

**Description of the Feature:**
This feature allows users to select and book a bus ticket from Mumbai to Bangalore by selecting available seats, boarding and dropping points, and proceeding to payment. The user interface should display available seats, the total fare, and other relevant details for the journey.

---

**Pre-conditions for Testing:**
1. The testing environment should have internet access.
2. The user should not be logged in (for testing as a guest user).
3. There should be available bus schedules for the route Mumbai to Bangalore on the selected date.
4. The system should be initialized without any backend errors.

---

**Step-by-Step Testing Instructions:**

1. **Navigate to the Website:**
 - Open the web browser and go to `redbus.in`.

2. **Search for Buses:**
 - Enter "Mumbai" in the "From" field.
 - Enter "Bangalore" in the "To" field.
 - Select the date "28 Sep 2024" from the date picker.
 - Click the "SEARCH BUSES" button.

3. **Select a Bus:**
 - From the list of available buses, identify a bus based on departure time.
 - Click on the "VIEW SEATS" button next to a chosen bus.

4. **Choose Seats:**
 - Upon navigating to the seat selection page, ensure that available seats are highlighted.

---

**Expected Result:**
The selected seat should be highlighted, and the user should be able to proceed to the payment page with the selected bus and seat details.

# Screenshots
Screenshots are available to showcase the process:

Web Interface:

Generated Test Case:

# How It Works
- Users visit the web interface and upload one or more screenshots.
- Optionally, users can provide additional context for test case generation.
- Upon submission, the backend API (hosted on Heroku) processes the request and generates a structured test case.
- The result is displayed in the web interface for users to review or copy.

# Local Setup
To run this project locally, follow these steps:

Clone the Repository
```
git clone https://github.com/Arittra-Bag/Myracle.git
```
Access the app by navigating to http://127.0.0.1:5000 in your browser.

# License
This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.
