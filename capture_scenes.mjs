import puppeteer from 'puppeteer-core';
import path from 'path';
import fs from 'fs';

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

export async function captureLessonScenes(lessonNum, scenesCount) {
  const folderName = `lesson_${String(lessonNum).padStart(2, '0')}`;
  const lessonDir = path.resolve('course_grok_bot', 'videos', folderName);
  const htmlPath = path.join(lessonDir, 'index.html');

  if (!fs.existsSync(htmlPath)) {
    throw new Error(`HTML súbor pre lekciu ${lessonNum} neexistuje: ${htmlPath}`);
  }

  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-web-security',
      '--allow-file-access-from-files',
      '--window-size=1920,1080'
    ]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  
  const fileUrl = `file:///${htmlPath.replace(/\\/g, '/')}`;
  await page.goto(fileUrl, { waitUntil: 'networkidle0' });

  const capturedPaths = [];
  for (let idx = 0; idx < scenesCount; idx++) {
    await page.evaluate((targetIdx) => {
      document.querySelectorAll('.scene-card').forEach(item => {
        item.classList.remove('active');
        item.style.opacity = '0';
        item.style.visibility = 'hidden';
      });
      const el = document.getElementById(`scene-${targetIdx}`);
      if (el) {
        el.classList.add('active');
        el.style.opacity = '1';
        el.style.visibility = 'visible';
        el.style.transform = 'translateY(0px) scale(1)';
      }
    }, idx);

    await new Promise(r => setTimeout(r, 120));

    const imgPath = path.join(lessonDir, `scene_${idx}.png`);
    await page.screenshot({ path: imgPath, type: 'png' });
    capturedPaths.push(imgPath);
  }

  await browser.close();
  return capturedPaths;
}

// CLI usage: node capture_scenes.mjs <lessonNum> <scenesCount>
if (process.argv[1] && process.argv[1].endsWith('capture_scenes.mjs')) {
  const lessonNum = parseInt(process.argv[2] || '1', 10);
  const scenesCount = parseInt(process.argv[3] || '4', 10);
  captureLessonScenes(lessonNum, scenesCount)
    .then((paths) => {
      console.log(JSON.stringify({ success: true, paths }));
    })
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
}
