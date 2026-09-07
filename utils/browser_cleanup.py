from playwright.sync_api import Page


def clear_browser_data(page: Page) -> None:
    """
    Clear browser-side data before starting the test.
    """

    context = page.context

    # Clear cookies
    context.clear_cookies()

    # Clear browser cache for Chromium
    try:
        cdp = context.new_cdp_session(page)
        cdp.send("Network.enable")
        cdp.send("Network.clearBrowserCache")
        cdp.send("Network.clearBrowserCookies")
    except Exception:
        pass

    # Open the application origin so storage can be cleared
    page.goto(
        "https://staging-v2-admin.escapeplan.ie",
        wait_until="domcontentloaded",
    )

    # Clear local/session storage and IndexedDB
    page.evaluate(
        """
        async () => {
            localStorage.clear();
            sessionStorage.clear();

            if (window.indexedDB && indexedDB.databases) {
                const databases = await indexedDB.databases();

                for (const db of databases) {
                    if (db.name) {
                        indexedDB.deleteDatabase(db.name);
                    }
                }
            }
        }
        """
    )