*****************************REST API: Patent Search*****************************
Problem Statement:
-	Develop a keyword-based search feature that retrieves documents by performing a keyword search on the text content (all fields) within the documents.
Implementation:
-	Used Cloud Elastic Search and Flask REST Frame work to Implement the Solution.
-	Container has been created for application using Docker.
-	Git for Version control and GitHub to upload Code.
File Structure:
-	app/
   o	patent_json/: Contains JSON Data
   o	credential.py: Contain Authentication Details Elastic Cloud.
   o	Elastic_connections.py: All request and response operation for application
   o	query_preparator.py: prepare query to execute on elastic cloud
   o	views.py: Resource API to get relevant response from elastic cloud.

-	main.py: initialization of program starts here.
-	Dockerfile: Contain details of “how to create container”
-	Docker-compose.yml: to build and manage image.
-	.gitignore: ignore files that are not required while checkin.
-	.dockerigone : ignore files that are not required for dockerizations.
-	requirements.txt : contains all dependencies.
