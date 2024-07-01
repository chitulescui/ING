# ING Assignment
<br />
<div align="center">
  <a href="https://github.com/chitulescui/ING/blob/main/Assignment%20-%20DevOps%20FlexING.docx">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Download the initial assignment</h3>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
1. Create a Dockerfile that creates a SQL Server Docker container. The Dockerfile uses an <a href="https://hub.docker.com/r/microsoft/mssql-server">mcr.microsoft.com/mssql/server:2019-latest</a> image and has the 1433 PORT exposed. 
2. Create a `connection` to Microsoft SQL Server using `pyodbc` library in Python.
3. Create a `cursor` based on the connection established at the previous step.
4. Check if exists, create and use a Database using `create_database()` function.
5. Check if exists and create tables based on the predefined values of a list using `create_table()` function.
6. Populate the tables using `populate_tables()` function.
7. Check if exists and export a random table from your database in a JSON format using `export_table()` function.
8. Close the connection in order for transactions to not remain active on the Database server using `close_connection()` function. 

## Python
I used the following libraries to fulfill python requirements: 
* `pyodbc` - In order to establish the connection with SQL server and execute T-SQL statements. 
* `json` - In order to export T-SQL convert-to JSON statement as a file. 
* `os` - In order to directly manipulate the variables declared in Azure DevOps.
* `random` - To randomly pick which table will be exported in a JSON format.  
* `exists from os.path` - To check if the JSON file exists or not in the same directory.

Variables and credential variables were declared in separate .py files.
* For global variables used to create and manipulate the database -> `variables.py`
* For environment variables declared in Azure DevOps -> `credentials.py`

## Azure DevOps
Yaml file was created at the repository level. In order to execute `docker run` step and successfully connect to the database using Python I`ve created two variable groups:
* pythonVariables - for `pythonInterpreter` and `scriptPath` paths.
  
![PTHVARSGGOOD](https://github.com/chitulescui/ING/assets/93248891/07d39114-a300-497a-8c90-d4c720f1e48c)

* sqlVariables - for `ACCEPT_EULA`,`HOST`, `MSSQL_ROOT_PASSWORD`, `PORT`, `USER`, `JSON_NAME`(name of the output file), `DATABASE`(database name)

![SALVARSBUN](https://github.com/chitulescui/ING/assets/93248891/9d1b4b59-7769-48ce-8010-49c6c33ec88f)

Trigger was set to `none` so you can trigger the pipeline manually.
The Agent hosting the pipeline runs locally on my computer(`SWK`- declared in `Default` agent pool) 
Github repository is specified as the primary resource of the source code, using the service connection created before. (endpoint: chitulescui)

I`ve declared 3 different stages: 
* Build_And_Run_Docker_Image (2 Powershell tasks) - To execute the Dockerfile and run the Microsoft SQL container and to ensure that the Run task will start after the Build one. 
```
Docker_Build
Run_Docker_Container (dependsOn Docker_Build)
```
* Run_Python_Script (1 PythonScript@0 task) - To execute the Python script.
```
Python
```
* Publish_Python_Artifact (1 PublishPipelineArtifact@1 task) - To publish the JSON output file as an artifact. 
```
Publish_Python_Artifact
```
## Azure DevOps Pipeline Results
* The pipeline `chitulescui.ING` is working as expected.

![Pipeline_successfull](https://github.com/chitulescui/ING/assets/93248891/bab578d8-4f47-4645-bd0e-1fb7f81cfc52)

* The artifact was successfully published. 

![Published_artifact_successfully](https://github.com/chitulescui/ING/assets/93248891/0cd5123b-b36b-44ba-a487-24b8a2918be3)

* Artifact content.

![image](https://github.com/chitulescui/ING/assets/93248891/855b2403-605a-49e0-a4d6-97fcae14a268)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
