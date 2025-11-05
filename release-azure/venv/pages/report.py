import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

with col1:
    version = st.text_input("Insira a versão da release: ")
    analyst_name = st.text_input("Insira o nome do analista: ")
    sprint = st.text_input("Insira o numero da sprint")
    date = st.text_input("Insira a data do relatório: ")

with col2:
    link_testplan = st.text_input("Insira o link do Test Plan")
    link_testresult = st.text_input("Insira o link do Test Result")
    link_exploratorytest = st.text_input("Insira o link do relatório de teste exploratorio")
    link_testReport = st.text_input("Insira o link do Test Report")
with col3:
    stories = st.text_area("Insira o markdown das stories")
    bugs = st.text_area("Insira o markdown dos bugs")

with col4:
    with st.expander("Test Plan"):
        st.markdown(f'''
        Test Plan - Version {version} - Jabil - Tester Performance
        ========================================================================================================================================================================================================================================

        1. Introduction
        --------------------------------------------------------------------------------------------------------------------------------------------------------

        ### 1.1 Purpose of the Document

        This document aims to outline the testing process for the Jabil - Tester Performance System project. It will define testing strategies and artifacts, delineate the project scope, and list the testing methodologies and artifacts to be generated throughout the project's duration.

        ### 1.2 Purpose of the Project

        The project objective consists of enhancing performance, availability, and utilization of testers by standardizing performance monitoring across all Jabil sites and acquiring real-time data for analysis and decision-making.

        2. Test Strategies
        -------------------------------------------------------------------------------------------------------------------------------------------------------

        *   Data validation tests;
        *   Manual tests on the web application.

        ### 2.1 Testing Tools 
        For the execution of the tests Azure DevOps will be used to Project documentation, monitoring of activities, registration and monitoring of failures found during the tests. Case Tests.

        ### 2.2 Testing Activitiese 
        Test analyst for this project is responsible for performing the following activities:
        *   Create and maintain the test plan;
        *   Document information in Confluence throughout the project;
        *   Document activities in Azure;
        *   List flaws and improvements found in Azure;
        *   Monitor the registered flaws and improvements until their resolution or cancellation;
        *   Create and run test cases as needed;
        *   Create and run exploratory tests as needed;
        *   Apply test strategies aimed at ensuring the project's quality;
        *   Develop automated tests whenever possible.

        ### 2.3 Feature Development Lifecycle

        Project documentation and monitoring:
        *   N/A

        ### 2.4 Testing Types
        Types of tests to be applied:
        *   Business rule;
        *   Screen and layout rule;
        *   Verification;
        *   Exploratory test;
        *   Regression test;
        *   Automated test;
        *   Performance test.

        ### 2.5 Test Criteria

        #### 2.5.1 Success Criteria
        The system version will be considered stable and recommended for the customer when all planned tests are completed, and all bugs with "high" severity are checked.

        #### 2.5.2 Failure Criteria
        The system version will be considered faulty and not recommended when there are planned tests not yet executed, and bugs with "normal" or higher severity awaiting correction.

        #### 2.5.3 Suspension Criteria

        The version will be considered unstable and suspended with one or more "Blocked" errors and five or more "Critical" errors.

        ### 2.6 Test Requirements
        #### 2.6.1 Requirements for Starting Teststing

        Testing will begin whenever a new version identified as a "test version" is made available and there are no test activities currently being performed.

        #### 2.6.2 Requirements for Restarting Tests After Suspension

        Testing will resume after an interruption when all “Blocked” bugs have been fixed, and a new test version is available.

        ### 2.7 Development and Approvall

        This section outlines the procedures and locations for conducting tests and obtaining approvals.  
        For the current version testing will be conducted manually by deploying the system on the following machine:
        *   Server:  
            _Work Platform_: VDI - Remote Desktop  
            _Hardware_: Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz (2.59 GHz), 16GB RAM  
            _Software_: Low-Code - Mendix
        
        *   Client:  
            _Work Platform_: Desktop / Web  
            _Hardware_: Notebook Intel(R) Core(TM) i7-1185G7 CPU @ 3.00GHz 1.80GHz 16GB Operational System of 64 bits  
            _Software_: Windows 11
        

        3. Test Scope----------------------------------------------------------------------------------------------------------------------------------------

        ### 3.1 Test Cases to be Tested

        This section describes the test cases that the test team will validate.
        *   N/A

        ### 3.2 Test Cases Excluded to Test test

        This section describes the test cases that will not be validated by the test team.
        *   N/A

        ### 3.3 Test Reports

        [Test Report - Version {version}]({link_testReport})


        ''')
    with st.expander("Test Results"):
        st.markdown(f'''

        # Test Results - Version {version} - Jabil - Tester Performance

        ## Version
        {sprint}

        ## Functionalities:
        - N/A

        ## Bugs and Improvements Found:
        - N/A

        ## Bugs and Improvements Validated:

        {bugs}

        ## Bugs Reopened:
        - N/A

        ## Documentation:
        - [Exploratory Test Sprint {sprint} - Version {version}]({link_exploratorytest})]''')
with col5:    
    with st.expander("Exploratory Test"):
        st.markdown(f'''
        Exploratory test
        # Exploratory Test - Version {version} - Jabil - Tester Performance

        ## Story:

        {stories}

        ## Mission:
        - Test the stories according to the release notes available

        ## Description:

        - ***Explore*** Release {sprint} for testing features.
        - ***To*** test the features:

        ## Testing Time:
        - 1 day

        ## Tester:
        - {analyst_name}

        ## Key Areas:
        - Validation of release notes;
        - Black box testing;
        - Exploratory test;
        - Regression test.

        ## Setup:
        ### Access Instructions:
        - FRONTEND
        - Connection with Jabil VDI
        - [Application Access](https://testerperformance.qa.mendix.jabilapps.com)

        ## Notes:
        I'm pleased to inform that the testing of the Jabil - Tester Performance System v{sprint} project has been successfully completed with a positive outcome. Consequently, the version has been **approved**.

        ## Bugs and Improvements Found:

        [Version {version} - Overview](https://dev.azure.com/VNT-MAO-Jabil/Tester%20Performance/_wiki/wikis/Tester-Performance.wiki/1109/Version-2.5)
''')
    
    with st.expander("Test Report"):
        st.markdown(f'''        

        # Test Report - Version {version} - Jabil - Tester Performance

        ## Introduction
        This document outlines the testing plan for the **Jabil - Tester Performance System**, aligning with raised requirements and following the guidelines and features discussed during the project planning meeting.

        ## Objectives
        1. Identify project information and software components for development in each sprint backlog cycle;
        2. Recommend and outline testing strategies for the project cycle;
        3. List the test requirements for each sprint backlog cycle, detailing test scenarios creation, execution, verification, and validation;
        4. Identify testing resources and estimate testing efforts;
        5. Document test reports to identify areas for improvement in the testing process.

        ## Test Planning
        This section details the test planning for the current sprint: [Test Plan - Version {version}]({link_testplan})
        ### Requirements for Testing
        - N/A

        ### Features Excluded from Testing
        - N/A

        ## Testing Types
        This section outlines various types of tests to be conducted.

        |ID | Business Rules | Screen Rules | Layout Validation | Bug Verification | Regression Test |
        |--|--|--|--|--|--|
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |
        |: |  |  |  | ✅ |  |


        ### Done Criteria
        The test is considered done when the following activities are carried out for each story:

        1. *Per Sprint:*
        - Creation of a test plan (Test Activities report in Azure Wiki);
        - Documentation review;
        - Sprint Test Report (Test report of the sprint including defects/bugs found and tested stories).

        2. *Per Story:*
        - Test case specification;
        - Test case automation;
        - Test case execution;
        - Reporting of bugs and improvements;
        - Verification of bugs and improvements.

        ### Fail Criteria
        Bugs and improvements discovered will be reported in Azure according to the following criteria:
        1. *Test Suspension:* Testing will be paused whenever the release being evaluated is deemed unstable, characterized by the presence of **two or more** Block Bugs (highest priority) and **five or more** Critical Bugs. Furthermore, the testing will be resumed in the next released version.
        2. *Test Passed:* To recommend stories for invitation to the customer, it is necessary that **all planned tests** are Done and only bugs with **low-priority and To-Do** status remain.

        ## Test Environment
        The Project Jabil - Tester Performance System will be tested by **{analyst_name}** throughout the entire development process, with activities planned for each cycle. The following tools will be used for testing:

        - Jabil VDI connection  
        - Google Chrome  
        - Azure DevOps  
        - Confluence  

        ## Test Results
        This session presents the results of the current sprint's test: [Test Results - Version {version}]({link_testresult})
        ## General Information

        ### Testers:
        - {analyst_name}

        ### New Features Evaluated
        - N/A

        ### Final Feedback from the Test Team
        We are in favor of delivering the tested functionalities from this cycle to the client.

        **Bugs and Improvements Found**
        - N/A

        ## Tests Executed
        - [Exploratory Test - Version {version}]({link_exploratorytest})''')