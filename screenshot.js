const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 390, height: 844 }); // iPhone 12 Pro size
  await page.goto('http://localhost:8000');
  await page.waitForTimeout(2000); // Wait for React to render
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
})();
