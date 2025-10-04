from playwright.sync_api import sync_playwright

# Use before_all/after_all for the main Playwright instance
def before_all(context):
    context.p = sync_playwright().start()

def after_all(context):
    if hasattr(context, 'p') and context.p:
        context.p.stop()

# Open a new 'browser' before each scenario
def before_scenario(context, scenario):
    # Launch the browser and save it to context
    context.browser = context.p.chromium.launch(headless=False)
    # Create the 'page' within the context
    context.page = context.browser.new_page()

# Close only the 'browser' after each scenario
def after_scenario(context, scenario):
    # Close context.browser
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()
