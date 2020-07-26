category
    category_title              Space 
    category_desc               Space is wow 

feed
    feed_id | PK                100
    feed_source_name            nasa.com
    feed_url                    nasa.com/feed/all

category_feeds
    category_id                 1
    feed_id                     100

article
    article_id | PK 
    link
    title
    author
    summary
    added_ts
    published
    author_img_url
    article_img_url
    feed_id | FK
    


from apscheduler.schedulers.background import BackgroundScheduler
celery
django-allauth
mq


