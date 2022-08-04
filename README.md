# Apicitos
Tests of the CRUD of comments and users endpoints of WordPress
To execute the framework needs: \
1.Install WordPress \
2.Install the following plugins:\
    - WordPress REST API Authentication\
    - WP REST API Controller\
3.Activate the installed plugins \
4.Create a file .env in root project with the following environment variables must be set with the required data:

    BASE_URL -> The url of your local wordpress e.g. BASE_URL = 'http://localhost/apicitos'
    USER-> username registered in your local wordpress e.g. USER = 'apicitos'
    PASSWORD -> password registered in your local wordpress PASSWORD = '1234'
    ACCESS_TOKEN -> Copy the authorization token generate with the pluggin WordPress REST API Authentication e.g. ACCESS_TOKEN = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey...'
    ID_COMMENT -> id of comment created 
    ID_USER -> id of user created
5. Run the following command to run all test cases and get reports \
   - py.test --alluredir=%allure_result_folder% ./tests

6. Run the following command to view the reports in Allure\
   - allure serve %allure_result_folder% (You need have installed Allure Framework in your OS)
