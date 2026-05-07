const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false }); // Set to false if you want to see it in a window, but since we are in a CLI, we'll use screenshots if needed.
  const page = await browser.newPage();
  await page.setViewportSize({ width: 390, height: 844 });
  
  console.log('--- Starting Automated Walkthrough ---');
  
  // 1. Intro Step
  await page.goto('http://localhost:8000');
  console.log('Step: Intro');
  await page.fill('input[placeholder*="이름을 새기게나"]', 'Gemini Hunter');
  await page.waitForTimeout(2000);
  await page.click('button:has-text("모험 시작하기")');

  // 2. Map Step
  console.log('Step: Map');
  await page.waitForTimeout(2000);
  
  // 3. Open a Mission Hint
  console.log('Step: Mission Hint');
  await page.click('text=⚓'); // Click the first mission
  await page.waitForTimeout(2000);
  
  // 4. Cheat/Complete Missions (using the "Demo" bypass buttons if available or clicking all)
  console.log('Step: Completing Missions...');
  await page.click('text=강제 인증하기');
  await page.waitForTimeout(1000);
  
  await page.click('text=🛶');
  await page.waitForTimeout(1000);
  await page.click('text=강제 인증하기');
  await page.waitForTimeout(1000);
  
  await page.click('text=🌊');
  await page.waitForTimeout(1000);
  await page.click('text=강제 인증하기');
  await page.waitForTimeout(2000);

  // 5. Admin/Staff Verification Step
  console.log('Step: Admin Verification');
  await page.click('button:has-text("보물 상자 열기")');
  await page.waitForTimeout(2000);
  await page.fill('input[placeholder="0000"]', '7777');
  await page.waitForTimeout(1000);
  await page.click('button:has-text("금고 열기")');

  // 6. Ending Story Step
  console.log('Step: Ending Story');
  await page.waitForTimeout(2000); // Wait for animations
  await page.click('button:has-text("임명장 확인하기")');

  // 7. Reward/Certificate Step
  console.log('Step: Reward & Certificate');
  await page.waitForTimeout(2000);
  
  console.log('--- Walkthrough Complete ---');
  await browser.close();
})();
