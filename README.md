# 2) MODEL DEPLOYMENT DEMONSTRATION
Please fork this repo (you may opt to share a private repo with us to preserve your privacy) and then do the following:
- Create a branch in your forked repo
- Create a container to process inference requests from any pretrained model in the huggingface model hub: https://huggingface.co/models
- Your solution should include server components to support multiple parallel incoming requests (e.g., NGINX/gunicorn)
- Create a notebook to demonstrate requests that POST to the container endpoint and print out the response
- Please explain why you have chosen this model as your demonstration

In this I have used Flask, hugging face and gunicorn to build a complete model to run a pretrained hugging face model in any location machine using docker. I chose this model because I was performing sentiment analysis EDA on amazon_popularity and noticed that this model had good number of verified reviews, and the output made sense to me. That is the main reason I chose this model. I created everything following few blogposts and journal.
