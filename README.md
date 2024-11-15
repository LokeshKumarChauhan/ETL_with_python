# A Comprehensive ETL Workflow with Python for Data Engineers
Solution Overview
This project submission demonstrates a complete ETL (Extract, Transform, Load) workflow using Python, addressing core data engineering skills. The ETL process involves:

Extracting data from various file formats (CSV, JSON, XML),
Transforming data, including unit conversions, and
Loading the transformed data into a structured CSV format for further analysis.
Project Orientation Video
For an overview of the project requirements and objectives, refer to the orientation video: Project Orientation - Comprehensive ETL.

Project Objectives Achieved
By implementing this project, I accomplished the following:

Extracted data from multiple file formats (CSV, JSON, XML).
Transformed data by converting units (e.g., inches to meters, pounds to kilograms).
Loaded transformed data into transformed_data.csv, a structured CSV format.
Implemented logging for each ETL step, ensuring traceability.
Technologies Used
Programming Language: Python
Data Formats: CSV, JSON, XML
Libraries:
pandas - for data manipulation
glob - to handle file format patterns
xml.etree.ElementTree - for parsing XML data
datetime - for logging timestamps
Project Dataset
The dataset is obtained from the following source:


wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
After downloading, the files were extracted with:

unzip source.zip -d ./unzipped_folder
Solution Steps and Code Walkthrough
Step 1: Data Extraction
Separate functions were implemented to handle data extraction from each file type:

extract_csv() - Extracts data from CSV files.
extract_json() - Extracts data from JSON files.
extract_xml() - Extracts data from XML files.
Each file type’s data is combined into a single DataFrame for further processing.

Step 2: Data Transformation
Data transformation involved converting:

Heights from inches to meters,
Weights from pounds to kilograms.
This standardized the data format, making it suitable for analysis or storage.

Step 3: Data Loading
The transformed data is saved in transformed_data.csv, enabling seamless data import into databases or other analytical tools.

Step 4: Logging
To facilitate monitoring and debugging, logging was implemented for each ETL phase:

Extraction Phase: Logs data extraction activities.
Transformation Phase: Logs data transformation activities.
Loading Phase: Logs data loading activities.
Logs are recorded in log_file.txt to maintain a history of ETL operations.

Execution Instructions
Prerequisites
Python 3.6+
Required Python libraries (pandas)
To install the necessary packages:

pip install pandas
Running the Solution
To execute the ETL script, use:


python etl_script.py
Ensure the dataset files are available in the designated folder, and check log_file.txt for the log details of each ETL phase.

Solution Structure
plaintext
Copy code
├── unzipped_folder/           # Folder with CSV, JSON, and XML files
├── etl_script.py              # Python script implementing ETL workflow
├── log_file.txt               # Log file tracking ETL process
├── transformed_data.csv       # Output CSV file with transformed data
└── README.md                  # Project documentation (this file)
Secure Code Practices
This project adheres to secure code guidelines by following best practices such as:

Excluding sensitive credentials from the codebase.
Using secure coding practices outlined in Secure Code: Managing Credentials with Your Python Script session on 28/09/2024.
Coding Standards Followed
The code adheres to the PEP 8 coding standards, ensuring code readability and maintainability.