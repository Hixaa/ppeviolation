# ppeviolation

**1. System Requirements**
• Operating System: Windows, macOS, or Linux
• Python Version: 3.6 or higher
• Memory: Minimum 4GB RAM
• Disk Space: Sufficient space for model files and dependencies

**2. Software Dependencies**
• Python: Programming language
• PyQt5: Graphical user interface library for Python
• Ultralytics YOLO: Object detection model library

**3. Development Tools**
• Python IDE (Integrated Development Environment) such as PyCharm, Visual Studio Code, or Jupyter
Notebook
• Command-line interface or terminal for executing commands

**4. Configuration Settings**
• No specific configuration settings required.

**5. Setup Instructions**
1. Install Python: Download and install Python from the official Python website (https://www.python.org)
based on your operating system.
2. Install Required Libraries: Open a terminal or command prompt and execute the following commands:
pip install ultralytics
pip install PyQt5
3. Download Project Files: Download the project files, including ”configure.py,” ”realtime.py,” and ”last.pt.”
Store them in the same directory.
4. Run the Application: Open a terminal or command prompt, navigate to the project directory, and execute
the following command:
python configure.py
1
5. Configure Detection Preferences: In the application window, select the desired objects to be detected
(Helmet, Mask, Jacket, Shoe, Harness) by checking the corresponding checkboxes.
6. Start Real-time Detection: Click the ”Enter” button in the application window to start the real-time object
detection based on the selected preferences. Press ”Q” to exit from real-time object detection and return
to the application window.
