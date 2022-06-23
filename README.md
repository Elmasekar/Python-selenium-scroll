# How to scroll webpage in automation test in Python-selenium on [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=Python-selenium-scroll)

If you want to test scrolling of a webpage using an automation test in Python-selenium on LambdaTest, you can use the follwing steps. You can refer to sample test repo [here](https://github.com/LambdaTest/python-selenium-sample).

# Steps

## Scrolling to bottom of the page

To scroll to the bottom of the page, you can use the following line of code (refer to `scroll.py` for full code):

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

## Infitinite scroll

If you want **to scroll to a page with infinite loading**, like social network ones, facebook etc. You can use the following code (refer to `lambdatest.py` for full code):

```python
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

#controls how many times scrolled to bottom
scroll_pass = 0

#change to True for infinite scroll
while scroll_pass < 10:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height 
    scroll_passs+=1
```
## Run your test

```bash
python lambdatest.py
```

# Links:

[LambdaTest Community](http://community.lambdatest.com/)

