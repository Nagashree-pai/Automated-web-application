const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false }); // <- important if you want to see the browser
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.google.com');
  await browser.close();
})();
