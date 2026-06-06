File Integrity Monitor (second project)

 Overview

This project is a simple File Integrity Monitor built with Python. The program monitors files within a selected directory by generating SHA-256 hashes and comparing them against previously stored values.

The goal of the project is to detect unauthorised changes to files, including modifications, additions, and deletions.

 Features

- Monitors files within a specified folder
- Generates SHA-256 hashes for file verification
- Detects newly added files
- Detects modified files
- Detects deleted files
- Stores file hashes in a JSON database
- Displays changes in the terminal

Technologies Used

- Python 3
- Hashlib
- OS Module
- JSON Module

How It Works

The program scans all files within the monitored directory and generates SHA-256 hashes for each file. These hashes are stored in a JSON file.

When the program runs again, it compares the current file hashes against the previously stored hashes. If a file has been added, modified, or deleted, the program displays a notification showing the change.

 Challenges

As this was my first cybersecurity project, one of the biggest challenges was understanding how hashing algorithms work and how they can be used to verify file integrity. I also had to learn how to compare stored data with current file information and detect changes accurately. Through testing and troubleshooting, I gained a better understanding of Python and defensive security concepts.

 What I Learned

Through this project I improved my understanding of:

- File integrity monitoring
- SHA-256 hashing
- Python file handling
- JSON data storage
- Basic cybersecurity monitoring techniques
- Detecting unauthorised file changes

Future Improvements

- Monitor subdirectories automatically
- Add real-time monitoring instead of manual scans
- Export logs to a file
- Send email alerts when changes are detected
- Create a graphical user interface (GUI)
- Improve reporting and logging features

 Disclaimer

This project was created for educational purposes to demonstrate file integrity monitoring concepts and defensive cybersecurity techniques.
