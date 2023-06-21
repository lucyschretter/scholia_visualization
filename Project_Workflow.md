Welcome to the project workflow! 

1. Introduction
2. Data Collection and Understanding
3. GitHub Repository Strucutre
4. Dashboard Design and Features
5. Visualization Implementation
6. Testing and Quality Asssurance
7. Documentation and Deployment
8. Conclusion


**1. Introduction**
This GitHub repository shows our work on a group project to create a comprehensive dashboard for visualizing Scholia diseases data. 
The initial goal of creating a Circos plot to showcase connections between diseases and their associated papers has been revised. 
Instead, we aim to develop a dashboard that incorporates multiple visualizations to provide insights into various diseases of a specific disease group. 
The purpose of the project is to analyze and present meaningful information derived from the Scholia diseases topic using Python, SPARQL endpoint to execute queries and libraries to visualize data.
In this project, we are specifically working with data related to psychiatric diseases. 
We have selected the following diseases for our analysis:
  - Mental Depression
  - Bipolar Disorder
  - Schizophrenia
  - Bulimia
  - Migraine

We chose this topic and these diseases due to their significant impact on individuals' mental health and the wider population. 
Each of these diseases represents a distinct psychiatric condition, and Scholia allowing us to explore a range of aspect about the diseases. 


**2. Data Collection and Understanding**
We have obtained the necessary data from Scholia and Wikidata. 
The data collection process involved accessing the Scholia API and extracting relevant information about diseases, such as prevalence, genetic associations, comorbidities, medication, geographic distribution, symptom frequencies, disease trends over time. 
Understanding the data structure has allowed us to identify the key attributes and relationships within the dataset.


**3. GitHub Repository Structure**
To ensure effective collaboration, we have structured our GitHub repository with organized folders. 
The repository includes directories for data collection scripts - *data collection* | app folder with *util.py* with visualization functions; *main.py* with code to generate the dashboard; *run.py* with code to run dash |Application directory with util, main and run script - *Dashboard* |  testing scripts and visuals - *Schizophrenia* 
This structure facilitates easy navigation and version control, allowing team members to work simultaneously and merge changes seamlessly.

**4. Dashboard Design and Features**
The dashboard will feature multiple visualizations to address the identified goals. 
These visualizations will include bar charts, line graphs, etc. Each visualization will provide insights into specific disease-related aspects. 
The dashboard will be developed using Python, Dash, and Plotly libraries, providing an interactive and user-friendly interface.

**5. Visualization Implementation**
For each visualization, we will follow a systematic implementation process. We will use plot libraries to create the visualizations. T
he code snippets and scripts for each visualization will be well-documented and shared within the GitHub repository. We will consider the availability of data and perform any necessary data cleaning or preprocessing steps before generating the visualizations. 
Throughout the implementation, we will address specific challenges, such as dealing with incomplete or missing data, ensuring data integrity, and optimizing the visualizations for performance.

**6. Testing and Quality Assurance**
To ensure the functionality and accuracy of the dashboard, rigorous testing will be conducted. 
We will validate each visualization against the expected results, checking for proper data integration and correct display of information. We will also assess the responsiveness and interactivity of the dashboard to ensure a seamless user experience. Any identified issues or bugs will be addressed promptly, and the dashboard will undergo iterative testing to guarantee its reliability.

**7. Documentation and Deployment**
Thorough documentation is crucial for understanding and replicating the project. 
We will include code comments and documentation files to provide clarity and insight into the implementation details. 
User guides and technical manuals will be created to explain the dashboard's functionalities, allowing users to navigate and interpret the visualizations effectively. 
Additionally, we will provide instructions for deploying the dashboard, either running the script or on the terminal, ensuring accessibility for end users. The documentation and deployment instructions will be included in the GitHub repository.


**8. Conclusion**
In conclusion, we have adapted our project's focus from a Circos plot to a comprehensive dashboard for visualizing Scholia diseases data. 
The dashboard will incorporate multiple visualizations, addressing various disease-related aspects outlined in the project goals. 
The revised workflow ensures effective collaboration, systematic implementation, thorough testing, and comprehensive documentation. 
We are confident that the developed dashboard will provide valuable insights into the diseases, empowering users to explore and understand the Scholia diseases Topic and information about a specific disease and also expand the dashbaord per need or interest.
