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
    FOLDERFILE = './files/'
5. Run the following command to run all test cases and view the reports in Allure \
   - py.test --alluredir=general_report ./tests
   - allure serve general_report (You need have installed Allure Framework in your OS)

6. Run the following command to run all acceptance tests cases \
   - py.test --alluredir=acceptance_report ./tests -m acceptance
   - allure serve acceptance_report
   
7.Run the following command to run all negative tests cases \
   - py.test --alluredir=negative_report ./tests -m negative
   - allure serve negative_report

8.Run the following command to run all regression tests cases \
   - py.test --alluredir=regression_report ./tests -m regression
   - allure serve regression_report

9.Run the following command to run all black_box tests cases \
   - py.test --alluredir=black_box_report ./tests -m black_box
   - allure serve black_box_report

10.Run the following command to run all sanity tests cases \
   - py.test --alluredir=sanity_report ./tests -m sanity
   - allure serve sanity_report