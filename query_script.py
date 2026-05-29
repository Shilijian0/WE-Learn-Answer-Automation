// WE Learn 自动化答题辅助脚本 (单任务可控版)
// 功能：自动识别页面中带有 data-solution 标记的隐藏答案，并自动模拟填写与选中

(function() {
  const allAnswerElements = document.querySelectorAll('[data-solution]');
  let successCount = 0;
  let failCount = 0;

  console.log(`🚀 脚本启动：共检测到 ${allAnswerElements.length} 个带有答案标记的元素。`);

  // 遍历所有带答案标记的元素，自动处理对应题型
  allAnswerElements.forEach((element, index) => {
    const answer = element.dataset.solution.trim();
    const tagName = element.tagName.toUpperCase();
    const taskNum = index + 1;
    
    try {
      // 1. 处理单选题（选项通常为 li 标签）
      if (tagName === 'LI') {
        // 模拟点击选中正确选项
        element.click();
        // 视觉高亮增强反馈
        element.style.backgroundColor = '#28a745';
        element.style.color = '#ffffff';
        element.style.fontWeight = 'bold';
        console.log(`✅ [题号 ${taskNum}] 单选题：已自动选中正确答案`);
        successCount++;
      }

      // 2. 处理单空填空题（input 输入框）
      else if (tagName === 'INPUT') {
        // 填入解析出的答案
        element.value = answer;
        // 触发标准输入和改变事件，确保前端框架（如 Vue/React）能正常捕获到填写的值
        element.dispatchEvent(new Event('input', { bubbles: true }));
        element.dispatchEvent(new Event('change', { bubbles: true }));
        // 边框和背景高亮提醒
        element.style.border = '2px solid #28a745';
        element.style.backgroundColor = '#f0fff4';
        console.log(`✅ [题号 ${taskNum}] 填空题：已自动填入答案 -> "${answer}"`);
        successCount++;
      }

      // 3. 处理长文本答题/翻译题（textarea 文本框）
      else if (tagName === 'TEXTAREA') {
        // 填入长文本答案
        element.value = answer;
        // 触发输入事件，防止表单提交时数据丢失
        element.dispatchEvent(new Event('input', { bubbles: true }));
        element.dispatchEvent(new Event('change', { bubbles: true }));
        // 边框和背景高亮提醒
        element.style.border = '2px solid #28a745';
        element.style.backgroundColor = '#f0fff4';
        console.log(`✅ [题号 ${taskNum}] 长文本/翻译题：已成功填入完整文本`);
        successCount++;
      }

      // 4. 暂时无法处理的未知或复杂题型
      else {
        console.warn(`⚠️ [题号 ${taskNum}] 未知或复合题型 (${tagName})，已安全跳过`);
        failCount++;
      }
    } catch (err) {
      console.error(`❌ [题号 ${taskNum}] 自动化处理时发生异常：`, err);
      failCount++;
    }
  });

  // 最终执行结果汇总打印
  console.log('\n==================== 自动化执行汇总 ====================');
  console.log(`  🎉 成功处理题目：${successCount} 道`);
  console.log(`  ❌ 跳过/失败题目：${failCount} 道`);
  console.log('========================================================');
})();
