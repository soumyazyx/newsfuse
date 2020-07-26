user_profile
    user_id 
    user_name
    email_id

user_subscriptions
    user_id | FK
    feed_id | FK

user_articles
    user_id
    article_id | FK 
    read_status | boolean true/false 
    

