# BITS F364 Human Computer Interaction - Assignment 3

This repository contains the code and documentation for **Assignment 3: Automated UX Testing using Selenium and Appium**.

---

## Requirements

- Python 3.10+
- Selenium WebDriver
- Appium Python Client
- Chrome WebDriver
- Android SDK (for Appium tests)
- Additional Python packages:
  - `pandas`
  - `matplotlib`

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sid881/HCI_Assignment.git
   cd bits-f364-assignment3
   ```

2. Install the required Python packages:

   ```bash
   pip install selenium webdriver-manager pandas Appium-Python-Client matplotlib
   ```

---

## Running the Tests

### Website Tests (Using Selenium)

To run the Amazon website tests:

```bash
python web.py
```

This will:
1. Open Amazon.in in a headless Chrome browser
2. Search for "wireless headphones"
3. Sort by price and retrieve the lowest priced item
4. Sort by highest rated and retrieve the lowest priced item
5. Add the highest rated item to the cart
6. Record response times for each action

---

### Mobile App Tests (Using Appium)

This section provides instructions for setting up and running the Appium tests on a local Android emulator or physical device.

---

## Setup Instructions for Appium Testing

### Prerequisites

1. Install Node.js and npm  
2. Install Appium using npm:

   ```bash
   npm install -g appium
   ```

3. Install Appium Doctor:

   ```bash
   npm install -g appium-doctor
   ```

4. Run Appium Doctor to verify your setup:

   ```bash
   appium-doctor --android
   ```

5. Install Android Studio and set up an emulator or connect a physical device  
6. Install the required Python packages:

   ```bash
   pip install Appium-Python-Client pandas
   ```

---

### Setting Up the Android Emulator

1. Open Android Studio  
2. Go to **Tools > AVD Manager**  
3. Create a new virtual device (e.g., Pixel 4 with Android 11)  
4. Start the emulator  

---

### Installing the Amazon App

1. On the emulator or device, open Google Play Store  
2. Search for **Amazon Shopping**  
3. Install the app  
4. Open the app once to complete any initial setup  

---

### Running the Appium Server

1. Open a terminal or command prompt  
2. Start the Appium server:

   ```bash
   appium
   ```

3. Keep this terminal open while running the tests  

---

### Running the Mobile App Tests

1. Open another terminal or command prompt  
2. Navigate to the test script directory  
3. Run the mobile test:

   ```bash
   python app.py
   ```

---

## Troubleshooting

- **Connection issues**: Ensure the Appium server is running  
- **Element not found**: The app UI might have changed; update the selectors in the script  
- **Device not found**: Make sure the emulator is running or your physical device is connected  
- Run `adb devices` to verify if your device is recognized  

---

## Notes on Test Execution

Both the web and mobile tests will:

- Search for "wireless headphones"
- Sort by price and retrieve the lowest priced item
- Sort by highest rated and retrieve the lowest priced item
- Add the highest rated item to the cart
- Record response times for each action

---
## Notes on app tap gesture functions
Since the Amazon Android app disables WebView support by default and uses only native components, most automated interactions in this script are performed using tap gestures. These gestures locate UI elements based on their relative positions or accessibility identifiers, due to limited access to traditional web-based DOM queries.
Since DOM-based retrieval of product names and prices was not possible due to the native nature of the Amazon app, screenshots of the results were captured instead for further 
   analysis or manual verification. these two screenshot are saved as lowest_priced.png and customer_review.png.
  

## License

This project is submitted as part of the **BITS F364 Human Computer Interaction** course assignment.
