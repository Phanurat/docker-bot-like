const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    
    // Navigate to Facebook's signup page
    await page.goto('https://www.facebook.com/r.php');

    // Fill out the sign-up form
    await page.type('input[name="firstname"]', 'Silip');
    await page.type('input[name="lastname"]', 'Napap');
    await page.type('input[name="reg_email__"]', 'silip_napap@getnada.com');
    
    // Confirm email
    await page.type('input[name="reg_email_confirmation__"]', 'silip_napap@getnada.com');
    
    await page.type('input[name="reg_passwd__"]', 'Ppass252544');
    
    // Select birth date
    await page.select('select[name="birthday_day"]', '15');
    await page.select('select[name="birthday_month"]', '6'); // June
    await page.select('select[name="birthday_year"]', '1990');

    // Select gender
    await page.click('input[name="sex"][value="2"]'); // Select male (value="2"), female is value="1"

    // Click the Sign-Up button
    await page.click('button[name="websubmit"]');

    // Wait for a while to let the form submit (adjust as needed)
    await page.waitForTimeout(5000);

    // Close the browser
    await browser.close();
})().catch(err => {
    console.error(err);
});
