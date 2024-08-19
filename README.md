
# Automation with Python

This automation will be covered :
- UI Web Automation
- API Automation

## Prerequisite

**pycharm** - used for your playground, [here](https://www.jetbrains.com/pycharm/download/?section=mac)

Install **python** first in your computer, [here](https://www.python.org/) 



### Installation


run command in pycharm terminal to install **behave**
```bash
  pip install behave
```

And install all of package 

### Directory Tree
```
My Project
├── config
│   └── endpoints.py
├── features
│   ├── api
│   │   └── file_api.feature
│   ├── web
│   │   └── file_web.feature
│   └── steps
│       ├── step_def_api.py
│       └── step_def_web.py  
├── schemas
│   └── schema.json
├── .env
└── locator.py  
```
    
### How to Run

run all in behave

```
behave
```

run by tagging all
```
behave --tags=all
```


run by specific tagging
```
behave --tags={tag}
```