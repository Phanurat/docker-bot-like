const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: false }); // เปิด browser ในโหมดที่ไม่ใช่ headless เพื่อให้เห็นหน้าจอ
    const page = await browser.newPage();

    // ตั้งค่าคุกกี้
    const cookies = [
        {
            name: 'c_user',
            value: '100020688590532',
            domain: '.facebook.com',
            path: '/',
            expires: new Date('2025-05-29T06:53:31.187Z').getTime() / 1000,
            httpOnly: false,
            secure: true,
            session: false,
            sameSite: 'None'
        },
        {
            name: 'xs',
            value: '38%3AWo3dORZPK5KMkw%3A2%3A1716974618%3A-1%3A11361',
            domain: '.facebook.com',
            path: '/',
            expires: new Date('2025-05-29T06:53:31.187Z').getTime() / 1000,
            httpOnly: true,
            secure: true,
            session: false,
            sameSite: 'None'
        },
        {
            name: 'datr',
            value: 'eOlPZjhhJxb4hoWIuz9f0v-b',
            domain: '.facebook.com',
            path: '/',
            expires: new Date('2025-06-28T01:12:26.667Z').getTime() / 1000,
            httpOnly: true,
            secure: true,
            session: false,
            sameSite: 'None'
        },
        {
            name: 'fr',
            value: '1NH1qvOmWkHD93yqj.AWXCazSHf2-scMGEuV0678FniU0.BmVu89..AAA.0.0.BmVvQb.AWWN1xD4904',
            domain: '.facebook.com',
            path: '/',
            expires: new Date('2024-08-27T06:53:31.187Z').getTime() / 1000,
            httpOnly: true,
            secure: true,
            session: false,
            sameSite: 'None'
        }
    ];

    await page.setCookie(...cookies);

    // ไปที่หน้าโปรไฟล์ของ Facebook เพื่อเช็คว่าเข้าสู่ระบบสำเร็จหรือไม่
    await page.goto('https://www.facebook.com', { waitUntil: 'networkidle2' });

    // ตรวจสอบว่ามีองค์ประกอบที่บ่งบอกว่าเข้าสู่ระบบสำเร็จ
    const isLoggedIn = await page.evaluate(() => {
        return !!document.querySelector('[aria-label="Create a post"]');
    });

    if (isLoggedIn) {
        console.log('Logged in successfully');

        // ไปที่ลิงก์ของโพสต์ที่ต้องการไลค์
        await page.goto('https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid0SNry3kALTR2aEEGZyPim71burUwc3bxmsViNPcG78AKv3mg3VMk38ZAv4S4nFpBkl', { waitUntil: 'networkidle2' });

        // เลื่อนหน้าจอลงเพื่อค้นหาปุ่มไลค์
        await page.evaluate(async () => {
            const distance = 100; // ระยะทางในการเลื่อนในแต่ละครั้ง
            const delay = 100; // หน่วงเวลาในการเลื่อนแต่ละครั้ง

            while (!document.querySelector('div[aria-label="Like"]')) {
                window.scrollBy(0, distance);
                await new Promise(resolve => setTimeout(resolve, delay));
            }
        });

        // รอให้ปุ่มไลค์ปรากฏขึ้น
        await page.waitForSelector('div[aria-label="Like"]', { visible: true });

        // วางเมาส์บนปุ่มไลค์เพื่อเปิดไอคอน reactions
        const likeButton = await page.$('div[aria-label="Like"]');
        await likeButton.hover();

        // รอให้การคลิกทำงานเสร็จ
        await new Promise(resolve => setTimeout(resolve, 2000));

    } else {
        console.log('Failed to log in');
    }

    // ปิด browser
    await browser.close();
})();
