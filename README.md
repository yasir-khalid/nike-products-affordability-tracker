
# Nike price affordability workflow using Prefect 2.0

[Prefect.io](https://prefect.io) is an open source tool to manage your workflows seemlessly without getting into lots of boiler plate code

It can automatically detect your code execution DAGs, can run on schedule, across different infrasturcture and can be either self-hosted or cloud based monitoring.

## Screenshots

This shows the overall concept of the project; where all of the functions (called *Prefect tasks*) are managed by Prefect 2.0
![Concept](https://i.imgur.com/UISh7gO.png)

All of the **observability** and **monitoring** is automatically added to the code execution when you specifiy the **@task** and **@flow** *decorators* in your code 

![Prefect cloud dashboard](https://i.imgur.com/glZpzwv.png)

**Code execution** (*Flows*) can also be deployed to Prefect cloud where they can be parameterized as well as run on specific schedules either defined from UI or cron jobs

![Prefect deployment schedule](https://i.imgur.com/uMH1gOi.png)
## Environment Variables

To run this project, you will need to add the following environment variables to your execution environment

`NIKE_URL` which points to a product's page on Nike store

`MY_BUDGET` i.e. your budget for that product

`SLACK_WEBHOOK_PIKACHU_WORKFLOWS` i.e. slack webhook url which can be generated using [Slack Apps](https://api.slack.com/apps)

## Authors

- [Yasir Khalid](https://www.linkedin.com/in/yasir-khalid)

