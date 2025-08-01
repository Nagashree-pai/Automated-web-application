import { chromium } from 'playwright';

const run = async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto('https://www.wikipedia.org');
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
};

run();
