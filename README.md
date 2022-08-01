# Apicitos
Tests of the CRUD of comments and users endpoints of Wordpress
To execute the framework needs: \
1.Install wordpress \
2.Install the following pluggings:\
    - WordPress REST API Authentication\
    - WP REST API Controller\
3.Activate the installed pluggins \
4.Create a file .env with the following environment variables must be set with the required data:

    BASE_URL -> The url of your local wordpress 
    USER-> username registered in your local wordpress
    PASSWORD -> password registered in your local wordpress
    ACCESS_TOKEN -> Copy the authorization token generate with the pluggin
    ID_COMMENT -> id of comment created
    ID_USER -> id of user created
