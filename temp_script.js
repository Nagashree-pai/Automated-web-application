import { chromium } from 'playwright';

(async () => {
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();

    console.log("Launching browser");
    await page.goto('https://www.youtube.com');
    console.log("Navigated to YouTube");

    await page.type('#search', 'tiger');
    await Promise.all([
        page.waitForSelector('#search-icon-legacy'),
        page.keyboard.press('Enter')
    ]);
    console.log("Searched for tiger");

    await page.waitForSelector('.yt-lockup-title');
    const screenshotBuffer = await page.screenshot({ fullPage: true });
    console.log("Took screenshot");

    await browser.close();
    console.log("Browser closed");

    // Save the screenshot to a file named 'screenshot.png' in the current directory
    const fs = require('fs');
    fs.writeFileSync('screenshot.png', screenshotBuffer, 'base64');
})();